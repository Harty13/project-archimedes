#!/usr/bin/env python3
"""
Script to fit the Archimedes logistic regression model for predicting future power
Based on the model specification in model/ArchimedesModel.tex
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.pipeline import Pipeline
from scipy import stats
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')

def load_ratio_data():
    """Load all ratio data from the combined CSV files"""
    print("Loading US/UK ratio data...")
    
    # Load the combined wide format data
    wide_data_path = Path("data/ratios/all_ratios_combined_wide.csv")
    if not wide_data_path.exists():
        print("Error: Combined ratio data not found. Run analyze_all_ratios.py first.")
        return pd.DataFrame()
    
    df = pd.read_csv(wide_data_path)
    
    print(f"Loaded data: {len(df)} years from {df['Year'].min()}-{df['Year'].max()}")
    print(f"Available ratios: {[col for col in df.columns if col != 'Year']}")
    
    return df

def prepare_predictors(df):
    """Prepare the predictor variables according to the model specification"""
    print("\nPreparing predictor variables...")
    
    # Create a copy for processing
    data = df.copy()
    
    # Map column names to model variables (excluding GDP ratio from predictors)
    predictor_mapping = {
        'Military Power Ratio': 'm_t', 
        'Education Ratio': 'e_t',
        'Food Price Volatility Ratio': 'v_t',
        'Exchange Rate Volatility': 'sigma_fx_t'
    }
    
    # Keep GDP ratio for target creation only
    if 'GDP Ratio' in data.columns:
        data['g_t'] = data['GDP Ratio']
    
    # Rename columns and take log where appropriate
    for original_name, model_name in predictor_mapping.items():
        if original_name in data.columns:
            if model_name in ['m_t', 'e_t', 'v_t']:
                # These are already log ratios or should be log-transformed
                data[model_name] = data[original_name]
            else:
                # Exchange rate volatility - use as is
                data[model_name] = data[original_name]
        else:
            print(f"Warning: {original_name} not found in data")
            data[model_name] = np.nan
    
    # Keep only the model variables, GDP ratio for target, and Year
    model_vars = ['Year', 'g_t'] + list(predictor_mapping.values())
    data = data[model_vars].copy()
    
    print(f"Prepared predictors: {list(predictor_mapping.values())}")
    print(f"Data coverage: {data.dropna().shape[0]} complete observations")
    
    return data

def create_target_variable(data, horizon=5):
    """Create the binary target variable Y^(h)_t"""
    print(f"\nCreating target variable with horizon h={horizon} years...")
    
    # Use GDP ratio as the power score (PTT-lite approach)
    if 'g_t' not in data.columns:
        print("Error: GDP ratio not available for target creation")
        return data
    
    # Create future GDP ratio
    data = data.sort_values('Year').reset_index(drop=True)
    data[f'g_t_plus_{horizon}'] = data['g_t'].shift(-horizon)
    
    # Since US always leads in GDP, use relative improvement/decline as target
    # Y^(h)_t = 1 if US GDP advantage increases over the next h years
    data['gdp_change'] = data[f'g_t_plus_{horizon}'] - data['g_t']
    data[f'Y_h{horizon}'] = (data['gdp_change'] > 0).astype(int)
    
    # Remove the last h years (no target available)
    data = data[:-horizon].copy()
    
    target_stats = data[f'Y_h{horizon}'].value_counts()
    print(f"Target variable Y^({horizon}) - US GDP advantage increases:")
    print(f"  Advantage increases: {target_stats.get(1, 0)} years ({target_stats.get(1, 0)/len(data)*100:.1f}%)")
    print(f"  Advantage decreases: {target_stats.get(0, 0)} years ({target_stats.get(0, 0)/len(data)*100:.1f}%)")
    
    # Check if we have both classes
    if len(target_stats) < 2:
        print("Warning: Only one class in target variable. Using median split instead.")
        # Use median split as alternative
        median_change = data['gdp_change'].median()
        data[f'Y_h{horizon}'] = (data['gdp_change'] > median_change).astype(int)
        target_stats = data[f'Y_h{horizon}'].value_counts()
        print(f"Median split target:")
        print(f"  Above median: {target_stats.get(1, 0)} years ({target_stats.get(1, 0)/len(data)*100:.1f}%)")
        print(f"  Below median: {target_stats.get(0, 0)} years ({target_stats.get(0, 0)/len(data)*100:.1f}%)")
    
    return data

def add_lags(data, lag=1):
    """Add lagged predictors to reduce simultaneity"""
    print(f"\nAdding {lag}-year lags to predictors...")
    
    predictors = ['g_t', 'm_t', 'e_t', 'v_t', 'sigma_fx_t']
    
    for pred in predictors:
        if pred in data.columns:
            data[f'{pred}_lag{lag}'] = data[pred].shift(lag)
    
    # Remove the first lag years
    data = data[lag:].reset_index(drop=True)
    
    print(f"Data after lagging: {len(data)} observations")
    return data

def fit_logistic_model(data, horizon=5, lag=1, use_ridge=True, alpha=1.0):
    """Fit the logistic regression model"""
    print(f"\nFitting logistic model (horizon={horizon}, lag={lag}, ridge={use_ridge})...")
    
    # Define predictor columns (excluding GDP ratio)
    predictor_cols = [f'm_t_lag{lag}', f'e_t_lag{lag}', 
                     f'v_t_lag{lag}', f'sigma_fx_t_lag{lag}']
    target_col = f'Y_h{horizon}'
    
    # Filter to complete cases
    model_data = data[['Year'] + predictor_cols + [target_col]].dropna()
    
    if len(model_data) == 0:
        print("Error: No complete observations for modeling")
        return None, None, None
    
    print(f"Model data: {len(model_data)} complete observations")
    print(f"Year range: {model_data['Year'].min()}-{model_data['Year'].max()}")
    
    # Prepare features and target
    X = model_data[predictor_cols].values
    y = model_data[target_col].values
    years = model_data['Year'].values
    
    # Add time trend (cubic spline approximation using polynomial)
    time_normalized = (years - years.min()) / (years.max() - years.min())
    time_features = np.column_stack([time_normalized, time_normalized**2, time_normalized**3])
    X_with_time = np.column_stack([X, time_features])
    
    # Feature names for interpretation
    feature_names = predictor_cols + ['time', 'time^2', 'time^3']
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_with_time)
    
    # Fit model
    if use_ridge:
        model = LogisticRegression(penalty='l2', C=1/alpha, random_state=42, max_iter=1000)
    else:
        model = LogisticRegression(penalty=None, random_state=42, max_iter=1000)
    
    model.fit(X_scaled, y)
    
    # Predictions
    y_pred_proba = model.predict_proba(X_scaled)[:, 1]
    y_pred = model.predict(X_scaled)
    
    # Model performance
    auc_score = roc_auc_score(y, y_pred_proba)
    
    print(f"\nModel Performance:")
    print(f"AUC Score: {auc_score:.3f}")
    print(f"Accuracy: {(y_pred == y).mean():.3f}")
    
    # Create results dataframe
    results = pd.DataFrame({
        'Year': years,
        'Y_actual': y,
        'Y_pred_proba': y_pred_proba,
        'Y_pred': y_pred,
        'Power_Score': 2 * y_pred_proba - 1  # S^(h)_t = 2*q^(h)_t - 1
    })
    
    # Model coefficients
    coef_df = pd.DataFrame({
        'Feature': feature_names,
        'Coefficient': model.coef_[0],
        'Abs_Coefficient': np.abs(model.coef_[0])
    }).sort_values('Abs_Coefficient', ascending=False)
    
    model_info = {
        'model': model,
        'scaler': scaler,
        'feature_names': feature_names,
        'coefficients': coef_df,
        'auc_score': auc_score,
        'n_obs': len(model_data),
        'year_range': (model_data['Year'].min(), model_data['Year'].max())
    }
    
    return results, model_info, model_data

def evaluate_model(results, model_info):
    """Evaluate model performance and create diagnostic plots"""
    print(f"\n" + "="*60)
    print("MODEL EVALUATION")
    print("="*60)
    
    # Basic statistics
    y_true = results['Y_actual']
    y_pred_proba = results['Y_pred_proba']
    y_pred = results['Y_pred']
    
    print(f"\nModel Statistics:")
    print(f"Observations: {model_info['n_obs']}")
    print(f"Year range: {model_info['year_range'][0]}-{model_info['year_range'][1]}")
    print(f"AUC Score: {model_info['auc_score']:.3f}")
    print(f"Accuracy: {(y_pred == y_true).mean():.3f}")
    
    # Classification report
    print(f"\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=['UK Leads', 'US Leads']))
    
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    print(f"\nConfusion Matrix:")
    print(f"                Predicted")
    print(f"Actual    UK    US")
    print(f"UK       {cm[0,0]:3d}   {cm[0,1]:3d}")
    print(f"US       {cm[1,0]:3d}   {cm[1,1]:3d}")
    
    # Coefficient interpretation
    print(f"\nModel Coefficients (standardized):")
    print("-" * 40)
    for _, row in model_info['coefficients'].head(8).iterrows():
        direction = "+" if row['Coefficient'] > 0 else "-"
        print(f"{row['Feature']:20s}: {direction}{abs(row['Coefficient']):6.3f}")
    
    return True

def create_diagnostic_plots(results, model_info):
    """Create diagnostic plots for model evaluation"""
    print(f"\nCreating diagnostic plots...")
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Archimedes Model Diagnostic Plots', fontsize=16, fontweight='bold')
    
    # 1. Predicted probabilities over time
    ax1 = axes[0, 0]
    ax1.plot(results['Year'], results['Y_pred_proba'], 'b-', linewidth=2, alpha=0.7)
    ax1.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Decision Threshold')
    ax1.fill_between(results['Year'], 0, results['Y_pred_proba'], alpha=0.3)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('P(US Leads at t+h)')
    ax1.set_title('Predicted Probability Over Time')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Power score over time
    ax2 = axes[0, 1]
    colors = ['red' if score < 0 else 'blue' for score in results['Power_Score']]
    ax2.scatter(results['Year'], results['Power_Score'], c=colors, alpha=0.6)
    ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Power Score S^(h)_t')
    ax2.set_title('Power Score Over Time\n(Blue=US Favored, Red=UK Favored)')
    ax2.grid(True, alpha=0.3)
    
    # 3. ROC Curve
    ax3 = axes[0, 2]
    fpr, tpr, _ = roc_curve(results['Y_actual'], results['Y_pred_proba'])
    ax3.plot(fpr, tpr, 'b-', linewidth=2, label=f'ROC (AUC = {model_info["auc_score"]:.3f})')
    ax3.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Random')
    ax3.set_xlabel('False Positive Rate')
    ax3.set_ylabel('True Positive Rate')
    ax3.set_title('ROC Curve')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Coefficient plot
    ax4 = axes[1, 0]
    coef_data = model_info['coefficients'].head(8)
    colors = ['red' if x < 0 else 'blue' for x in coef_data['Coefficient']]
    bars = ax4.barh(range(len(coef_data)), coef_data['Coefficient'], color=colors, alpha=0.7)
    ax4.set_yticks(range(len(coef_data)))
    ax4.set_yticklabels(coef_data['Feature'])
    ax4.set_xlabel('Coefficient Value')
    ax4.set_title('Model Coefficients\n(Blue=Pro-US, Red=Pro-UK)')
    ax4.axvline(x=0, color='black', linestyle='-', alpha=0.5)
    ax4.grid(True, alpha=0.3)
    
    # 5. Actual vs Predicted
    ax5 = axes[1, 1]
    actual_colors = ['red' if x == 0 else 'blue' for x in results['Y_actual']]
    ax5.scatter(results['Year'], results['Y_pred_proba'], c=actual_colors, alpha=0.6)
    ax5.axhline(y=0.5, color='black', linestyle='--', alpha=0.5)
    ax5.set_xlabel('Year')
    ax5.set_ylabel('Predicted Probability')
    ax5.set_title('Actual vs Predicted\n(Blue=US Actually Led, Red=UK Actually Led)')
    ax5.grid(True, alpha=0.3)
    
    # 6. Residuals over time
    ax6 = axes[1, 2]
    residuals = results['Y_actual'] - results['Y_pred_proba']
    ax6.scatter(results['Year'], residuals, alpha=0.6)
    ax6.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    ax6.set_xlabel('Year')
    ax6.set_ylabel('Residuals (Actual - Predicted)')
    ax6.set_title('Residuals Over Time')
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('plots/archimedes_model_diagnostics.png', dpi=300, bbox_inches='tight')
    print("Diagnostic plots saved to 'plots/archimedes_model_diagnostics.png'")
    plt.show()

def cross_validate_model(data, horizon=5, lag=1, n_splits=5):
    """Perform time series cross-validation"""
    print(f"\nPerforming time series cross-validation ({n_splits} splits)...")
    
    predictor_cols = [f'm_t_lag{lag}', f'e_t_lag{lag}', 
                     f'v_t_lag{lag}', f'sigma_fx_t_lag{lag}']
    target_col = f'Y_h{horizon}'
    
    model_data = data[['Year'] + predictor_cols + [target_col]].dropna()
    
    if len(model_data) < n_splits * 2:
        print(f"Warning: Not enough data for {n_splits}-fold CV. Using {len(model_data)//2} splits.")
        n_splits = max(2, len(model_data)//2)
    
    X = model_data[predictor_cols].values
    y = model_data[target_col].values
    years = model_data['Year'].values
    
    # Add time trend
    time_normalized = (years - years.min()) / (years.max() - years.min())
    time_features = np.column_stack([time_normalized, time_normalized**2, time_normalized**3])
    X_with_time = np.column_stack([X, time_features])
    
    # Time series split
    tscv = TimeSeriesSplit(n_splits=n_splits)
    
    cv_scores = []
    cv_accuracies = []
    
    for fold, (train_idx, test_idx) in enumerate(tscv.split(X_with_time)):
        X_train, X_test = X_with_time[train_idx], X_with_time[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        
        # Standardize
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Fit model
        model = LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000)
        model.fit(X_train_scaled, y_train)
        
        # Predict
        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        y_pred = model.predict(X_test_scaled)
        
        # Score
        if len(np.unique(y_test)) > 1:  # Only calculate AUC if both classes present
            auc = roc_auc_score(y_test, y_pred_proba)
            cv_scores.append(auc)
        
        accuracy = (y_pred == y_test).mean()
        cv_accuracies.append(accuracy)
        
        print(f"Fold {fold+1}: AUC = {auc:.3f}, Accuracy = {accuracy:.3f}")
    
    print(f"\nCross-Validation Results:")
    print(f"Mean AUC: {np.mean(cv_scores):.3f} ± {np.std(cv_scores):.3f}")
    print(f"Mean Accuracy: {np.mean(cv_accuracies):.3f} ± {np.std(cv_accuracies):.3f}")
    
    return cv_scores, cv_accuracies

def main():
    """Main function to run the complete analysis"""
    print("ARCHIMEDES MODEL: LOGISTIC REGRESSION FOR FUTURE POWER PREDICTION")
    print("=" * 70)
    
    # Ensure plots directory exists
    Path("plots").mkdir(exist_ok=True)
    
    # Load data
    df = load_ratio_data()
    if df.empty:
        return
    
    # Prepare predictors
    data = prepare_predictors(df)
    
    # Create target variable
    horizon = 5
    data = create_target_variable(data, horizon=horizon)
    
    # Add lags
    lag = 1
    data = add_lags(data, lag=lag)
    
    # Fit model
    results, model_info, model_data = fit_logistic_model(data, horizon=horizon, lag=lag)
    
    if results is None:
        print("Model fitting failed!")
        return
    
    # Evaluate model
    evaluate_model(results, model_info)
    
    # Create diagnostic plots
    create_diagnostic_plots(results, model_info)
    
    # Cross-validation
    cv_scores, cv_accuracies = cross_validate_model(data, horizon=horizon, lag=lag)
    
    # Export results
    results.to_csv('data/archimedes_model_predictions.csv', index=False)
    model_info['coefficients'].to_csv('data/archimedes_model_coefficients.csv', index=False)
    
    print(f"\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
    print("Generated files:")
    print("  - plots/archimedes_model_diagnostics.png")
    print("  - data/archimedes_model_predictions.csv")
    print("  - data/archimedes_model_coefficients.csv")
    
    return results, model_info

if __name__ == "__main__":
    main()
