choice = (input("a. Addition b. Subtraction c. Multiply d. Division: "))
if choice == "a":
    input1 = eval(input("Input your first number: "))
    input2 = eval(input("Input your second number: "))
    print(input1+input2)
elif choice == "b":
    input1 = eval(input("Input your first number: "))
    input2 = eval(input("Input your second number: "))
    print(input1-input2)
elif choice == "c":
    input1 = eval(input("Input your first number: "))
    input2 = eval(input("Input your second number: "))
    print(input1*input2)
elif choice == "d":
    input1 = eval(input("Input your first number: "))
    input2 = eval(input("Input your second number: "))
    print(input1/input2)
else:print("Invalid Entry!")