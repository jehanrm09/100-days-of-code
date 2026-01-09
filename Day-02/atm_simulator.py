balance = 1000

print("how much would you like to withdraw?")
user_input=int(input("Enter amount to withdraw : "))

if user_input > balance:
    print(f"Insufficient funds! you have only {balance} rupees")

elif user_input==balance:
    print("warning : Your account will be empty")

else:
    print("Withdrawal Successful")
    new_balance=balance-user_input
    print(f"Remaining balance: {new_balance}")