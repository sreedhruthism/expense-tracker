import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.json"
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        """Save expenses to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, amount, description, category):
        """Add a new expense to the tracker."""
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "description": description,
            "category": category
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        for expense in self.expenses:
            print(f"Date: {expense['date']}, Amount: ${expense['amount']:.2f}, "
                  f"Description: {expense['description']}, Category: {expense['category']}")

    def monthly_summary(self):
        """Display monthly summary of expenses."""
        monthly_totals = {}
        for expense in self.expenses:
            month = expense['date'][:7]  # Extract YYYY-MM
            monthly_totals[month] = monthly_totals.get(month, 0) + expense['amount']
        
        for month, total in monthly_totals.items():
            print(f"Month: {month}, Total: ${total:.2f}")

    def category_summary(self):
        """Display category-wise summary of expenses."""
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            category_totals[category] = category_totals.get(category, 0) + expense['amount']
        
        for category, total in category_totals.items():
            print(f"Category: {category}, Total: ${total:.2f}")

def get_float_input(prompt):
    """Get a float input from the user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = get_float_input("Enter expense amount: $")
            description = input("Enter expense description: ")
            category = input("Enter expense category: ")
            tracker.add_expense(amount, description, category)
            print("Expense added successfully!")

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.monthly_summary()

        elif choice == '4':
            tracker.category_summary()

        elif choice == '5':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    print("Sree Dhruthi from Jain University")