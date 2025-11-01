# import from cs50
from cs50 import get_float

# declare main function


def main():

    # while loop to ask for user input
    while True:
        try:
            change = get_float("Change owed: ")
            change *= 100
            # move on to next function if valid
            if (change > 0):
                break
        # reprompt user if input is invalid
        except ValueError:
            pass

    # execute function to determine number of quarters and subtract
    quarters = calculate_quarters(change)
    change = change - (quarters * 25)

    # execute function to determine number of dimes and subtract
    dimes = calculate_dimes(change)
    change = change - (dimes * 10)

    # execute function to determine number of nickels and subtract
    nickels = calculate_nickels(change)
    change = change - (nickels * 5)

    # execute function to determine number of pennies and subtract
    pennies = calculate_pennies(change)
    change = change - (pennies)

    # declaration of total variable
    total = quarters + dimes + nickels + pennies
    # print out total number of coins
    print(total)


# quarters function
def calculate_quarters(change):
    quarters = 0
    while (change >= 25):
        quarters += 1
        change -= 25

    return quarters


# dimes function
def calculate_dimes(change):
    dimes = 0

    while (change >= 10):
        dimes += 1
        change -= 10

    return dimes


# nickels function
def calculate_nickels(change):
    nickels = 0

    while (change >= 5):
        nickels += 1
        change -= 5

    return nickels


# pennies function
def calculate_pennies(change):
    pennies = 0

    while (change >= 1):
        pennies += 1
        change -= 1

    return pennies


# start main function
main()
