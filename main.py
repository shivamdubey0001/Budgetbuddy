# budgetbuddy/main.py
import os
import json
from datetime import datetime
from tracker import add_income, add_expense, calculate_summary
from utils import clear_screen, display_header, print_colored, format_currency

# File path to store budget data
DATA_FILE = "data/budget_log.json"

def load_data():
    """Load existing data from JSON file. If file doesn't exist, return empty data."""
    try:
        # Ensure data directory exists
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        
        if not os.path.exists(DATA_FILE):
            # Create empty file with default structure
            default_data = {"income": [], "expenses": []}
            with open(DATA_FILE, "w") as file:
                json.dump(default_data, file, indent=2)
            return default_data

        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            # Validate data structure
            if not isinstance(data, dict) or "income" not in data or "expenses" not in data:
                print_colored("⚠️ Invalid data format, creating new file...", "yellow")
                return {"income": [], "expenses": []}
            return data
    except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
        print_colored(f"⚠️ Error loading data: {e}", "red")
        print_colored("Creating new data file...", "yellow")
        return {"income": [], "expenses": []}

def save_data(data):
    """Save data to JSON file. Creates folder if missing."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print_colored(f"⚠️ Failed to save data: {e}", "red")

def show_summary(data):
    """Display total income, expenses, and balance."""
    summary = calculate_summary(data)
    print_colored("\n📊 MONTHLY SUMMARY", "blue")
    print(f"💰 Total Income: {format_currency(summary['total_income'])}")
    print(f"💸 Total Expenses: {format_currency(summary['total_expenses'])}")
    print(f"🤑 Balance Remaining: {format_currency(summary['balance'])}")

    # Smart tip (example)
    if summary["balance"] < 1000:
        print_colored("💡 Tip: Your balance is low! Cut unnecessary expenses.", "yellow")

def main_menu():
    """Display main menu and handle user choice."""
    data = load_data()

    while True:
        clear_screen()
        display_header("💼 BudgetBuddy – Your Personal Finance Tracker")

        print("\nWhat would you like to do?")
        print("1. ➕ Add Income")
        print("2. ➖ Add Expense")
        print("3. 📊 View Summary")
        print("4. 💱 Change Currency")
        print("5. 💾 Save & Exit")

        choice = input("\n👉 Enter your choice (1-5): ").strip()

        if choice == "1":
            from utils import CURRENT_CURRENCY
            try:
                amount_input = input(f"Enter income amount ({CURRENT_CURRENCY['name']}): {CURRENT_CURRENCY['symbol']}")
                amount_input = amount_input.strip()
                
                if not amount_input:
                    print_colored("❌ Amount cannot be empty!", "red")
                    input("Press Enter to continue...")
                    continue
                    
                amount = float(amount_input)
                if amount <= 0:
                    print_colored("❌ Amount must be greater than 0!", "red")
                    input("Press Enter to continue...")
                    continue
                    
                source = input("Income source (e.g., Salary, Freelance): ").strip()
                if not source:
                    print_colored("❌ Income source cannot be empty!", "red")
                    input("Press Enter to continue...")
                    continue
                    
                add_income(data, amount, source)
                print_colored("✅ Income added!", "green")
                save_data(data)  # Auto-save after adding
                
            except (ValueError, TypeError) as e:
                print_colored(f"❌ Invalid amount! Please enter a valid number. Error: {e}", "red")
                input("Press Enter to continue...")
                continue
            except Exception as e:
                print_colored(f"❌ Unexpected error: {e}", "red")
                input("Press Enter to continue...")
                continue

        elif choice == "2":
            from utils import CURRENT_CURRENCY
            try:
                amount_input = input(f"Enter expense amount ({CURRENT_CURRENCY['name']}): {CURRENT_CURRENCY['symbol']}")
                amount_input = amount_input.strip()
                
                if not amount_input:
                    print_colored("❌ Amount cannot be empty!", "red")
                    input("Press Enter to continue...")
                    continue
                    
                amount = float(amount_input)
                if amount <= 0:
                    print_colored("❌ Amount must be greater than 0!", "red")
                    input("Press Enter to continue...")
                    continue
                    
                category = input("Category (e.g., Food, Travel): ").strip()
                if not category:
                    print_colored("❌ Category cannot be empty!", "red")
                    input("Press Enter to continue...")
                    continue
                    
                note = input("Note (optional): ").strip()
                add_expense(data, amount, category, note)
                print_colored("✅ Expense added!", "green")
                save_data(data)  # Auto-save after adding
                
            except (ValueError, TypeError) as e:
                print_colored(f"❌ Invalid amount! Please enter a valid number. Error: {e}", "red")
                input("Press Enter to continue...")
                continue
            except Exception as e:
                print_colored(f"❌ Unexpected error: {e}", "red")
                input("Press Enter to continue...")
                continue

        elif choice == "3":
            show_summary(data)
            input("\nPress Enter to continue...")

        elif choice == "4":
            from utils import select_currency
            select_currency()
            input("\nPress Enter to continue...")

        elif choice == "5":
            save_data(data)
            print_colored("💾 Data saved. Exiting...", "blue")
            break

        else:
            print_colored("❌ Invalid choice! Please select 1-5.", "red")
            input("Press Enter to retry...")

if __name__ == "__main__":
    main_menu()