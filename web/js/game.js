/**
 * Main Game Logic for The Great Game
 * Coordinates the UI, model predictions, and globe visualization
 */

class GreatGame {
    constructor() {
        this.model = new ArchimedesModel();
        this.globe = null;
        this.currentInputs = {
            military: 0,
            education: 0,
            volatility: 0,
            exchange: 0
        };
        this.currentPrediction = null;
        
        this.init();
    }

    init() {
        // Initialize globe
        this.globe = new Globe('globe-canvas');
        
        // Setup event listeners
        this.setupSliders();
        this.setupButtons();
        this.setupModals();
        
        // Initial prediction
        this.updatePrediction();
        
        console.log('The Great Game initialized successfully!');
    }

    setupSliders() {
        const sliders = [
            { id: 'military-slider', valueId: 'military-value', key: 'military' },
            { id: 'education-slider', valueId: 'education-value', key: 'education' },
            { id: 'volatility-slider', valueId: 'volatility-value', key: 'volatility' },
            { id: 'exchange-slider', valueId: 'exchange-value', key: 'exchange' }
        ];

        sliders.forEach(slider => {
            const element = document.getElementById(slider.id);
            const valueDisplay = document.getElementById(slider.valueId);
            
            if (element && valueDisplay) {
                element.addEventListener('input', (e) => {
                    const value = parseFloat(e.target.value);
                    this.currentInputs[slider.key] = value;
                    valueDisplay.textContent = value.toFixed(1);
                    
                    // Update prediction in real-time
                    this.updatePrediction();
                });
            }
        });
    }

