"""
TODO:
1. List options for user to select for expenses
2. Create function for each option selected
3. Add Expenses - add input of type, cost, description - write to csv file
4. View Expenses will open CSV and show contents
5. View Summary will summarise expenses / amount of rows / totals
6. Exit will close app
"""

def show_menu():
    return input("1. Add Expenses\n2. View Expenses\n3. View Summary\n" \
    "4. Delete Expense\n5. Exit\n> ")

show_menu()
