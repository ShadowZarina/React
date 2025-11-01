// declaration of header files
#include <cs50.h>
#include <stdio.h>

// declaration of function
int number_checker(long number);

// main function
int main(void)
{
    long number;

    // do while function to ask user input
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);

    // execute function
    number_checker(number);

    // end program
    return 0;
}

// function to check credit card number
int number_checker(long number)
{
    // declaration of integers and longs
    int digits = 0, sum1 = 0, sum2 = 0, total = 0;
    long other, product, tens, ones;
    long temporary = number;
    long digit_counter = number;

    // while loop to determine number of digits
    while (digit_counter > 0)
    {
        digit_counter = digit_counter / 10;
        digits++;
    }

    // print INVALID if digit count is invalid
    if (digits != 13 && digits != 15 && digits != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // declaration of alt boolean
    bool alt = false;
    // while loop to determine every other digit of credit card number
    while (temporary > 0)
    {
        other = temporary % 10;
        temporary /= 10;

        // if statement to collect sums' values
        if (alt)
        {
            // multiply every other digit by 2
            product = other * 2;
            // obtain the tens place of 2-digit values
            tens = product / 10;
            // determine the ones place of 2-digit values
            ones = product % 10;
            // determine value of second sum
            sum2 = sum2 + tens + ones;
        }
        else
        {
            // add to the first sum for every other digit not multiplied by 2
            sum1 += other;
        }

        // make alt boolean true
        alt = !alt;
    }

    // find the total of the 2 sums
    total = sum1 + sum2;

    // print INVALID if total sum is indivisible by 10
    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // determine the value of the first 2 digits of the number
    long first = number;
    while (first >= 100)
    {
        first /= 10;
    }

    // if statement to determine credit card type
    if ((digits == 15) && (first == 34 || first == 37))
    {
        printf("AMEX\n");
    }
    else if ((digits == 16) && (first >= 51 && first <= 55))
    {
        printf("MASTERCARD\n");
    }
    else if ((digits == 13 || digits == 16) && (first / 10 == 4))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }

    // end function
    return 0;
}
