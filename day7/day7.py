f = open("day7.txt", "r")
def evaluate_left_to_right(equation):
    # Split the equation into tokens (numbers and operators)
    tokens = equation.split()
    
    # Start with the first number
    result = int(tokens[0])
    
    # Iterate through the tokens in pairs of (operator, operand)
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        elif operator == "||":
            result = int(str(result) + str(operand))
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    
    return int(result)
from itertools import product
def generate_equations(numbers):
    if len(numbers) < 2:
        raise ValueError("The list of integers must contain at least two numbers.")
    
    # Get all combinations of operators for the number of gaps between numbers
    operators = ['+', '*', "||"]
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    
    # Generate equations by interleaving numbers with operator combinations
    equations = []
    for ops in operator_combinations:
        equation = str(numbers[0])
        for num, op in zip(numbers[1:], ops):
            equation += f" {op} {num}"
        equations.append(equation)
    
    return equations

lines = f.readlines()
final_total = 0
for line in lines:
    total = line.split(":")[0]
    numbers = [int(x) for x in line.split(":")[1].strip().split(" ")]
    for equation in generate_equations(numbers):
        #print(evaluate_left_to_right(equation), total)
        if evaluate_left_to_right(equation) == int(total):
            #print("HIT")
            final_total += int(total)
            break
    #print("-------")

    
print(final_total)
