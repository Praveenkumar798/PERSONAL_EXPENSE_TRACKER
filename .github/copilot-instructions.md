## Copilot / Agent Instructions — PERSONAL EXPENSE TRACKER

Repository state (discovered):
- Python-based expense tracker with main components:
  - `app.py`: Main application file
  - `utils.py`: Utility functions
  - `data/expenses.csv`: Data storage
  - `requirements.txt`: Python dependencies

Architecture & Data Flow:
- File-based CSV storage in `data/expenses.csv`
- Main application logic in `app.py`
- Helper functions and utilities in `utils.py`

Developer Workflow:
1. Setup:
```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

2. Running the application:
```powershell
python app.py
```

Conventions & Patterns:
- Data storage: CSV-based persistence in `data/expenses.csv`
- File organization: Flat structure with clear separation between app logic and utilities
- Dependencies: Listed in `requirements.txt`

Integration Points:
- Local file system: Reading/writing to `data/expenses.csv`
- No external service dependencies identified

Guidelines for Changes:
1. Data Handling:
   - Always use CSV operations from `utils.py` for consistency
   - Maintain the data schema in `expenses.csv`

2. Adding Features:
   - Place utility functions in `utils.py`
   - Core application logic goes in `app.py`
   - Update `requirements.txt` if adding new dependencies

3. Testing Changes:
   - Verify data persistence by checking `data/expenses.csv`
   - Test both add and view operations
   - Ensure error handling for invalid inputs

Notes & Guardrails:
- Preserve the CSV data format for compatibility
- Maintain the simple file-based architecture unless explicitly requested
- Keep the flat project structure for simplicity

Follow-up:
- After making changes, verify that:
  1. CSV operations work correctly
  2. All features are accessible through the main interface
  3. Data persists between application restarts