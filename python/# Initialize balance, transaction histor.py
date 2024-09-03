# Initialize balance, transaction history, PIN, and number of attempts
balance = 0.0
transactions = []
pin = 1111
attempts = 3
line = "----------------------------"

# Display welcome message
print(line)
print("Welcome to the bank\n")
print(line)

# PIN verification loop
while attempts > 0:
    try:
        # Ask the user for their PIN
        pin_verify = int(input("Enter your pin to access your account: "))
        if pin_verify == pin:
            # Correct PIN, allow access
            print(line)
            print("Correct pin\n")
            break
        else:
            # Incorrect PIN, reduce attempts and notify user
            attempts -= 1
            print("Incorrect PIN, try again.")
            print(f"You have {attempts} attempts remaining")
            if attempts == 0:
                # Too many failed attempts, exit program
                print("Too many invalid attempts, exiting")
                quit()
    except ValueError:
        # Handle non-integer input for PIN
        print("Enter a valid pin")

# Function to check the balance
def checkbal():
    print(f"Your current balance is ${balance}")

# Function to deposit money
def deposit():
    global balance
    while True:
        try:
            # Ask the user how much they want to deposit
            deposit_money = float(input("\nHow much money do you want to deposit?: "))
            # Update the balance and add to transaction history
            balance += deposit_money
            transactions.append(f"+${deposit_money}")
            print(f"You have deposited ${deposit_money}, so you have ${balance} total")
            break
        except ValueError:
            # Handle non-numeric input for deposit
            print("Enter a valid amount")

# Function to withdraw money
def withdraw():
    global balance
    while True:
        try:
            # Ask the user how much they want to withdraw
            withdraw_money = float(input("How much money would you want to withdraw: "))
            if withdraw_money > balance:
                # Not enough balance to withdraw
                print(f"You don't have enough, you only have ${balance}")
            elif withdraw_money <= 0:
                # Handle invalid withdrawal amounts
                print("Invalid amount, please withdraw more than $1")
            else:
                # Update the balance and add to transaction history
                balance -= withdraw_money
                transactions.append(f"-${withdraw_money}")
                print(f"You have withdrawn ${withdraw_money}, so you have ${balance} total")
                return balance
        except ValueError:
            # Handle non-numeric input for withdrawal
            print("Input a valid number.")

# Function to display transaction history
def transac_history():
    print("Your transactions are below:\n")
    for transaction in transactions:
        print(transaction)

# Main function to display options and interact with the user
def main():
    global balance
    while True:
        try:
            # Display options to the user
            print("Enter a number from 1-5. The actions are as follows:")
            print("1. Check Balance ")
            print("2. Deposit Money ")
            print("3. Withdraw Money ")
            print("4. View transaction history ")
            print("5. Exit ")
            option = int(input("\nChoose your option: "))

            # Execute the selected option
            if option == 1:
                checkbal()
            if option == 2:
                deposit()
            if option == 3:
                if balance == 0:
                    # Prevent withdrawal if balance is zero
                    print("\nNot enough money to withdraw")
                    print("Try another time\n")
                else:
                    withdraw()
            if option == 4:
                transac_history()
            if option == 5:
                # Exit the program
                print("Exiting ATM")
                break
            elif option <= 6:
                # Handle invalid options
                print("Enter a number from 1-5")
        except ValueError:
            # Handle non-integer input for option selection
            print("Enter a valid number from 1-5")

# Start the main function
main()