    setupButtons() {
        // Simulate button
        const simulateBtn = document.getElementById('simulate-btn');
        if (simulateBtn) {
            simulateBtn.addEventListener('click', () => {
                this.runSimulation();
            });
        }

        // Reset button
        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                this.resetParameters();
            });
        }

        // About link
        const aboutLink = document.getElementById('about-link');
        if (aboutLink) {
            aboutLink.addEventListener('click', (e) => {
                e.preventDefault();
                this.showModal('about-modal');
            });
        }
    }

    setupModals() {
        // Close buttons
        const closeButtons = document.querySelectorAll('.close');
        closeButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const modal = e.target.closest('.modal');
                if (modal) {
                    this.closeModal(modal.id);
                }
            });
        });

        // Click outside to close
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    this.closeModal(modal.id);
                }
            });
        });
    }

    updatePrediction() {
        // Validate inputs
        const validation = this.model.validateInputs(this.currentInputs);
        if (!validation.isValid) {
            console.warn('Invalid inputs:', validation.errors);
            return;
        }

        // Get prediction (but don't show results until simulation is run)
        this.currentPrediction = this.model.predict(this.currentInputs);
        
        // Only update globe and context, not the results display
        this.updateGlobe();
        this.updateHistoricalContext();
    }

    runSimulation() {
        if (!this.currentPrediction) {
            this.updatePrediction();
        }

        // Show loading state
        const container = document.getElementById('container');
        const resultsDisplay = document.getElementById('results-display');
        
        container.classList.add('loading');

        // Simulate processing time for dramatic effect
        setTimeout(() => {
            container.classList.remove('loading');
            this.showSimulationResults();
        }, 2000);
    }

    showSimulationResults() {
        if (!this.currentPrediction) return;

        const resultsDisplay = document.getElementById('results-display');
        const probabilityValue = document.getElementById('probability-value');
        const powerScoreValue = document.getElementById('power-score-value');
        const outcomeMessage = document.getElementById('outcome-message');
        const factorList = document.getElementById('factor-list');
        const container = document.getElementById('container');

        // Show results display
        if (resultsDisplay) {
            resultsDisplay.classList.remove('hidden');
        }

        // Update probability
        if (probabilityValue) {
            const percentage = Math.round(this.currentPrediction.probability * 100);
            probabilityValue.textContent = `${percentage}%`;
        }

        // Update power score
        if (powerScoreValue) {
            const powerScore = this.currentPrediction.powerScore.toFixed(3);
            powerScoreValue.textContent = powerScore;
        }

        // Determine outcome and set container state
        const isSuccess = this.currentPrediction.probability > 0.5;
        const probability = Math.round(this.currentPrediction.probability * 100);

        if (isSuccess) {
            container.className = 'success-state';
            if (outcomeMessage) {
                if (probability > 75) {
                    outcomeMessage.textContent = "CIVILIZATION ASCENDANT - Optimal conditions for expansion detected";
                } else {
                    outcomeMessage.textContent = "CIVILIZATION RISING - Growth trajectory confirmed";
                }
            }
        } else {
            container.className = 'failure-state';
            if (outcomeMessage) {
                if (probability < 25) {
                    outcomeMessage.textContent = "CIVILIZATION AT RISK - Critical structural weaknesses identified";
                } else {
                    outcomeMessage.textContent = "CIVILIZATION CHALLENGED - Significant obstacles detected";
                }
            }
        }

        // Update factor analysis
        if (factorList && this.currentPrediction.factors) {
            factorList.innerHTML = '';
            
            this.currentPrediction.factors.forEach(factor => {
                const factorDiv = document.createElement('div');
                factorDiv.className = 'terminal-line';
                
                const factorText = document.createElement('span');
                factorText.className = 'param-description';
                
                const impact = factor.impact === 'positive' ? '+' : '-';
                const strength = Math.abs(factor.coefficient).toFixed(3);
                
                factorText.textContent = `  ${factor.name.toLowerCase().replace(/\s+/g, '_')}: ${impact}${strength} (${factor.description})`;
                
                if (factor.impact === 'positive') {
                    factorText.classList.add('factor-positive');
                } else {
                    factorText.classList.add('factor-negative');
                }
                
                factorDiv.appendChild(factorText);
                factorList.appendChild(factorDiv);
            });
        }

        // Trigger globe animation
        if (this.globe) {
            if (isSuccess) {
                this.globe.triggerVictoryAnimation();
            } else {
                this.globe.triggerDefeatAnimation();
            }
        }
    }

    updateGlobe() {
        if (this.globe && this.currentPrediction) {
            this.globe.updateGlobeAppearance(this.currentPrediction.probability);
        }
    }

    updateHistoricalContext() {
        if (!this.currentPrediction) return;

        const contextText = document.getElementById('context-text');
        if (contextText) {
            const context = this.model.generateHistoricalContext(
                this.currentInputs, 
                this.currentPrediction
            );
            contextText.textContent = context;
        }
    }

    makePrediction() {
        if (!this.currentPrediction) {
            this.updatePrediction();
        }

        // Show loading state
        const container = document.getElementById('container');
        container.classList.add('loading');

        // Simulate processing time for dramatic effect
        setTimeout(() => {
            container.classList.remove('loading');
            this.showResults();
        }, 1500);
    }

    showResults() {
        if (!this.currentPrediction) return;

        const modal = document.getElementById('results-modal');
        const victoryTitle = document.getElementById('victory-title');
        const victoryAnimation = document.getElementById('victory-animation');
        const victoryMessage = document.getElementById('victory-message');
        const factorList = document.getElementById('factor-list');

        // Determine outcome
        const isVictory = this.currentPrediction.probability > 0.5;
        const probability = Math.round(this.currentPrediction.probability * 100);

        // Update title and animation
        if (victoryTitle) {
            victoryTitle.textContent = isVictory ? 
                "Your Civilization Rises!" : 
                "Your Civilization Struggles";
        }

        if (victoryAnimation) {
            victoryAnimation.textContent = isVictory ? "🏆" : "⚔️";
        }

        // Update message
        if (victoryMessage) {
            if (isVictory) {
                if (probability > 80) {
                    victoryMessage.textContent = `With a ${probability}% chance of success, your civilization is destined for greatness! The combination of your strategic choices creates optimal conditions for rapid growth and expansion.`;
                } else {
                    victoryMessage.textContent = `Your civilization has a ${probability}% chance of increasing its advantage. While success is likely, careful management of your resources will be crucial.`;
                }
            } else {
                if (probability < 20) {
                    victoryMessage.textContent = `With only a ${probability}% chance of success, your civilization faces severe challenges. Fundamental changes to your approach may be necessary to avoid decline.`;
                } else {
                    victoryMessage.textContent = `Your civilization has a ${probability}% chance of growth. The current path presents significant obstacles that must be overcome.`;
                }
            }
        }

        // Update factor analysis
        if (factorList && this.currentPrediction.factors) {
            factorList.innerHTML = '';
            
            this.currentPrediction.factors.forEach(factor => {
                const li = document.createElement('li');
                
                const factorName = document.createElement('span');
                factorName.textContent = factor.name;
                
                const factorImpact = document.createElement('span');
                factorImpact.className = `factor-impact ${factor.impact}-impact`;
                factorImpact.textContent = factor.impact === 'positive' ? 'Helps' : 'Hinders';
                
                li.appendChild(factorName);
                li.appendChild(factorImpact);
                li.title = factor.description;
                
                factorList.appendChild(li);
            });
        }

        // Trigger globe animation
        if (this.globe) {
            if (isVictory) {
                this.globe.triggerVictoryAnimation();
            } else {
                this.globe.triggerDefeatAnimation();
            }
        }

        // Show modal
        this.showModal('results-modal');
    }

    resetParameters() {
        // Reset all sliders to 0
        const sliders = [
            { id: 'military-slider', valueId: 'military-value', key: 'military' },
            { id: 'education-slider', valueId: 'education-value', key: 'education' },
            { id: 'volatility-slider', valueId: 'volatility-value', key: 'volatility' },
            { id: 'exchange-slider', valueId: 'exchange-value', key: 'exchange' }
        ];

        sliders.forEach(slider => {
            const element = document.getElementById(slider.id);
            const valueDisplay = document.getElementById(slider.valueId);
            
            if (element && valueDisplay) {
                element.value = 0;
                valueDisplay.textContent = '0.0';
                this.currentInputs[slider.key] = 0;
            }
        });

        // Hide results display
        const resultsDisplay = document.getElementById('results-display');
        if (resultsDisplay) {
            resultsDisplay.classList.add('hidden');
        }

        // Reset container state
        const container = document.getElementById('container');
        container.className = '';

        // Update prediction
        this.updatePrediction();
    }

    showModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        }
    }

    closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }

    // Public methods for external interaction
    setParameter(parameter, value) {
        if (parameter in this.currentInputs) {
            this.currentInputs[parameter] = Math.max(-1, Math.min(1, value));
            
            // Update slider and display
            const sliderId = `${parameter}-slider`;
            const valueId = `${parameter}-value`;
            
            const slider = document.getElementById(sliderId);
            const valueDisplay = document.getElementById(valueId);
            
            if (slider) slider.value = this.currentInputs[parameter];
            if (valueDisplay) valueDisplay.textContent = this.currentInputs[parameter].toFixed(1);
            
            this.updatePrediction();
        }
    }

    getModelInfo() {
        return this.model.getModelInfo();
    }

    getCurrentPrediction() {
        return this.currentPrediction;
    }

    // Cleanup method
    destroy() {
        if (this.globe) {
            this.globe.destroy();
        }
    }
}

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', () => {
    // Check if Three.js is loaded
    if (typeof THREE === 'undefined') {
        console.error('Three.js not loaded! Please check your internet connection.');
        return;
    }

    // Initialize the game
    window.greatGame = new GreatGame();
    
    // Add some helpful console commands for debugging
    console.log('The Great Game is ready!');
    console.log('Try: greatGame.setParameter("military", 0.8)');
    console.log('Or: greatGame.getModelInfo()');
});

// Handle page unload
window.addEventListener('beforeunload', () => {
    if (window.greatGame) {
        window.greatGame.destroy();
    }
});
