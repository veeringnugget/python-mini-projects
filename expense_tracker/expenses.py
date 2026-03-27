import csv
import os

HEADINGS = ['type', 'cost', 'description']

# Main Code
def main():

    # Check if file exists
    if not os.path.isfile('expenses.csv'):
        with open('expenses.csv', "w", newline="") as new_file:
            csv_reader = csv.DictWriter(new_file, fieldnames=HEADINGS)
            csv_reader.writeheader()

    while True:
    # Obtain portion of expenses user wants to access
        user_choice = show_menu()

        # Call the function dependant on users choice
        if user_choice == 1:
            add_expenses()
        elif user_choice == 2:
            view_expenses()
        elif user_choice == 3:
            view_summary()
        elif user_choice == 4:
            delete_expenses()
        elif user_choice == 5:
            return

# List menu options
def show_menu():
    while True:
        try:
            user_choice = int(input("1. Add Expenses\n2. View Expenses\n" \
            "3. View Summary\n4. Delete Expense\n5. Exit\n> "))
            if user_choice < 1 or user_choice > 5:
                print("Input must be between 1 and 5")
            else:
                return user_choice
        except ValueError:
            print("Enter integer only")
        
# Allows user to add new expense
def add_expenses():
    # Have user input expenses
    type = input("Type of expense: ")
    cost = input("Cost of expense: £")
    desc = input("Description of expense: ")
    # Open and write to the file
    with open('expenses.csv', "a", newline="") as file:
        csv_writer = csv.DictWriter(file, fieldnames=HEADINGS)
        csv_writer.writerow({'type' : type, 
                             'cost' : cost,
                             'description' : desc,})


# Allows user to view all expenses added
def view_expenses():
    with open('expenses.csv', "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(f"Type: {row['type']} - Cost: £{row['cost']} - Description: {row['description']}")

# Allows user to see summary of what has been added (counts, totals)
def view_summary():
    with open('expenses.csv', "r") as file:
        csv_reader = csv.DictReader(file)
        count = 0
        expense_costs = 0
        for row in csv_reader:
            count += 1
            expense_costs += int(row['cost'])
        print(f"Total entires: {count}\nTotal spend: £{expense_costs}")

# Allows user to delete previously added expense
def delete_expenses():
    count = 1
    print("Please enter the number of the row you want to delete: ")
    # Show user all the entires
    with open('expenses.csv', "r") as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)
        for row in data:
            print(f"{count}: {row['type']} - {row['cost']}")
            count += 1
    delete = int(input("Which row do you want to remove?: ")) - 1
    # Create new data without the row
    new_data = [row for index, row in enumerate(data) if index != delete]
    # Rewrite updated content
    with open('expenses.csv', "w", newline="") as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=HEADINGS)
        csv_writer.writeheader()
        csv_writer.writerows(new_data)
    


if __name__ == "__main__":
    main()
