# 💼 BudgetBuddy – Personal Finance & Savings CLI Planner

> *"Apne monthly income, expenses aur savings ko samjho, track karo aur better decisions lo – bina kisi app ke."*

**Created by: Shivam Dubey**

---

## 🎯 What is BudgetBuddy?

BudgetBuddy is a simple command-line tool that helps you manage your personal finances. Think of it as your digital notebook where you can:

- **Track your income** (salary, freelance, pocket money)
- **Record your expenses** (food, travel, shopping, bills)
- **See where your money goes** with smart summaries
- **Get helpful tips** when you're overspending

Perfect for college students, working professionals, or anyone who wants to understand their spending habits without using complex apps or websites.

## 🚀 Why Use BudgetBuddy?

### Real-Life Scenarios:
- **College Student**: "Main monthly 5000 rupees pocket money mein se kitna save kar sakta hun?"
- **Working Professional**: "Is month food pe kitna zyada kharcha ho gaya?"
- **Family Member**: "Ghar ke monthly expenses track karne ke liye"
- **Freelancer**: "Multiple income sources aur irregular expenses manage karne ke liye"

### Key Benefits:
- ✅ **No Internet Required** - Works completely offline
- ✅ **Simple Interface** - No complicated menus or settings
- ✅ **Data Privacy** - Your financial data stays on your computer
- ✅ **Smart Tips** - Get suggestions to improve your spending
- ✅ **Multiple Currency Support** - Use your preferred currency

---

## 📁 Project Structure

```
budgetbuddy/
├── main.py           🧠 Main controller (sab kuch yahin se chalega)
├── tracker.py        📊 Income/expense calculations aur data handling
├── utils.py          🧰 Colors, formatting, screen clearing utilities
├── data/             📁 Your personal finance data folder
│   └── budget_log.json   📝 All your entries stored here
└── README.md         📖 This guide you're reading
```

### What Each File Does:

**🧠 main.py** - The Brain
- Shows you the main menu
- Takes your input (income/expense)
- Handles errors gracefully
- Auto-saves your data

**📊 tracker.py** - The Calculator
- Adds your income entries
- Records your expenses
- Calculates total balance
- Generates monthly summaries

**🧰 utils.py** - The Helper
- Makes text colorful and pretty
- Clears screen for better experience
- Formats currency (₹, $, €, etc.)
- Handles different currencies

**📝 budget_log.json** - The Storage
- Stores all your financial data
- Creates automatically if missing
- Easy to backup or share

---

## 🔧 How to Install & Run

### Step 1: Download the Project
```bash
# Clone or download the project
git clone [your-repo-link]
cd budgetbuddy
```

### Step 2: Make Sure You Have Python
```bash
# Check if Python is installed
python --version
# or
python3 --version
```

### Step 3: Run BudgetBuddy
```bash
python main.py
# or
python3 main.py
```

That's it! No pip install, no dependencies, no complicated setup.

---

## 🎮 How to Use BudgetBuddy

### First Time Launch:
When you run the program for the first time, you'll see:

```
💼 BudgetBuddy – Your Personal Finance Tracker
=========================================================

📅 Today's Date: 28 July 2025

What would you like to do?
1. ➕ Add Income
2. ➖ Add Expense  
3. 📊 View Summary
4. 💱 Change Currency
5. 💾 Save & Exit

👉 Enter your choice (1-5):
```

### Adding Income (Option 1):
```
Enter income amount (Indian Rupee): ₹5000
Income source (e.g., Salary, Freelance): Freelance Work
✅ Income added!
```

### Adding Expense (Option 2):
```
Enter expense amount (Indian Rupee): ₹250
Category (e.g., Food, Travel): Food
Note (optional): Lunch with friends
✅ Expense added!
```

### Viewing Summary (Option 3):
```
📊 MONTHLY SUMMARY
💰 Total Income: ₹5,000.00
💸 Total Expenses: ₹1,250.00
🤑 Balance Remaining: ₹3,750.00

💡 Tip: Great job! You're saving 75% of your income.
```

