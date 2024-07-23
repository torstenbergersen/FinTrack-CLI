import re
import datetime

transactions = []
transaction_id_counter = 1

def valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_transaction():
    global transaction_id_counter
    print("\n=====================================================")
    print("                  ADD TRANSACTION                     ")
    print("=====================================================")
    print("Please enter the following details for the new \ntransaction (or type 'cancel' to return to menu):")
    
    # Date validation
    while True:
        date = input("Date (YYYY-MM-DD): ").strip()
        if date.lower() == 'cancel':
            print("Operation cancelled. Returning to main menu...")
            return
        if valid_date(date):
            break
        else:
            print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")

    # Amount validation
    while True:
        amount = input("Amount: ").strip()
        if amount.lower() == 'cancel':
            print("Operation cancelled. Returning to main menu...")
            return
        if re.match(r'^\d+(\.\d{1,2})?$', amount):
            break
        else:
            print("Invalid amount. Please use only digits.")

    # Category validation
    while True:
        category = input("Category (e.g., Groceries, Utilities): ").strip()
        if category.lower() == 'cancel':
            print("Operation cancelled. Returning to main menu...")
            return
        if category.strip():
            break
        else:
            print("Invalid category. Please enter a non-empty string.")

    transaction = {
        "id": transaction_id_counter,
        "date": date,
        "amount": float(amount),  # store as numeric for easier comparison
        "category": category,
    }
    transactions.append(transaction)
    transaction_id_counter += 1
    print("=====================================================")
    print("Transaction added successfully!")
    print("=====================================================")
    print("Returning to Main Menu...")
    print("=====================================================\n")

def view_transactions():
    print("\n=====================================================")
    print("                 VIEW TRANSACTIONS                    ")
    print("=====================================================")
    print("Filter by:")
    print("[1] Date")
    print("[2] Category")
    print("[3] Amount")
    print("[4] No Filter - View All")
    print("=====================================================")
    filter_choice = input("Select an option by entering a number: ")
    filter_options = {
        '1': 'date',
        '2': 'category',
        '3': 'amount',
        '4': 'none'
    }

    filter_type = filter_options.get(filter_choice, 'none')

    if filter_type == 'none':
        for transaction in transactions:
            print("-----------------------------------------------------")
            print(f"ID: {transaction['id']}, Date: {transaction['date']}, Amount: ${transaction['amount']:.2f}, Category: {transaction['category']}")
    else:
        filter_value = input(f"Enter the {filter_type}: ").strip().lower()
        found = False
        for transaction in transactions:
            if filter_type == 'amount':
                if abs(transaction[filter_type] - float(filter_value)) < 0.01:  # Example of numeric comparison for amount
                    found = True
                    print("-----------------------------------------------------")
                    print(f"ID: {transaction['id']}, Date: {transaction['date']}, Amount: ${transaction['amount']:.2f}, Category: {transaction['category']}")
            else:
                if filter_value in transaction[filter_type].lower():  # Partial match for date and category
                    found = True
                    print("-----------------------------------------------------")
                    print(f"ID: {transaction['id']}, Date: {transaction['date']}, Amount: ${transaction['amount']:.2f}, Category: {transaction['category']}")
        if not found:
            print("-----------------------------------------------------")
            print("No transactions found with the given filter.")
    print("=====================================================")
    print("Returning to Main Menu...")
    print("=====================================================\n")

def edit_transaction():
    print("\n=====================================================")
    print("                 EDIT TRANSACTION                     ")
    print("=====================================================")
    transaction_id = input("Enter the transaction ID to edit \n(or type 'cancel' to return to menu): ")
    
    if transaction_id.lower() == 'cancel':
        print("Operation cancelled. Returning to main menu...")
        return
    try:
        transaction_id = int(transaction_id)
    except ValueError:
        print("Invalid input: Transaction ID must be a number.")
        return

    found = False
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            found = True
            print("-----------------------------------------------------")
            print(f"Editing Transaction ID: {transaction_id} \n(press Enter to keep current information)")

            # Date validation
            new_date = input(f"New Date (current: {transaction['date']}): ").strip()
            if new_date:
                if valid_date(new_date):
                    transaction['date'] = new_date
                else:
                    print("Invalid date format. Keeping the current date.")
            
            # Amount validation
            new_amount = input(f"New Amount (current: ${transaction['amount']:.2f}): ").strip()
            if new_amount:
                if re.match(r'^\d+(\.\d{1,2})?$', new_amount):
                    transaction['amount'] = float(new_amount)
                else:
                    print("Invalid amount format. Keeping the current amount.")
            
            # Category validation
            new_category = input(f"New Category (current: {transaction['category']}): ").strip()
            if new_category:
                transaction['category'] = new_category
            else:
                print("Invalid category. Keeping the current category.")
                
            print("=====================================================")
            print("Transaction updated successfully!")
            break
    if not found:
        print("=====================================================")
        print("Transaction ID not found.")
    print("=====================================================")
    print("Returning to Main Menu...")
    print("=====================================================\n")

def main_menu():
    print("""

  _____ _     _____               _       ____ _     ___ 
 |  ___(_)_ _|_   _| __ __ _  ___| | __  / ___| |   |_ _|
 | |_  | | '_ \| || '__/ _` |/ __| |/ / | |   | |    | | 
 |  _| | | | | | || | | (_| | (__|   <  | |___| |___ | | 
 |_|   |_|_| |_|_||_|  \__,_|\___|_|\_\  \____|_____|___|
                                                         
                                                                   
    """)
    while True:
        print("=====================================================")
        print("                   FinTrack CLI                      ")
        print("          An easy way to track your finances!        ")
        print("=====================================================")
        print("[1] Add Transaction")
        print("[2] View Transactions")
        print("[3] Edit Transaction")
        print("[4] Exit")
        print("=====================================================")
        choice = input("Select an option by entering a number: ")
        print("")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            edit_transaction()
        elif choice == '4':
            print("Exiting application.")
            print("=====================================================\n")
            break
        else:
            print("Invalid option. Please try again.")
            print("=====================================================\n")

if __name__ == "__main__":
    main_menu()
