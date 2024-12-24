n = 55
print(n >= 100)

a = 2
b = 5

if a > b:
    largest = a
else:
    largest = b
print("The largest number is:", largest)


user_input = "spathiphyllum"

if user_input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif user_input == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {user_input}!")


income = 10000

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32
if tax < 0:
    tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


year = 1999

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")


odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Enter your guess: "))

# Цикл для перевірки
while guess != secret_number:
    print("Ha-ha! You've stuck in my loop!")
    guess = int(input("Try again: "))

# Виведення фінального повідомлення
print(secret_number)
print("Well done, muggle! You are free now.")


import time

for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)  # Затримка в 1 секунду після кожного виведення

print("Ready or not, here I come!")


while True:
    word = input("Please enter a word: ") 
    if word == "chupacabra": 
        print("You've successfully left the loop.")  
        break  


    user_word = "Gregory"

user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)


word_without_vowels = ""

user_word = input("Please enter a word: ")

user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)


blocks = 6

height = 0
used_blocks = 0

while used_blocks + (height + 1) <= blocks:
    height += 1  
    used_blocks += height  

print("The height of the pyramid is:", height)


c0 = int(input("Enter a natural number: "))

steps = 0

while c0 != 1:
    print(c0)  
    if c0 % 2 == 0:  
        c0 = c0 // 2
    else:  
        c0 = 3 * c0 + 1
    steps += 1 
print(c0)  
print("Total steps:", steps)