### Currency Support (Option 4):
Choose from multiple currencies:
- 🇮🇳 Indian Rupee (₹)
- 🇺🇸 US Dollar ($)
- 🇪🇺 Euro (€)
- 🇬🇧 British Pound (£)

---

## 📊 Understanding Your Data

### What Gets Saved?
Your `data/budget_log.json` file will look like this:

```json
{
  "income": [
    {
      "amount": 5000,
      "source": "Freelance Work", 
      "date": "2025-07-28T10:30:00"
    },
    {
      "amount": 2000,
      "source": "Part-time Job",
      "date": "2025-07-25T14:15:00"
    }
  ],
  "expenses": [
    {
      "amount": 250,
      "category": "Food",
      "note": "Lunch with friends",
      "date": "2025-07-28T12:45:00"
    },
    {
      "amount": 100,
      "category": "Travel", 
      "note": "Auto fare to college",
      "date": "2025-07-27T09:20:00"
    }
  ]
}
```

### Smart Tips You'll Get:
- 💡 "Your balance is low! Cut unnecessary expenses."
- 💡 "Great job! You're saving well this month."
- 💡 "Food expenses are high. Try cooking at home."

---

## 🛡️ Error Handling & Safety

BudgetBuddy is designed to be crash-proof:

### What if I enter wrong data?
- **Invalid amount**: "❌ Invalid amount! Please enter a valid number."
- **Empty fields**: "❌ Amount cannot be empty!"
- **Negative numbers**: "❌ Amount must be greater than 0!"

### What if files get corrupted?
- Automatically creates new data file
- Shows warning but doesn't crash
- Your previous data is safe

### What if I accidentally close the program?
- Auto-saves after every entry
- No data loss even if you close unexpectedly

---

## 🎨 Features Breakdown

| Feature | Description | Example |
|---------|-------------|---------|
| **➕ Add Income** | Record money coming in | Salary: ₹25,000 |
| **➖ Add Expense** | Track money going out | Food: ₹500 |
| **📊 View Summary** | See total income, expenses, balance | Balance: ₹24,500 |
| **💱 Multi-Currency** | Use your preferred currency | ₹, $, €, £ |
| **💾 Auto-Save** | Saves data after every entry | No manual saving needed |
| **🎨 Colorful Interface** | Easy-to-read colored text | Green for success, red for errors |
| **📅 Date Tracking** | Automatic date stamps | Knows when you added each entry |
| **💡 Smart Tips** | Helpful financial advice | Based on your spending patterns |

---

## 🔮 Future Enhancements

### Coming Soon:
- 📈 **Monthly Reports**: Detailed breakdown by category
- 🎯 **Budget Goals**: Set savings targets
- 📱 **Export Features**: Save data as PDF or Excel
- 🔍 **Search & Filter**: Find specific transactions
- 📊 **Visual Charts**: Simple graphs of your spending

### Want to Contribute?
This project is open for improvements! Some ideas:
- Add recurring income/expenses
- Create backup and restore features
- Add password protection
- Build category-wise spending limits

---

## 🤝 Support & Contact

**Created with ❤️ by Shivam Dubey**

### Need Help?
- 🐛 **Found a Bug?** Create an issue with details
- 💡 **Feature Request?** Share your ideas
- 🤔 **Questions?** Reach out anytime

### Common Issues & Solutions:

**Q: Program crashes when I enter amount**
A: Make sure you're entering only numbers (like 500, not 500 rupees)

**Q: Can't see my old data**
A: Check if `data/budget_log.json` exists in your folder

**Q: Colors not showing properly**
A: Your terminal might not support colors, but functionality still works

**Q: Want to reset all data**
A: Delete the `data/budget_log.json` file and restart the program

---

## 📝 License & Usage

This project is created for educational and personal use. Feel free to:
- ✅ Use it for your personal finance tracking
- ✅ Modify it according to your needs
- ✅ Share it with friends and family
- ✅ Learn from the code structure

---

## 🙏 Final Words

Money management doesn't have to be complicated. BudgetBuddy keeps it simple - just track what comes in, what goes out, and make better decisions based on real data.

**Remember**: The best budget is the one you actually use. Start small, be consistent, and watch your financial awareness grow!

*Happy Budgeting! 💰*

---