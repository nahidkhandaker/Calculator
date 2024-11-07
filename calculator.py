print("Welcome to Calculator Project") 
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divition")

option = int(input("Select an option for Basic Calculatior Operation: "))

if option == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = num1 + num2

    print("Addition of two numbers is: ", num3)

elif option == 2:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = num1 - num2

    print("Substraction of two numbers is: ", num3)


elif option == 3:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = num1 * num2

    print("Multiplication of two numbers is: ", num3)

elif option == 4:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = num1 / num2

    print("Division of two numbers is: ", num3)

else:
    print("Invalid Input")



