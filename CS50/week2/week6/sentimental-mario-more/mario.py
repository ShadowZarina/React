# import from cs50
from cs50 import get_int

# main function


def main():

    # while loop to ask for user input
    while True:
        try:
            height = get_int("Height: ")
            # move on to next function if valid
            if (1 <= height <= 8):
                break
        # reprompt user if input is invalid
        except ValueError:
            pass

    print_row(height)

# function to print rows


def print_row(height):
    i = 0

    # loop function
    while i < height:
        # loop to print spaces
        for j in range(height - i - 1):
            print(" ", end="")

        # loop to print left hashes
        for k in range(i + 1):
            print("#", end="")

        # prints a 2-space gap
        print("  ", end="")
        # loop to print right hasges
        for k in range(i + 1):
            print("#", end="")
        # move to next line
        i += 1
        print()


main()
