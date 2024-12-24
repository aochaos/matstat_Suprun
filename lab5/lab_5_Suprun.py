def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_year_leap(year):
        return 29
    
    return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30 ]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")



def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_year_leap(year):
        return 29
    
    return days_in_months[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    day_of_year = 0
    for i in range(1, month):
        day_of_year += days_in_month(year, i)
    
    day_of_year += day
    return day_of_year

print(day_of_year(2000, 12, 31))  
print(day_of_year(2016, 2, 29))  
print(day_of_year(1987, 1, 1))    
print(day_of_year(1987, 12, 31))  
print(day_of_year(1900, 2, 29))   
print(day_of_year(2000, 2, 29))   
print(day_of_year(2024, 5, 12))   



import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()



def liters_100km_to_miles_gallon(liters):
    return 235.214583 / liters

def miles_gallon_to_liters_100km(miles):
    return 235.214583 / miles

print(liters_100km_to_miles_gallon(3.9))  
print(liters_100km_to_miles_gallon(7.5))  
print(liters_100km_to_miles_gallon(10.))  
print(miles_gallon_to_liters_100km(60.3)) 
print(miles_gallon_to_liters_100km(31.4)) 
print(miles_gallon_to_liters_100km(23.5))


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))


def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Тестування
print(is_a_triangle(3, 4, 5))  
print(is_a_triangle(1, 2, 3))  
print(is_a_triangle(5, 12, 13))  
print(is_a_triangle(7, 10, 5))  
print(is_a_triangle(10, 15, 25))  



def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    
    sides = sorted([a, b, c])
    
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Тестування
print(is_a_right_triangle(3, 4, 5))  
print(is_a_right_triangle(5, 12, 13)) 
print(is_a_right_triangle(1, 1, 1))  
print(is_a_right_triangle(7, 24, 25))  
print(is_a_right_triangle(10, 15, 20)) 


