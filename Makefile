# Makefile for Project Archimedes
# TrueWealth Hackathon 2025

.PHONY: help install run test clean lint format setup dev

# Default target
help:
	@echo "Project Archimedes - Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make run        - Run the main application"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linting"
	@echo "  make format     - Format code"
	@echo "  make clean      - Clean up cache files"
	@echo "  make setup      - Initial project setup"
	@echo "  make dev        - Setup development environment"

# Install dependencies
install:
	pip install -r requirements.txt

# Run the main application
run:
	python main.py


# Clean up cache and temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

# Initial project setup
setup: install
	@echo "Project Archimedes setup complete!"

# Development environment setup
dev: setup
	@echo "Development environment ready!"
	@echo "Run 'make run' to start the application"