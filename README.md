# 💼 BudgetBuddy - Personal Finance Tracker

Hey there! 👋 This is **BudgetBuddy**, a simple command-line tool I built to help you manage your personal finances without any complicated apps or websites.

**Created by: Shivam Dubey** 🚀

## 🎯 What is BudgetBuddy?

Think of BudgetBuddy as your digital notebook where you can track your money. It's perfect for:

- 🎓 College students managing pocket money
- 💼 Working professionals tracking monthly expenses  
- 🤔 Anyone who wants to understand where their money goes
- 🔒 People who prefer simple tools over fancy apps

## 💡 Why I Built This

I was tired of using complex budgeting apps that required internet, had ads, or cost money. So I created something simple that works offline and keeps your financial data private on your own computer.

## ✨ What Can You Do With It?

**💰 Track Your Income**
- Add your salary, freelance earnings, or any money you receive
- Categorize different income sources

**💸 Record Your Expenses** 
- Log your daily spending on food, travel, shopping, etc.
- Add notes to remember what you bought

**📊 See Your Financial Summary**
- View total income vs expenses
- Check how much money you have left
- Get smart tips about your spending habits

**💱 Multiple Currency Support**
- Use Indian Rupees, US Dollars, Euros, or British Pounds
- Easy to switch between currencies

## 🚀 How to Use It

### 📥 Installation

1. Make sure you have Python installed on your computer 🐍
2. Download or clone this project 📁
3. Open terminal/command prompt in the project folder 💻
4. Run: `python main.py` ⚡

That's it! No pip installs, no dependencies, just pure Python. ✅

### 🎮 First Time Setup

When you run the program, you'll see a simple menu:

```
💼 BudgetBuddy – Your Personal Finance Tracker

What would you like to do?
1. ➕ Add Income
2. ➖ Add Expense  
3. 📊 View Summary
4. 💱 Change Currency
5. 💾 Save & Exit

👉 Enter your choice (1-5):
```

### ➕ Adding Income

Choose option 1 and enter:
- Amount (like 5000) 💵
- Source (like "Salary" or "Freelance work") 💼

### ➖ Adding Expenses

Choose option 2 and enter:
- Amount (like 250) 💸
- Category (like "Food" or "Travel") 🍔
- Optional note (like "Pizza with friends") 📝

### 📊 Viewing Summary

Choose option 3 to see:
- 💰 Total money you've earned
- 💸 Total money you've spent
- 🤑 How much you have left
- 💡 Smart tips about your spending

## 📁 Project Structure

Here's how the code is organized:

```
budgetbuddy/
├── main.py           🧠 Main program with menu and user input
├── tracker.py        📊 Handles income/expense calculations
├── utils.py          🧰 Helper functions for colors and formatting
├── data/             📁 Your personal data folder
│   └── budget_log.json   📝 All your financial data stored here
└── README.md         📖 This file you're reading
```

**🧠 main.py** - This is the heart of the program. It shows you the menu, takes your input, and handles any errors gracefully.

**📊 tracker.py** - This file does all the math. It adds your income, records expenses, and calculates your balance.

**🧰 utils.py** - This makes the program look nice with colors and proper formatting. It also handles different currencies.

**📝 budget_log.json** - This is where your data is saved. It's created automatically when you first use the program.

## 💾 Your Data

All your financial information is stored in a simple JSON file that looks like this:

```json
{
  "income": [
    {
      "amount": 5000,
      "source": "Freelance Work",
      "date": "2025-07-28T10:30:00"
    }
  ],
  "expenses": [
    {
      "amount": 250,
      "category": "Food",
      "note": "Lunch with friends",
      "date": "2025-07-28T12:45:00"
    }
  ]
}
```

This means you can easily backup your data, or even open it in any text editor to see your financial history. 📋

## 🛡️ Error Handling

I've made sure the program doesn't crash even if you make mistakes:

- ❌ Enter wrong amount? It will ask you to try again
- ⚠️ Leave a field empty? It will remind you to fill it
- 🔧 File gets corrupted? It will create a new one
- 💾 Close the program accidentally? Your data is auto-saved

## 💡 Smart Tips

Based on your spending patterns, BudgetBuddy gives you helpful advice:

- 🚨 "Your balance is low! Try to cut unnecessary expenses."
- 🎉 "Great job! You're saving well this month."
- 🍳 "You might be spending too much on food. Consider cooking at home."

## 🔮 Features I'm Planning to Add

- 📈 Monthly and weekly reports
- 🎯 Budget goals and savings targets
- 📄 Export data to Excel or PDF
- 🔍 Search through your transaction history
- 📊 Category-wise spending limits
- 🔄 Recurring income and expense tracking

## ❓ Common Questions

**🔐 Q: Is my financial data safe?**
A: Yes! Everything is stored on your computer. No data is sent anywhere online.

**💻 Q: Can I use this on different computers?**
A: Yes, just copy the entire folder to another computer with Python installed.

**🗑️ Q: What if I want to reset all my data?**
A: Just delete the `budget_log.json` file and restart the program.

**💱 Q: Can I change the currency after adding data?**
A: Yes, but existing amounts won't be converted. The currency setting only affects new entries.

## 🤝 Contributing

Found a bug or have an idea for improvement? I'd love to hear from you! This project is open for contributions and suggestions. 🎉

Some areas where you can help:
- ✨ Add new features
- 🎨 Improve the user interface
- 🐛 Fix bugs or improve error handling
- 💱 Add support for more currencies
- 📚 Create better documentation

## 🔧 Technical Details

- **🐍 Language**: Python 3.x
- **📦 Dependencies**: None (uses only built-in Python libraries)
- **💾 Data Storage**: JSON files
- **🖥️ Platform**: Works on Windows, Mac, and Linux
- **⌨️ Interface**: Command-line interface (CLI)

## 💻 Why Command Line?

I chose to make this a command-line tool because:
- ⚡ It's fast and lightweight
- 🌐 Works on any computer with Python
- 🔌 No need for internet connection
- 🔒 Your data stays completely private
- 💾 Easy to backup and share
- 🔄 Works the same way on all operating systems

## 📄 License

This project is free to use for personal and educational purposes. Feel free to modify it according to your needs, share it with friends, or use it to learn Python programming. 🆓

## 🎯 Final Thoughts

Managing money doesn't have to be complicated. BudgetBuddy keeps it simple - just track what comes in, what goes out, and make better decisions based on real data. 📈

The most important thing is to start tracking your finances, even if it's just for a week. You'll be surprised by what you discover about your spending habits! 😮

Start small, be consistent, and watch your financial awareness grow. 🌱

**Happy budgeting!** 💰✨

---

**Made with ❤️ by Shivam Dubey**
