import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_counts = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_ckeck = column[line]
            if symbol != symbol_to_ckeck:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols += [symbol] * symbol_count

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
    

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
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if balance >= total_bet:
            break
        else:
            print(f"you do not have enough money, Current balance is ₹{balance}"), 
    print(f"Your balance is ₹{balance}. You bet ₹{bet} on {lines} lines. Total bet is ₹{total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_counts)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ₹{winnings}")
    print(f"You won on lines: ", *winning_lines)

main()