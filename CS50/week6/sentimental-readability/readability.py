from cs50 import get_string

# Collect input from user
string = get_string("Text: ")

letters = 0
sentences = 0
words = 1

# Count number of letters, words and sentences
for i in string:
    if (i == " "):
        words += 1
    elif (i == "." or i == "!" or i == "?"):
        sentences += 1
    elif (i.isalpha()):
        letters += 1

# Find the index level and round it to the nearest integer
index = round(0.0588 * letters / words * 100 - 0.296 * sentences / words * 100 - 15.8)

# Output the grade level
if (index < 1):
    print("Before Grade 1")
elif (index >= 16):
    print("Grade 16+")
else:
    print(f"Grade {index}")
