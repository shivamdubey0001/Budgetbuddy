# budgetbuddy/tracker.py
from datetime import datetime
from utils import print_colored, format_currency

def add_income(data, amount, source):
    """Add income entry to the data with current date."""
    try:
        # Validate inputs
        if not isinstance(data, dict) or "income" not in data:
            raise ValueError("Invalid data structure")
            
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
            
        source = str(source).strip()
        if not source:
            raise ValueError("Source cannot be empty")
            
        new_entry = {
            "amount": round(amount, 2),
            "source": source,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        data["income"].append(new_entry)
        print_colored(f"✅ Added income: {format_currency(amount)} from {source}", "green")
        
    except (ValueError, TypeError) as e:
        print_colored(f"❌ Error adding income: {e}", "red")
        raise

def add_expense(data, amount, category, note=""):
    """Add expense entry to the data with current date."""
    try:
        # Validate inputs
        if not isinstance(data, dict) or "expenses" not in data:
            raise ValueError("Invalid data structure")
            
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
            
        category = str(category).strip()
        if not category:
            raise ValueError("Category cannot be empty")
            
        note = str(note).strip() if note else ""
        
        new_entry = {
            "amount": round(amount, 2),
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        data["expenses"].append(new_entry)
        print_colored(f"✅ Added expense: {format_currency(amount)} for {category}", "green")
        
    except (ValueError, TypeError) as e:
        print_colored(f"❌ Error adding expense: {e}", "red")
        raise

def calculate_summary(data):
    """Calculate total income, expenses, and balance."""
    total_income = sum(entry["amount"] for entry in data.get("income", []))
    total_expenses = sum(entry["amount"] for entry in data.get("expenses", []))

    return {
        "total_income": round(total_income, 2),
        "total_expenses": round(total_expenses, 2),
        "balance": round(total_income - total_expenses, 2)
    }