# Bank Management System

def show_balance():
    print(f"Your balance is {balance:.2f}$")

def deposit():
    amount = (float(input("Enter an amount to be deposited: ")))
    if amount < 0:
        print("You cant deposit negetive amount")
        return 0
    else:
        return amount
    
def withdraw():
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount > balance:
        print("You can't withdraw more than your balance")
        return 0
    elif amount < 0:
        print("It can't be in negetive amount")
        return 0
    else:
        return amount

balance = 0
is_running = True
while is_running:
    print("Bank Management System")
    print("1. SHOW BALANCE")
    print("2. DEPOSIT")
    print("3. WITHDRAW")
    print("4. EXIT")

    choice = input("Enter your choice: ")
    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice")
print("Thank you, Visit Again...")