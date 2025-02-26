
def deposit():
    while True:
        amount = input("Enter deposit amount: ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please Enter an amount greater that 0.")
        else:
            print("Please enter an valid amount.")

    return amount


deposit()