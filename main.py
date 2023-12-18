import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count = {
    "A": 2,
    "B": 4,
    "C":6,
    "D":8
}


symbol_value = {
    "A": 20,
    "B": 12,
    "C":16,
    "D":18  
}




def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)   
            column.append(value)

        columns.append(column)

    return columns





def print_slot_machine(columns):
    for row in range(len(columns)):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()                              # This print statement will take cursor to a new line




def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def deposit():
    while True:                                               #while loop will continue till we get proper input
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than zero.")
        else:
            print("Please enter a number.")
    return amount




def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines should be within 1-3.")
        else:
            print("Please enter a line between 1 to 3.")

    return lines




def get_bet():
    while True:
        bet = input("Enter your bet on each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amout must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return bet




def spin(balance):

    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet*lines

        if total_bet>balance:
            print(f"You have insufficient balance, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slot_machine = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot_machine)

    winnings, winning_lines = check_winnings(slot_machine, lines, bet, symbol_value)

    print(f"Your winnings are ${winnings}")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet




def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or q to quit")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

    
    


main()


