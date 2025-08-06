/**
 * Archimedes Model Implementation
 * Based on the fitted logistic regression model for predicting future power
 */

class ArchimedesModel {
    constructor() {
        // Model coefficients from the fitted model (standardized)
        this.coefficients = {
            intercept: 0.0,  // Will be calculated based on time
            military: -0.466,      // m_t_lag1 coefficient
            education: 0.127,      // e_t_lag1 coefficient  
            volatility: 0.513,     // v_t_lag1 coefficient
            exchange: -0.071,      // sigma_fx_t_lag1 coefficient
            time: 0.219,           // time coefficient
            time2: 0.044,          // time^2 coefficient
            time3: 0.051           // time^3 coefficient
        };

        // Model statistics
        this.modelStats = {
            auc: 0.613,
            accuracy: 0.552,
            trainingPeriod: '1826-1956',
            observations: 58
        };

        // Normalization parameters (approximate ranges from historical data)
        this.normalization = {
            military: { min: -2.0, max: 2.0 },
            education: { min: -1.0, max: 1.5 },
            volatility: { min: -2.0, max: 3.0 },
            exchange: { min: -1.0, max: 2.0 }
        };

        // Current time normalized (using mid-point of training period as reference)
        this.referenceYear = 1891; // Mid-point of 1826-1956
        this.currentYear = new Date().getFullYear();
        this.timeNormalized = this.normalizeTime(this.currentYear);
    }

    /**
     * Normalize time to [0, 1] range based on training period
     */
    normalizeTime(year) {
        const minYear = 1826;
        const maxYear = 1956;
        return Math.max(0, Math.min(1, (year - minYear) / (maxYear - minYear)));
    }

    /**
     * Standardize input values to match model training
     */
    standardizeInputs(inputs) {
        const standardized = {};
        
        // Convert -1 to 1 range to standardized values
        for (const [key, value] of Object.entries(inputs)) {
            if (this.normalization[key]) {
                const range = this.normalization[key];
                // Map from [-1, 1] to [min, max] then standardize
                const scaledValue = value * (range.max - range.min) / 2 + (range.max + range.min) / 2;
                standardized[key] = scaledValue;
            }
        }
        
        return standardized;
    }

    /**
     * Sigmoid function for logistic regression
     */
    sigmoid(z) {
        return 1 / (1 + Math.exp(-Math.max(-500, Math.min(500, z)))); // Clamp to prevent overflow
    }

    /**
     * Predict probability using the logistic regression model
     */
    predict(inputs) {
        const standardized = this.standardizeInputs(inputs);
        
        // Calculate time features
        const t = this.timeNormalized;
        const t2 = t * t;
        const t3 = t * t * t;
        
        // Calculate linear combination
        let z = this.coefficients.intercept +
                this.coefficients.military * standardized.military +
                this.coefficients.education * standardized.education +
                this.coefficients.volatility * standardized.volatility +
                this.coefficients.exchange * standardized.exchange +
                this.coefficients.time * t +
                this.coefficients.time2 * t2 +
                this.coefficients.time3 * t3;
        
        // Apply sigmoid to get probability
        const probability = this.sigmoid(z);
        
        return {
            probability: probability,
            powerScore: 2 * probability - 1, // Convert to [-1, 1] range
            confidence: this.calculateConfidence(probability),
            factors: this.analyzeFactors(standardized, probability)
        };
    }

    /**
     * Calculate confidence based on how extreme the probability is
     */
    calculateConfidence(probability) {
        // Higher confidence for probabilities closer to 0 or 1
        const distance = Math.abs(probability - 0.5);
        return Math.min(1.0, distance * 2);
    }

