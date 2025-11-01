// declaration of header files
#include <cs50.h>
#include <stdio.h>

// declaration of functions
int calculate_quarters(int change);
int calculate_dimes(int change);
int calculate_nickels(int change);
int calculate_pennies(int change);

// main function
int main(void)
{
    // declaration of change variable
    int change;

    // do while loop for user input
    do
    {
        change = get_int("Change owed: ");
    }

    while (change < 0);

    // functions to determine and subtract change
    int quarters = calculate_quarters(change);
    change = change - (quarters * 25);

    int dimes = calculate_dimes(change);
    change = change - (dimes * 10);

    int nickels = calculate_nickels(change);
    change = change - (nickels * 5);

    int pennies = calculate_pennies(change);
    change = change - (pennies);

    // declaration of total variable
    int total = quarters + dimes + nickels + pennies;
    // print out change value
    printf("%d\n", total);
}

// quarters function
int calculate_quarters(int change)
{
    int quarters = 0;
    while (change >= 25)
    {
        quarters++;
        change -= 25;
    }
    return quarters;
}

// dimes function
int calculate_dimes(int change)
{
    int dimes = 0;
    while (change >= 10)
    {
        dimes++;
        change -= 10;
    }
    return dimes;
}

// nickels function
int calculate_nickels(int change)
{
    int nickels = 0;
    while (change >= 5)
    {
        nickels++;
        change -= 5;
    }
    return nickels;
}

// pennies function
int calculate_pennies(int change)
{
    int pennies = 0;
    while (change >= 1)
    {
        pennies++;
        change -= 1;
    }
    return pennies;
}
