#calculate factorial
def calculateFactorial(iteration):
    factorial = 1
    for i in range(1, iteration+1):
        factorial = factorial*i
    return factorial

#These programs calculate the sin, cos, sinh, and cosh of a given value
def calculateSin(value, iteration):
    sin = 0
    for i in range(iteration):
        sin = sin + ((-1)**i) * (value**(2*i+1)) / calculateFactorial(2*i+1)
    return sin
def calculateCos(value, iteration):
    cos = 0
    for i in range(iteration):
        cos = cos + ((-1)**i) * (value**(2*i)) / calculateFactorial(2*i)
    return cos
def calculateSinh(value, iteration):
    sinh = 0
    for i in range(iteration):
        sinh = sinh + value**(2*i+1) / calculateFactorial(2*i+1)
    return sinh
def calculateCosh(value, iteration):
    cosh = 0
    for i in range(iteration):
        cosh = cosh + value**(2*i) / calculateFactorial(2*i)
    return cosh

#Print the result of sin, cos, sinh, and cosh
def printResult(value, iteration):
    print("The value of sin(" + str(value) + ") is:", calculateSin(value, iteration))
    print("The value of cos(" + str(value) + ") is:", calculateCos(value, iteration))
    print("The value of sinh(" + str(value) + ") is:", calculateSinh(value, iteration))
    print("The value of cosh(" + str(value) + ") is:", calculateCosh(value, iteration))

#Main function
def main():
    radian_value = input("Enter the value: ")
    iteration = input("Enter the number of iteration: ")
    
    #Check if the iteration is positive number or not
    if iteration.isnumeric() and int(iteration) > 0:
        iteration = int(iteration)
    else:
        raise ValueError("Iteration must be a positive integer")
    
    printResult(float(radian_value), iteration)

#Run the main function
if __name__ == "__main__":
    main()