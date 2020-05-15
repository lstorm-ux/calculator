
input("Let's do some Maths")
x = int(input("Type a number: "))
operation = input("Choose the arithmetic operation: (+, -, * or /)")
y = int(input("Type another number: "))


if operation == "+":
    sum = int(x) + int(y)
    print("The sum is: ", sum)

elif operation == "-":
    sum = int(x) - int(y)
    print("The sum is: ", sum)

elif operation == "*":
    sum = int(x) * int(y)
    print("The sum is: ", sum)

elif operation == "/":
    sum = int(x) / int(y)
    print("The sum is: ", sum)

else:
    print("That is not an aritmetic operation!")