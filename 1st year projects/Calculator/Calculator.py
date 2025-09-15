import math

print("Simple Calculator created by Lanz Olaes\n")

while True:
    
    operation = input("Enter operation: +, -, *, /, sqrt, ^, or press q to quit: ")
    if operation == "q":
        print("Thanks for using me!")
        break
    
    if operation == "sqrt":
        x = float(input("Enter your number: "))
        print(f"Result: {math.sqrt(x):}\n")
        continue
    
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if operation == "+":
        print (f"Result: {int(x + y)}\n")
    elif operation == "-":
        print (f"Result: {int(x - y)}\n")
    elif operation == "*":
        print (f"Result: {int(x * y)}\n")
    elif operation == "/":
        if y == 0:   
            print ("Not divisible by 0!\n")
        else:
            print (f"Result: {int(x // y)}, remainder: {int(x % y)}\n")
    elif operation == "^":
        print (f"Result: {x ** y}\n")
    else:
        print ("Invalid operation!\n")
