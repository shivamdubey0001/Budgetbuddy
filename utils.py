# budgetbuddy/utils.py
import os
from datetime import datetime

# Available currencies for different countries
CURRENCIES = {
    "1": {"symbol": "₹", "name": "Indian Rupee (INR)"},
    "2": {"symbol": "$", "name": "US Dollar (USD)"},
    "3": {"symbol": "€", "name": "Euro (EUR)"},
    "4": {"symbol": "£", "name": "British Pound (GBP)"},
    "5": {"symbol": "¥", "name": "Japanese Yen (JPY)"},
    "6": {"symbol": "C$", "name": "Canadian Dollar (CAD)"},
    "7": {"symbol": "A$", "name": "Australian Dollar (AUD)"},
    "8": {"symbol": "₽", "name": "Russian Ruble (RUB)"},
    "9": {"symbol": "¥", "name": "Chinese Yuan (CNY)"},
    "10": {"symbol": "₩", "name": "South Korean Won (KRW)"}
}

# Default currency (can be changed by user)
CURRENT_CURRENCY = {"symbol": "₹", "name": "Indian Rupee (INR)"}

# Text styles and colors
STYLES = {
    # Colors
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    # Text Decorations
    "bold": "\033[1m",
    "underline": "\033[4m",
    "reset": "\033[0m"
}

def clear_screen():
    """Clear terminal screen (works for both Windows & Mac/Linux)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_styled(text, style=None):
    """
    Print text with style (color/bold/underline).
    Examples:
        print_styled("Warning!", "bold red")
        print_styled("Underlined", "underline blue")
    """
    if not style:
        print(text)
        return

    style_codes = []
    for s in style.split():
        if s in STYLES:
            style_codes.append(STYLES[s])

    if style_codes:
        styled_text = "".join(style_codes) + text + STYLES["reset"]
        print(styled_text)
    else:
        print(text)

def display_header(title):
    """Display a styled header with double border"""
    border = "═" * (len(title) + 2)  # Fancy double-line border
    print_styled(f"\n ║{title}║", "bold purple")
    print_styled(f" ╚{border}╝", "purple")

def get_current_date():
    """Return current date in YYYY-MM-DD format"""
    return datetime.now().strftime("%Y-%m-%d")

def format_currency(amount):
    """Format number as currency using selected currency symbol"""
    return f"{STYLES['bold']}{CURRENT_CURRENCY['symbol']}{round(amount, 2)}{STYLES['reset']}"

def select_currency():
    """Let user choose their preferred currency"""
    try:
        print_colored("\n💱 SELECT YOUR CURRENCY", "blue")
        print("Choose your preferred currency:")
        
        # Show all available currencies
        for key, currency in CURRENCIES.items():
            print(f"{key}. {currency['symbol']} - {currency['name']}")
        
        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            choice = input("\n👉 Enter currency number (1-10): ").strip()
            
            if not choice:
                print_colored("❌ Please enter a number!", "red")
                attempts += 1
                continue
                
            if choice in CURRENCIES:
                # Update global currency setting
                global CURRENT_CURRENCY
                CURRENT_CURRENCY = CURRENCIES[choice].copy()
                print_colored(f"✅ Currency changed to: {CURRENT_CURRENCY['symbol']} {CURRENT_CURRENCY['name']}", "green")
                return
            else:
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print_colored(f"❌ Invalid choice! Please select 1-10. ({remaining} attempts remaining)", "red")
                else:
                    print_colored("❌ Too many invalid attempts. Keeping current currency.", "red")
                    return
                    
    except KeyboardInterrupt:
        print_colored("\n❌ Currency selection cancelled.", "yellow")
        return
    except Exception as e:
        print_colored(f"❌ Error in currency selection: {e}", "red")
        return

def print_colored(text, color):
    """Print text with color"""
    if color in STYLES:
        print(f"{STYLES[color]}{text}{STYLES['reset']}")
    else:
        print(text)