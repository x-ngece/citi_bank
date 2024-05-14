# Import datetime module for logging transaction timestamps
from datetime import datetime

try:
    # Create BankData.txt if it does not exist
    with open("BankData.txt", "x") as bank_data_file:
        bank_data_file.write("0.0")  # Initial balance set to 0.0
    
    # Create TransactionLog.txt if it does not exist
    with open("TransactionLog.txt", "x") as transaction_log_file:
        pass  # No initial content
    
    print("Bank data files created successfully.")
except FileExistsError:
    print("Bank data files already exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

try:
    # Read initial bank balance from BankData.txt
    with open("BankData.txt", "r") as file:
        balance = float(file.read())

    # Prompt user for transaction
    while True:
        transaction_choice = input("Would you like to make a transaction? (Yes or No): ").lower()
        if transaction_choice == "no":
            break
        elif transaction_choice != "yes":
            print("You provided an invalid input.")
            continue
        
        # Prompt user for deposit or withdrawal
        action_choice = input("Would you like to make a deposit or withdrawal? (Deposit or Withdrawal): ").lower()
        if action_choice == "deposit":
            amount = float(input("How much would you like to deposit? "))
            balance += amount
        elif action_choice == "withdrawal":
            amount = float(input("How much would you like to withdraw? "))
            if amount > balance:
                print("Insufficient funds.")
                continue
            balance -= amount
        else:
            print("You provided an invalid input.")
            continue
        
        # Update BankData.txt
        with open("BankData.txt", "w") as file:
            file.write(str(balance))
        
        # Log transaction
        with open("TransactionLog.txt", "a") as file:
            file.write(f"{action_choice.capitalize()} of {amount} at {datetime.now()}\n")
        
        print(f"Transaction successful. Updated balance: {balance}")

    # Display final balance
    print(f"Current balance: {balance}")

except FileNotFoundError:
    print("Bank data files not found. Please ensure BankData.txt and TransactionLog.txt exist.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {str(e)}")