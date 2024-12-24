def calculate_life_number(date):
    digits = ''.join(filter(str.isdigit, date))

    digit_sum = sum(int(d) for d in digits)

    while digit_sum > 9:
        digit_sum = sum(int(d) for d in str(digit_sum))

    return digit_sum


while True:
    try:
        date = input("Введіть дату народження у форматі РРРРММДД, РРРРДДММ або ММДДРРРР: ")

        if not any(char.isdigit() for char in date):
            raise ValueError("Дата має містити хоча б одну цифру!")

        life_number = calculate_life_number(date)
        print("Цифра життя для дати {}: {}".format(date, life_number))
        break

    except ValueError as e:
        print(f"Помилка: {e}. Будь ласка, спробуйте знову.")
        

def get_integer(prompt, min_value, max_value):
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)
            
            if min_value <= number <= max_value:
                return number
            else:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value}).")
        
        except ValueError:
            print("Error: wrong input. Please enter an integer.")

result = get_integer("Enter an integer between 1 and 10: ", 1, 10)
print(f"You entered: {result}")
