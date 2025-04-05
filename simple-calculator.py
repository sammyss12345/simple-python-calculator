# Simple calculator program
# Ask for input from the user 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operator(+ , - , * , /): ")
# Perform the Operation 
if operation == '+':
   result = num1 + num2
   print(f"{num1}+{num2}= {result}")

elif operation == '-':
     result = num1 - num2
     print(f"{num1}-{num2}= {result}")

elif operation== '*' :
    result = num1 * num2
    print(f"{num1}*{num2}= {result}")

elif operation == '/':
    if num2 != 0 :
        result = num1 / num2
        print(f"{num1}/{num2}= {result}")
    else : 
        print("Division by zero is not allowed.")   

else:
    print("Invalid operator entered.")         


    