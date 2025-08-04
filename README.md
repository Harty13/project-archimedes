# Project Archimedes

**TrueWealth Hackathon 2025**

## Project Structure

```
Project Archimedes/
├── main.py              # Main entry point
├── services/            # Business logic and services
├── data/               # Data models and utilities
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore patterns
└── README.md          # This file
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Development

The project is structured to support full cross-module imports:
```python
from data.example import ExampleData
from services.example import ExampleService
```

## Contributing

This project was created for the TrueWealth Hackathon 2025.