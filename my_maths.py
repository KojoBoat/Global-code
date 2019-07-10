#function that takes arguments

def calculate(operation,num1,num2):
    if (operation == 'Add'):
        cal = num1 + num2
    elif (operation == 'Sub'):
        cal = num1-num2
    elif (operation == 'Mul' ):
        cal = num1 * num2
    elif (operation == 'Div'):
        cal = num1 / num2
    return cal

num1 = int(input("Enter the first number \n"))
num2 = int(input("Enter the second number \n"))
operation = input ("Which operation do you want to perform? \n")
print(calculate(operation,num1,num2))

