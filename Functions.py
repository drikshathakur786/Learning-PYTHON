# Function- made to reuse the code
# block of code which only runs when it is called
# You can pass data, known as parameters, into a function

# Creating a function:
def hello():
    print('Hello Driksha')

# Sum of two numbers using functions
def sum_of_two():
    num1 = 10
    num2 = 30
    result = num1 + num2
    print(result)
# Calling the function
sum_of_two()


# Calculate salary of a employee
# No. of days = 28
# per_day_salary =1000

def tankha(days_worked, per_day_salary):
    salary = days_worked * per_day_salary
    return salary

number_of_days = 28
per_day_salary = 1000

employee_salary = tankha(number_of_days, per_day_salary)
print("Employee's salary is:", employee_salary)

# Input vowel/consonant and check using function
def check_vowel_consonant(char):
    char = char.lower()
    if char in ['a','e','i','o','u']:
        return f"{char} is a vowel."
    elif char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        return f"{char} is a consonant."
    else:
        return "Invalid input. Please enter a valid alphabet."

input_char = input("Enter:")

result = check_vowel_consonant(input_char)
print(result)

