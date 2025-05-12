print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
Options = int(input("Enter your choice: "))
if (Options in [1, 2, 3, 4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if Options == 1:
        print("Addition of two numbers is: ", num1 + num2)
    elif Options == 2:
        print("Subtraction of two numbers is: ", num1 - num2)
    elif Options == 3:
        print("Multiplication of two numbers is: ", num1 * num2)
    elif Options == 4:
        if num2 != 0:
            print("Division of two numbers is: ", num1 / num2)
        else:
            print("Division by zero is not allowed")
else:
    print("Invalid choice")            