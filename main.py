#
print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("enter the first number: ")
    num2 = input("enter the second: ")
    #validation
    if(num1.isnumeric() and num2).isnumeric())
    sum = int(num1) + int(num2)
    print("the sum of 2 numbers is :"+str(sum))
elif operation == "2":
 num1 = input("enter the first number: ")
 num2 = input("inter the second: ")
 sub = int(num1) - int(num2)
 print("the difference between 2 numbers is : "+str(sub))
 if operation == "3":
    num1 = input("enter the first number: ")
    num2 = input("enter the second: ")
    mul = int(num1) * int(num2)
    print("the multiplication 2 values :"+str(mul))
elif operation == "4":
     num1 = input("enter the first number: ")
     num2 = input ("enter the second number:")
     div = int (num1) / int(num2)
     print("the division of 2 numbers :"+str(div))
    if num1.isnumeric() and num2.isnumeric():
        result = int(num1) + int(num2)
        print("The sum is " + str(result))
    else:
        print("Invalid input. Please enter a number.")

elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if num1.isnumeric() and num2.isnumeric():
        result = int(num1) - int(num2)
        print("The result is " + str(result))
    else:
        print("Invalid input. Please enter a number.")

elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if num1.isnumeric() and num2.isnumeric():
        result = int(num1) * int(num2)
        print("The result is " + str(result))
    else:
        print("Invalid input. Please enter a number.")

elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if num1.isnumeric() and num2.isnumeric():
        result = int(num1) / int(num2)
        print("The result is " + str(result))
    else:
        print("Invalid input. Please enter a number.")

else:
    print("Invalid Operation. Please enter 1, 2, 3, or 4.")