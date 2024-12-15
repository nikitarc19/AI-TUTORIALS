# Python Virtual Environment Setup Guide

## Creating a Virtual Environment

1. Open your terminal or command prompt
2. Navigate to your project directory
3. Create a virtual environment using:
```bash
python -m venv .env
```

## Activating the Virtual Environment

### Windows
```bash
.env\Scripts\activate
```

### Linux/macOS
```bash
source .env/bin/activate
```

## Deactivating the Virtual Environment
```bash
deactivate
```

## Common Commands
- `pip list` - View installed packages
- `pip freeze > requirements.txt` - Save dependencies
- `pip install -r requirements.txt` - Install dependencies

## Notes
- Keep `.env` in your `.gitignore` file
- Always activate the virtual environment before installing packages
- Use `requirements.txt` to share project dependencies
