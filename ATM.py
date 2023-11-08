print("Welcome to Abel National Bank")
pin = 1234
user_pin = int(input("Enter your password:"))
if pin == user_pin:
    print("Login successfully!")
else:
    print("Wrong password!")
    exit()
print("1.Balance\n2.Deposit \n3.Withdraw\n")
user_choice = int(input("Please select a number:"))
Balance = 500
if user_choice == 1:
    print(f"Balance is {Balance}$")
elif user_choice == 2:
    deposit = int(input("Enter amount:"))
    Balance = deposit+Balance
    print(f"Balance is {Balance}$")
elif user_choice == 3:
    Withdraw = int(input("Enter amount:"))
    if Withdraw > Balance:
        print("Balance insufficient!")
    else:
        Balance = Balance-Withdraw
        print(f"Balance is {Balance}$")
else:
    print("Synthax Error!")