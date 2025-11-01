# import from cs50
from cs50 import get_int

# declare main function


def main():

    # while loop to ask for user input
    while True:
        try:
            number = get_int("Number: ")
            # move on to next function if valid
            if (number > 0):
                break
        # reprompt user if input is invalid
        except ValueError:
            pass

    # execute function to determine credit card type
    number_checker(number)


# declare function to check credit card number
def number_checker(number):

    # declaration of variables
    digits, sum1, sum2, total = 0, 0, 0, 0
    other, product, tens, ones = 0, 0, 0, 0
    temporary = number
    digit_counter = number

    # while loop to determine number of digits
    while (digit_counter > 0):
        digit_counter = digit_counter // 10
        digits += 1

    # print INVALID if digit count is invalid
    if (digits != 13 and digits != 15 and digits != 16):
        print("INVALID\n")
        return 0


    # declaration of alt variable
    alt = False
    # while loop to determine every other digit of credit card number
    while (temporary > 0):
        other = temporary % 10
        temporary // 10

        # if statement to collect sums' values
        if (alt):

            # multiply every other digit by 2
            product = other * 2
            # obtain the tens place of 2-digit values
            tens = product / 10
            # determine the ones place of 2-digit values
            ones = product % 10
            # determine value of second sum
            sum2 = sum2 + tens + ones

        else:
            # add to the first sum for every other digit not multiplied by 2
            sum1 += other


        # make alt variable true
        alt = not alt


    # find the total of the 2 sums
    total = sum1 + sum2

    # print INVALID if total sum is indivisible by 10
    if (total % 10 != 0):
        print("INVALID\n")
        return 0

    # determine the value of the first 2 digits of the number
    first = number
    while (first >= 100):
        first // 10

    # if statement to determine credit card type
    if ((digits == 15) and (first == 34 or first == 37)):
        print("AMEX\n")
    elif ((digits == 16) and (first >= 51 and first <= 55)):
        print("MASTERCARD\n")
    elif ((digits == 13 or digits == 16) and (first // 10 == 4)):
        print("VISA\n")
    else:
        print("INVALID\n")

    # end function
    return 0

# start main function
main()
