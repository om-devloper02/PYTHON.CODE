import time
import msvcrt

# Multiple users database
users = {
    "123456": {"password": "Omkar!@123", "balance": 20000.52},
    "654321": {"password": "jay@321", "balance": 15000.00},
    "987654": {"password": "rahul#999", "balance": 30000.75}
}

# '''Track login attempts & locked accounts'''
login_attempts = {acc: 0 for acc in users}
locked_accounts = set()

last_transaction = None

print("Welcome ATM Machine")
time.sleep(1)

print("Please insert card and hold steadyly...")
time.sleep(2)
print("Reading card...")
time.sleep(1)

# '''Ask for account number'''
account_no = input("Enter your Account Number: ").strip()

# '''Check if account exists'''
if account_no not in users:
    print("Invalid entry. Returning to main menu...")
    exit()

# '''If account already locked, show home-branch message'''
if account_no in locked_accounts:
    print("......Your account is locked.....")
    print("Please visit your home branch or contact customer support to unlock your account.")
    exit()

# '''Password input function (masked)'''
def input_password(prompt="Enter Password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getch()
        if ch in {b'\r', b'\n'}:
            print()
            break
        password += ch.decode()
        print("*", end="", flush=True)
    return password

# '''Password validation with 3 attempts'''
while True:
    user_password = input_password("Enter Your Password: ")

    if user_password == users[account_no]["password"]:
        print("Login successful. Welcome")
        break
    else:
        login_attempts[account_no] += 1
        print(f"Incorrect password. Attempt {login_attempts[account_no]}/3")

        if login_attempts[account_no] >= 3:
            locked_accounts.add(account_no)
            print("Too many incorrect attempts. Your account has been locked.")
            print("Please visit your home branch or contact customer support to unlock your account.")
            exit()

time.sleep(2)
print("Please wait while we process your request")
time.sleep(2)
print("You can now access your account")
time.sleep(1)

#''' ATM Menu'''
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Exit")
    choice = input("Please select an option (1-4): ")

    if choice == '1':
        balance = users[account_no]["balance"]
        print(f"Your current balance is: ${balance: }")
        last_transaction = ("Balance Inquiry", 0, balance)

    elif choice == '2':
        balance = users[account_no]["balance"]
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient balance")
        else:
            users[account_no]["balance"] -= amount
            print(f"Please take your cash. Your new balance is: ${users[account_no]['balance']: }")
            last_transaction = ("Cash Withdrawal", amount, users[account_no]["balance"])

    elif choice == '3':
        amount = float(input("Enter amount to deposit: $"))
        users[account_no]["balance"] += amount
        print(f"Deposit successful. Your new balance is: ${users[account_no]['balance']: }")
        last_transaction = ("Cash Deposit", amount, users[account_no]["balance"])

    elif choice == '4':
        print("Thank you for using our ATM. Goodbye!")
        break

    else:
        print("......Wrong choice. Please re-enter your selection.......")
        time.sleep(1)
        continue

    # '''Ask for receipt'''
    request_receipt = input("Print transaction receipt? (yes/no): ").strip().lower()
    if request_receipt == "yes":
        print("Generating receipt...")
        time.sleep(2)
        print("\n--------------------------------")
        print("          ATM Receipt")
        print("--------------------------------")
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Date: {current_time}")
        print(f"Account: {account_no}")

        if last_transaction:
            transaction, amt, new_balance = last_transaction
            print(f"Transaction: {transaction}")
            if transaction == "Cash Withdrawal":
                print(f"Amount Withdrawn: ${amt: }")
            elif transaction == "Cash Deposit":
                print(f"Amount Deposited: ${amt: }")
            elif transaction == "Balance Inquiry":
                print("Balance Inquiry only (No amount involved)")
            print(f"Balance: ${new_balance: }")
        else:
            print("No transaction performed yet.")

        print("--------------------------------")
        print("Thank you for using our ATM!")
        print("--------------------------------")
        time.sleep(2)
        print("Please take your card")
        time.sleep(2)
        print("Please take your card.")
        time.sleep(1)
        print("Goodbye!")
        break
