// declaration of header files
#include <cs50.h>
#include <stdio.h>

// main function
int main()
{
    // ask for user input
    string name = get_string("What's your name?\n");
    // print out hello statement
    printf("hello, %s\n", name);
}
