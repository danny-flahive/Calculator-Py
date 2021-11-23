from math import floor

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

def process_goto(command):
    if len(command) == 2:                           #If it's strictly goto [line], return the line number
        return int(command[1]) - 1                  #-1 as the array is 0 indexed but commands aren't
    else:                                           #Else, there's a calculate command here
        return floor(calculator(command[1:]) - 1)   #Calculate and then -1 for indexing reasons

if __name__ == "__main__":
    commands = get_input_from_file("step_3.txt")
    current_index = 0
    seen_commands = []
    current_command = commands[current_index]
    while ((current_command not in seen_commands) and (current_index >= 0 and current_index < len(commands))):      #Within range and not seen before
        seen_commands.append(current_command)
        current_index = process_goto(current_command)
        current_command = commands[current_index]
    print("Stopped at line: ")
    print(current_index + 1)
    print("On the command: ")
    print(current_command)