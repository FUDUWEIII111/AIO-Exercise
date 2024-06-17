#calculate factorial
def calculate_factorial(iteration):
    factorial = 1
    for i in range(1, iteration+1):
        factorial = factorial*i
    return factorial

#These programs calculate the sin, cos, sinh, and cosh of a given value
def calculate_sin(value, iteration):
    sin = 0
    for i in range(iteration):
        sin = sin + ((-1)**i) * (value**(2*i+1)) / calculate_factorial(2*i+1)
    return sin
def calculate_cos(value, iteration):
    cos = 0
    for i in range(iteration):
        cos = cos + ((-1)**i) * (value**(2*i)) / calculate_factorial(2*i)
    return cos
def calculate_sinh(value, iteration):
    sinh = 0
    for i in range(iteration):
        sinh = sinh + value**(2*i+1) / calculate_factorial(2*i+1)
    return sinh
def calculate_cosh(value, iteration):
    cosh = 0
    for i in range(iteration):
        cosh = cosh + value**(2*i) / calculate_factorial(2*i)
    return cosh

#Print the result of sin, cos, sinh, and cosh
def print_result(value, iteration):
    RESULT_MSG = ") is:"
    print("The value of sin(" + str(value) + RESULT_MSG, calculate_sin(value, iteration))
    print("The value of cos(" + str(value) + RESULT_MSG, calculate_cos(value, iteration))
    print("The value of sinh(" + str(value) + RESULT_MSG, calculate_sinh(value, iteration))
    print("The value of cosh(" + str(value) + RESULT_MSG, calculate_cosh(value, iteration))

#Main function
def main():
    radian_value = input("Enter the value: ")
    iteration = input("Enter the number of iteration: ")
    
    #Check if the iteration is positive number or not
    if iteration.isnumeric() and int(iteration) > 0:
        iteration = int(iteration)
    else:
        raise ValueError("Iteration must be a positive integer")
    
    print_result(float(radian_value), iteration)

#Run the main function
if __name__ == "__main__":
    main()