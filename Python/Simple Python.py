

#Even and Odd Number Checker

number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")



#Simple Calculator

number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))
operation = int(input("Please enter the operation: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

def solve_operation(number1, number2, operation):
    match operation:
        case 1:
            sum = number1 + number2
            print(f"{number1} + {number2} = {sum}")
        case 2:
            difference = number1 - number2
            print(f"{number1} - {number2} = {difference}")
        case 3:
            product = number1 * number2
            print(f"{number1} * {number2} = {product}")
        case 4:
            if number2 == 0:
                print("Error: You cannot divide by zero!")
            else:
                quotient = number1 / number2
                print(f"{number1} / {number2} = {quotient}")
        case _:
            print("Please select from numbers 1 to 4!")

solve_operation(number1, number2, operation)



#Temperature Converter

number = float(input("Please enter a temperature: "))
unit1 = int(input("Please enter the unit you are using (1-3):\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))
unit2 = int(input("Please enter the unit you want to convert to (1-3):\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))

def conversion(number, unit1, unit2):
    if unit1 == unit2:
        print(f"{number:.2f} in the same unit is still {number:.2f}")
        return

    result = None

    if unit1 == 1:  # Celsius
        if unit2 == 2:
            result = (number * 9/5) + 32
            print(f"{number:.2f} °C is equivalent to {result:.2f} °F")
        elif unit2 == 3:
            result = number + 273.15
            print(f"{number:.2f} °C is equivalent to {result:.2f} K")

    elif unit1 == 2:  # Fahrenheit
        if unit2 == 1:
            result = (number - 32) * 5/9
            print(f"{number:.2f} °F is equivalent to {result:.2f} °C")
        elif unit2 == 3:
            result = ((number - 32) * 5/9) + 273.15
            print(f"{number:.2f} °F is equivalent to {result:.2f} K")

    elif unit1 == 3:  # Kelvin
        if unit2 == 1:
            result = number - 273.15
            print(f"{number:.2f} K is equivalent to {result:.2f} °C")
        elif unit2 == 2:
            result = (number - 273.15) * 9/5 + 32
            print(f"{number:.2f} K is equivalent to {result:.2f} °F")
    
    else:
        print("Error: Please select units between 1 and 3.")

conversion(number, unit1, unit2)



# FizzBuzz

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

def fizzbuzz(start, end):
    if start > end:
        print("Start should be less than or equal to end.")
        return
    
    for number in range(start, end + 1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)

fizzbuzz(start, end)


# Palindrome Checker

word = input("Enter a word: ")
first = 0
last = len(word) - 1

def palindrome_check(word, first, last):
    for letter in word:
        while first < last:
           if word[first] == word[last]:
              first += 1
              last -= 1
           else:
               print(f"The word {word} is not a palindrome.")
               return
        
    print(f"The word {word} is a palindrome.")
    
palindrome_check(word, first, last)



# Interest Calculator

principal = float(input("Enter your initial amount of money: "))
rate = float(input("Enter the interest rate (%): "))
time = int(input("Enter the amount of time (in months): "))
interest_type = float(input("Enter the type of interest you have:\n1. Simple Interest\n2. Compound Interest\n"))

years = time/12
percent = rate/100

def interest_calculator(principal, percent, years):

    interest = principal * percent * years

    total = interest + principal

    print(f"You would receive an interest of {interest:.2f} after {time} months, and your total amount of money will be {total:.2f}.")

    
    if interest_type == 1:
        total_simple = principal + interest * 5 
        print(f"\nAfter 5 years, you will have a total of {total_simple:.2f} in money.")
    else:
        total_compound = principal * (1 + percent)**5
        print(f"\nAfter 5 years, you will have a total of {total_compound:.2f} in money.")

    
interest_calculator(principal, percent, years)



# Vowel Checker

word = input("Please enter a word: ")


def vowel_check(word):
    letter = 0
    vowels = 0

    for letter in word.lower():
        if letter in "aeiou":
            vowels += 1
    
    print(f"The word {word} has {vowels} vowel(s).")

vowel_check(word)



# Number Guesser

import random

a = int(input("Enter the minimum value: "))
b = int(input("Enter the maximum value: "))
guess = int(input(f"Guess a number from {a} to {b}: "))

def guessing_game(a,b,guess):
    
    tries = 0
    secret_number = random.randint(a, b) 
    
    while tries < 3:
        if guess == secret_number:
            print("\nCongrats! You guessed right!\n")
            break
        else:
            print("\nTry again!")
            tries += 1
            if tries < 3:
                guess = int(input(f"Guess again (({3-tries} tries left): "))
            else:
                print(f"\nSorry, you've run out of tries. The correct number was {secret_number}!\n")

guessing_game(a,b,guess)



# Largest Number Finder

numbers_str = input("Enter up to 10 numbers separated by spaces: ")
numbers = [int(number) for number in numbers_str.split()]

def largest_number(numbers):

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest
    

largest = largest_number(numbers)

print(f"The largest number in the list is {largest}.")



# Rock Paper Scissors Game

import random

selected = int(input(f"Select between rock, paper, and scissors:\n1. Rock\n2. Paper\n3. Scissors\n"))

def rps_game(selected):
    
    move = ""
    enemy_move = ""

    enemy_selected = random.randint(1,3) 
    
    match selected:
        case 1:
            move = "Rock"
        case 2:
            move = "Paper"
        case 3:
            move = "Scissors"

    match enemy_selected:
        case 1:
            enemy_move = "Rock"
        case 2:
            enemy_move = "Paper"
        case 3:
            enemy_move = "Scissors"
    
    print(f"\nYou selected {move} versus {enemy_move}!")
    
    if selected == enemy_selected:
        print("You have a draw!")

    match selected:
        case 1:
            if enemy_selected == 2:
                print("You lose!")
            elif enemy_selected == 3:
                print("You win!")
        case 2:
            if enemy_selected == 3:
                print("You lose!")
            elif enemy_selected == 1:
                print("You win!")
        case 3:
            if enemy_selected == 1:
                print("You lose!")
            elif enemy_selected == 2:
                print("You win!")

rps_game(selected)



# Digital Dice Roller

import random

number = int(input("How many dice do you want rolled? "))

def dice_roll(number):
 
    sum = 0

    for i in range(number):
        roll = random.randint(1,6)
        print(f"Roll {i + 1}: {roll}")
        sum += roll

    print(f"Total value of rolls: {sum}")

dice_roll(number)



# Multiplication Table Generator

rows = int(input("How many rows do you want to include? "))
columns = int(input("How many columns do you want to include? "))

def table_generator(rows, columns):
    
    x = 1
    y = 1
    
    while x <= rows:
        print(x)
        x += 1

    while y <= columns:
        print("")
        print(y,end='\t')
        z = 2
        while z <= columns:
            print(y*z,end='\t')
            z += 1
        y += 1
    print()

table_generator(rows, columns)



# Days Until Birthday Calculator

from datetime import date

month = int(input("Enter your birthday month (1-12): "))
day = int(input("Enter your birthday day (1-31): "))


def days_until_birthday(month, day):

    today = date.today()
    birthday = date(today.year, month, day)

    if birthday < today:
        birthday = birthday.replace(year = today.year + 1)

    remaining = (birthday - today).days
    return remaining
    
days_to_birthday = days_until_birthday(month, day)

if days_to_birthday == 1:
    print(f"There is {days_to_birthday} day remaining until your next birthday!")
else:
    print(f"There are {days_to_birthday} days remaining until your next birthday!")



# Name Generator

'''
# (may need "pip install faker" to install in Anaconda)

from faker import Faker
faker = Faker()

number = int(input("How many names would you like to generate? "))

first_name = faker.unique.first_name()
last_name = faker.unique.last_name()
name = first_name + last_name

for i in number:
    print(name)

'''



# France Trivia Quiz

import random

print("How much do you know about France? Let's find out with the quiz below!")

def quiz_generator(questions):
    score = 0
    random.shuffle(questions)

    for question_data in questions:
        question = question_data["question"]
        options_dict = question_data["options"]
        correct_answer = question_data["answer"]

        print("\n" + question)

        # Convert options dictionary to a list of values and shuffle
        options = list(options_dict.values())
        random.shuffle(options)

        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        while True:
            try:
                user_answer_index = int(input("Enter your answer (number): ")) - 1
                if 0 <= user_answer_index < len(options):
                    user_answer = options[user_answer_index]
                    break
                else:
                    print("Invalid input. Please enter a number within the range of options.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    {
        'question': "What is the capital of France?",
        'options': {'A': "Berlin", 'B': "Madrid", 'C': "Paris", 'D': "Rome"},
        'answer': "Paris"
    },
    {
        'question': "What is the national flower of France?",
        'options': {'A': "Rose", 'B': "Iris", 'C': "Daffodil", 'D': "Tulip"},
        'answer': "Iris"
    },
    {
        'question': "How many kinds of cheese does France produce?",
        'options': {'A': "1000", 'B': "1200", 'C': "1400", 'D': "1600"},
        'answer': "1600"
    },
    {
        'question': "What is the nickname for the shape of France, referring to its hexagonal form?",
        'options': {'A': "L'Hexagone", 'B': "L'Île-de-France", 'C': "La Riviera", 'D': "La Belle France"},
        'answer': "L'Hexagone"
    },
    {
        'question': "What is the name of the largest river in France?",
        'options': {'A': "The Rhone", 'B': "The Seine", 'C': "The Loire", 'D': "The Rhone"},
        'answer': "The Loire"
    }
]

quiz_generator(questions)

# PYRAMIDS

# Number Half-Pyramid

def main():

    rows = int(input("Number of rows: "))

    for i in range(rows):
        num = 1
        for j in range(0, i + 1):
            print(num, end="")
            num += 1
        print("")

main()

# Reversed Number Half-Pyramid

def main():

    rows = int(input("Number of rows: "))

    for i in range(rows):
        num = rows
        for j in range(rows, i, -1):
            print(num, end="")
            num -= 1
        print("")

main()

# Hollow Right-Aligned Inverse Pyramid

def main():

    rows = int(input("Enter the number of rows: "))

    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i):
            if j == 0 or j == i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print(" ")

main()

# Right-Aligned Letter Pyramid

import string

def main(rows):
    letters = string.ascii_uppercase

    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        letter_index = 0 

        for _ in range(i):
            print(letters[letter_index], end="")
            letter_index += 1
        print()  

main(15)

## Full Asterisk Pyramid

def main(rows):
    
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(1, 2*i):
            print("*", end="")
        print()

main(15)

# Full Number Pyramid


def main(rows):
    
    for i in range(1, rows + 1):
        num = 1
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(1, 2*i):
            print(num, end="")
            num += 1
        print()

main(5)

# Reverse Full Alphabet Pyramid

import string

def main(rows):
    letters = string.ascii_uppercase

    for i in range(rows, 0, -1):
        letter_index = 0 
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(2*i - 1):
            print(letters[letter_index], end="")
            letter_index += 1
        print()

main(5)




# Using String Module

import string
import random

def main():
    s = input("Enter a sequence: ")
    a = "".join(char for char in s if char in string.ascii_letters)
    print(a)

    password = "".join(random.choices(string.ascii_letters, k=8))
    print(password)

main()