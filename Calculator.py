from re import sub
import sys

def calculator():
    if len(sys.argv) == 4:                  #Ensure the corrent number of inputd are taken
        operator = sys.argv[1]
        try:                                #Ensure the operand inputs are integers
            first_operand = int(sys.argv[2])
            second_operand = int(sys.argv[3])
        except:
            print("Invalid operand(s)")
            return
        if operator == "x":
            print(multiply(first_operand, second_operand))
        elif operator == "/":
            if second_operand == 0:         #Prevents divide by 0 errors
                print("Cannot divide by 0")
                return
            print(divide(first_operand, second_operand))
        elif operator == "+":
            print(add(first_operand, second_operand))
        elif operator == "-":
            print(subtract(first_operand, second_operand))
        else:
            print("Invalid operator")
    else:
        print("Incorrect number of arguments")



def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

if __name__ == "__main__":
    calculator()