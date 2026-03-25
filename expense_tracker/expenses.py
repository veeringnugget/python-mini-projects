"""
TODO:
3. Add Expenses - add input of type, cost, description - write to csv file
4. View Expenses will open CSV and show contents
5. View Summary will summarise expenses / amount of rows / totals
6. Exit will close app
"""
import csv

# Main Code
def main():
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
        exit

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
    pass

# Allows user to view all expenses added
def view_expenses():
    pass

# Allows user to see summary of what has been added (counts, totals)
def view_summary():
    pass

# Allows user to delete previously added expense
def delete_expenses():
    pass

if __name__ == "__main__":
    main()
