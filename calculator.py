num1 = float(input("enter you num 1: "))
operation = input("enter your oparation: ")
num2 = float(input("enter you num 2: "))
    

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2

print(f"the result of your calculation is {result}")
