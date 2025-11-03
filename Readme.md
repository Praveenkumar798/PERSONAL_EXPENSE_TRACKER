# Personal Expense Tracker

A simple, intuitive expense tracking application built with Streamlit. Track daily expenses, categorize spending, and visualize your financial patterns with interactive charts.

## Features

- 📝 Add daily expenses with categories
- 💰 Track spending amounts and notes
- 📊 Visualize expenses by category
- 📋 View all transactions in a sortable table
- 💾 Automatic CSV-based data storage

## Setup

1. Clone or download this repository
2. Create and activate a virtual environment:

```powershell
# Create virtual environment
python -m venv .venv

# Activate (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Install required packages:

```powershell
pip install -r requirements.txt
```

## Running the App

Start the Streamlit app:

```powershell
streamlit run app.py
```

The app will open in your default web browser at http://localhost:8501

## Usage

1. **Add New Expense**
   - Select a date
   - Choose a category (Food, Travel, Shopping, etc.)
   - Enter the amount
   - Add an optional note
   - Click "Add Expense"

2. **View Expenses**
   - All expenses are shown in the table below the form
   - The chart shows total spending by category
   - Data is automatically saved to `data/expenses.csv`

## Data Storage

Your expenses are stored in `data/expenses.csv` with the following structure:
- Date: Date of expense
- Category: Expense category
- Amount: Cost in your currency
- Note: Optional description

## Dependencies

- streamlit
- pandas
- matplotlib

## File Structure

```
PERSONAL_EXPENSE_TRACKER/
├── app.py              # Main Streamlit application
├── utils.py            # Helper functions
├── requirements.txt    # Python dependencies
└── data/
    └── expenses.csv    # Expense data storage
```
