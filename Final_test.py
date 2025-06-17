# Q1. Write a Python program to Count Special Symbols, Constants, and
# Vowels in a String
# The number of vowels(a, e, i, o, u)
# The number of constants(all alphabets that are not vowels)
# The number of special symbols(characters that are not alphanumeric)

def count_characters(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    special_symbol_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif not char.isalnum():
            special_symbol_count += 1

    print("Vowels:", vowel_count)
    print("Constants:", consonant_count)
    print("Special Symbols:", special_symbol_count)


# Example input
input_string = "Hello@123!"
count_characters(input_string)
 
# Q2. Write a Python program to check whether a given string or number is

def is_palindrome(value):
    # Convert number to string if needed
    value_str = str(value)

    # Reverse the string and compare
    if value_str == value_str[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


# Test cases
is_palindrome(121)       # Output: Palindrome
is_palindrome("madam")   # Output: Palindrome
is_palindrome(123)       # Output: Not a palindrome
is_palindrome("hello")   # Output: Not a palindrome

# Q3. Write a Python program to check whether a number is prime.
def check_prime(number):
    if number <= 1:
        print(f"{number} is not a prime number.")
        return

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return

    print(f"{number} is a prime number.")
# Test cases
check_prime(7)   # Output: 7 is a prime number.
check_prime(10)  # Output: 10 is not a prime number.

# Q4. Write a Python program to check whether a number is an Armstrong
# number.
# (An Armstrong number is a number that is equal to the sum of its own
# digits raised to the power of the number of digits.)

def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over digits
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    if armstrong_sum == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

# Test cases
is_armstrong_number(153)  # Output: 153 is an Armstrong number.
is_armstrong_number(123)  # Output: 123 is not an Armstrong number.

# Q5. Write a Python program to print the Fibonacci series up to n terms.

def print_fibonacci_series(n):
    a, b = 0, 1
    fibonacci_sequence = []
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    print("Fibonacci series up to", n, "terms:")
    print(" ".join(map(str, fibonacci_sequence)))

# Example usage
n = 6
print_fibonacci_series(n)

# Q6. Write a Python program to print the following pattern:
#  A
#  AB
#  ABC
# ABCD
# ABCDE
def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(65, 65 + i):  # ASCII of 'A' is 65
            print(chr(j), end='')
        print()  # Move to next line


# Print the pattern with 5 rows
print_pattern(5)

# Q7. Write a Python program to calculate a student’s percentage based on
# marks in 5 subjects(Maths, Science, Hindi, English, Social Science),
# and classify the result:

def calculate_percentage_and_classify(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100  # Assuming each subject is out of 100

    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 90:
        classification = "A+"
    elif percentage >= 80:
        classification = "A"
    elif percentage >= 70:
        classification = "B"
    elif percentage >= 60:
        classification = "C"
    elif percentage >= 50:
        classification = "D"
    else:
        classification = "F"

    print(f"Classification: {classification}")


# Q8. Multiply All Numbers in List Using reduce() and lambda
# Write a Python program to multiply all numbers in a list.
from functools import reduce

def multiply_numbers(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    print("Product of all numbers:", result)

# Example usage
num_list = [1, 2, 3, 4, 5]
multiply_numbers(num_list)

# Q9. Extract Palindromes from a List Using filter() and lambda
# Write a Python program to filter out only palindrome strings from a list.

def is_palindrome(s):
    return s == s[::-1]

def extract_palindromes(strings):
    palindromes = list(filter(is_palindrome, strings))
    print("Palindromes in the list:", palindromes)

# Example usage
string_list = ["radar", "hello", "level", "world", "madam"]
extract_palindromes(string_list)


# Q10. Convert Temperatures from Celsius to Fahrenheit
# Given a list of temperatures in Celsius, convert them to Fahrenheit using
# map() and lambda .
def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = list(map(lambda c: (c * 9/5) + 32, celsius_list))
    print("Temperatures in Fahrenheit:", fahrenheit_list)