import json
from datetime import datetime
import os

FILE_NAME = "expenses.json"


# Load expenses from JSON file
def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


# Save expenses to JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    print("\n--- Add Expense ---")

    title = input("Enter expense name: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    date = datetime.now().strftime("%d-%m-%Y")

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# View all expenses
def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['date']}"
        )


# Calculate total expenses
def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total spent: ₹{total:.2f}")


# Search expenses by category
def search_category(expenses):
    category = input("\nEnter category to search: ").lower()

    found = False

    print(f"\n--- Expenses in {category.title()} ---")

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"{expense['title']} | "
                f"₹{expense['amount']:.2f} | "
                f"{expense['date']}"
            )
            found = True

    if not found:
        print("No expenses found in this category.")


# Category-wise summary
def category_summary(expenses):
    print("\n--- Category-wise Summary ---")

    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


# Delete an expense
def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses(expenses)

            print(f"Deleted: {deleted['title']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    expenses = load_expenses()

    while True:
        print("\n================================")
        print("      PERSONAL EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total Expenses")
        print("5. Category-wise Summary")
        print("6. Delete Expense")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_category(expenses)

        elif choice == "4":
            total_expenses(expenses)

        elif choice == "5":
            category_summary(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()