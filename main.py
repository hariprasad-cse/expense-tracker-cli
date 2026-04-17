# Expense Tracker CLI - Made by Hari Prasad
# Python Developer Internship Project

import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ₹")
    category = input("Enter category (Food/Travel/Bills/Other): ")
    note = input("Enter note: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    print("✅ Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found yet.")
        return

    total = 0
    print("\n--- All Expenses ---")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]} | ₹{row[1]} | {row[2]} | {row[3]}")
            total += float(row[1])
    print(f"\nTotal Spent: ₹{total}")

def main():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Note"])

    while True:
        print("\n=== Expense Tracker CLI ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Enter choice 1/2/3: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Thank you. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
