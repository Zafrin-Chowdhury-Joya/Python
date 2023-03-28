import random

def find_solution(func, target, inputs, max_iter=1000):
    for i in range(max_iter):
        x = random.choice(inputs) # randomly pick an input value from the list of inputs
        y = func(x)
        if y == target:
            return x, y
        else:
            print("not")

    return None

# Ask the user to input the function expression as a string
expression = input("Enter a function expression (using 'x' as the variable): ")
def example_function(x):
    return eval(expression)

inputs = [1,2,3,4,5,-1,-2,-3]



result = find_solution(example_function,0, inputs)

# Print the input value and the function value if a solution is found.
if result is not None:
    x, y = result
    print(f"x = {x}, y = {y}.")
else:
    print("No solution found.")
