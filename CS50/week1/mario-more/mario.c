// declaration of header files and function
#include <cs50.h>
#include <stdio.h>
void print_row(int height);

// main function
int main(void)
{
    int height;

    do
    {
        height = get_int("Height: ");
    }

    while ((height < 1) || (height > 8));

    print_row(height);
}

// function to print rows
void print_row(int height)
{
    int i, j, k;

    // loop function
    for (i = 0; i < height; i++)
    {
        // loop to print spaces
        for (j = (height - 1); j > i; j--)
        {
            printf(" ");
        }

        // loop to print left hashes
        for (k = 0; k <= i; k++)
        {
            printf("#");
        }
        // prints a 2-space gap
        printf("  ");
        // loop to print right hasges
        for (k = 0; k <= i; k++)
        {
            printf("#");
        }

        // moves to next line
        printf("\n");
    }
}
