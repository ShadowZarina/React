#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Find the index level and round it to the nearest integer
    int index = round(0.0588 * letters / words * 100 - 0.296 * sentences / words * 100 - 15.8);

    // Output the grade level
    if (index < 1)
        printf("Before Grade 1\n");
    else if (index >= 16)
        printf("Grade 16+\n");
    else
        printf("Grade %d\n", index);

    return 0;
}

int count_letters(string text)
{
    int letters = 0;
    int length = strlen(text);

    // Return the number of letters in text
    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]) != 0)
            letters++;
    }

    return letters;
}

int count_words(string text)
{
    int words = 1;
    int length = strlen(text);

    // Return the number of words in text
    for (int i = 0; i < length; i++)
    {
        if (text[i] == ' ')
            words++;
    }

    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    int length = strlen(text);

    // Return the number of sentences in text
    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
            sentences++;
    }

    return sentences;
}
