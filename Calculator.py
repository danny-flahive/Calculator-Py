import sys

def calculator(question_arr):              
    operator = question_arr[1]
    try:                                    #Ensure the operand inputs are integers
        first_operand = int(question_arr[2])
        second_operand = int(question_arr[3])
    except:
        print("Invalid operand(s)")
        return
    if operator == "x":
        return multiply(first_operand, second_operand)
    elif operator == "/":
        if second_operand == 0:             #Prevents divide by 0 errors
            print("Cannot divide by 0")
            return
        return divide(first_operand, second_operand)
    elif operator == "+":
        return add(first_operand, second_operand)
    elif operator == "-":
        return subtract(first_operand, second_operand)
    else:
        print("Invalid operator")           #Only accepts valid operators

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def get_input_from_file(path):
    try:
        question_file = open(path)      #Prevents file not found errors
    except:
        print("Invalid file")
        return [-1]
    question_strings = question_file.read().splitlines()
    question_file.close()
    question_arr = []
    for question in question_strings:
        question_arr.append(question.split(" "))
    return question_arr

if __name__ == "__main__":
    questions = get_input_from_file("step_2.txt")
    results = []
    for question in questions:
        if question[0] == "calc":
            results.append(round(calculator(question), 3))
    print("Results: ")
    print(results)
    print("Sum: ")
    print(sum(results))