    /**
     * Analyze which factors are contributing most to the prediction
     */
    analyzeFactors(standardized, probability) {
        const factors = [];
        
        // Calculate individual contributions
        const contributions = {
            military: this.coefficients.military * standardized.military,
            education: this.coefficients.education * standardized.education,
            volatility: this.coefficients.volatility * standardized.volatility,
            exchange: this.coefficients.exchange * standardized.exchange
        };

        // Sort by absolute contribution
        const sortedFactors = Object.entries(contributions)
            .sort((a, b) => Math.abs(b[1]) - Math.abs(a[1]));

        for (const [factor, contribution] of sortedFactors) {
            const impact = contribution > 0 ? 'positive' : 'negative';
            const strength = Math.abs(contribution);
            
            let description = '';
            switch (factor) {
                case 'military':
                    description = contribution > 0 
                        ? 'Military strength supports growth' 
                        : 'Military focus may limit economic development';
                    break;
                case 'education':
                    description = contribution > 0 
                        ? 'Education systems drive advancement' 
                        : 'Educational disadvantage limits progress';
                    break;
                case 'volatility':
                    description = contribution > 0 
                        ? 'Economic dynamism fuels growth' 
                        : 'Economic stability may limit structural change';
                    break;
                case 'exchange':
                    description = contribution > 0 
                        ? 'Currency volatility indicates dynamism' 
                        : 'Exchange rate stability supports development';
                    break;
            }

            factors.push({
                name: this.getFactorDisplayName(factor),
                impact: impact,
                strength: strength,
                description: description,
                coefficient: this.coefficients[factor]
            });
        }

        return factors;
    }

    /**
     * Get display name for factors
     */
    getFactorDisplayName(factor) {
        const names = {
            military: 'Military Power',
            education: 'Education Level',
            volatility: 'Economic Volatility',
            exchange: 'Currency Stability'
        };
        return names[factor] || factor;
    }

    /**
     * Generate historical context based on inputs
     */
    generateHistoricalContext(inputs, prediction) {
        const contexts = [
            {
                condition: inputs.military > 0.5 && inputs.volatility > 0.5,
                text: "Your civilization shows the dynamic militarism characteristic of rising powers during periods of rapid change, similar to the United States during the Civil War era."
            },
            {
                condition: inputs.education > 0.5 && inputs.exchange < -0.3,
                text: "High education with stable currency mirrors the conditions that supported sustained growth in advanced economies during the Industrial Revolution."
            },
            {
                condition: inputs.volatility > 0.7,
                text: "Extreme economic volatility suggests your civilization is undergoing rapid structural transformation, which historically has been both opportunity and risk."
            },
            {
                condition: inputs.military < -0.5 && inputs.education > 0.3,
                text: "Your focus on education over military might reflects the peaceful development path taken by some successful civilizations."
            },
            {
                condition: prediction.probability > 0.7,
                text: "The model predicts strong growth potential, similar to the conditions that preceded major economic expansions in history."
            },
            {
                condition: prediction.probability < 0.3,
                text: "Current conditions suggest challenges ahead, reminiscent of periods when established powers faced structural headwinds."
            }
        ];

        // Find the first matching context
        const matchingContext = contexts.find(ctx => ctx.condition);
        return matchingContext ? matchingContext.text : 
            "Your civilization's parameters create a unique combination not commonly seen in historical data.";
    }

    /**
     * Get model information for display
     */
    getModelInfo() {
        return {
            name: "Archimedes Model",
            description: "Logistic regression model for predicting future power transitions",
            performance: this.modelStats,
            predictors: [
                { name: "Military Power Ratio", coefficient: this.coefficients.military, description: "Relative military strength" },
                { name: "Education Ratio", coefficient: this.coefficients.education, description: "Educational advancement" },
                { name: "Food Price Volatility", coefficient: this.coefficients.volatility, description: "Economic dynamism" },
                { name: "Exchange Rate Volatility", coefficient: this.coefficients.exchange, description: "Currency stability" }
            ],
            trainingData: {
                period: this.modelStats.trainingPeriod,
                observations: this.modelStats.observations,
                target: "Whether GDP advantage increases over next 5 years"
            }
        };
    }

    /**
     * Validate inputs
     */
    validateInputs(inputs) {
        const required = ['military', 'education', 'volatility', 'exchange'];
        const errors = [];

        for (const field of required) {
            if (!(field in inputs)) {
                errors.push(`Missing required field: ${field}`);
            } else if (typeof inputs[field] !== 'number') {
                errors.push(`Field ${field} must be a number`);
            } else if (inputs[field] < -1 || inputs[field] > 1) {
                errors.push(`Field ${field} must be between -1 and 1`);
            }
        }

        return {
            isValid: errors.length === 0,
            errors: errors
        };
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ArchimedesModel;
}
