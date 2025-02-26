MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

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

def number_of_lines():
    while True:
        lines = input("How many line do you want to bet on(1-" +str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines > 0:
                break
            else:
                print("Please Enter a line in the range 1-" + str(MAX_LINES)+".")
        else:
            print("Please enter a numer.")

    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet on each line? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break
            else:
                print(f"Please Enter an amount in the range(₹{MIN_BET} - ₹{MAX_BET}).")
        else:
            print("Please enter an valid amount.")

    return amount

def main():
    balance = deposit()
    lines = number_of_lines()
    bet = get_bet() 
    bet *= lines
    print(balance, lines, bet)

main()