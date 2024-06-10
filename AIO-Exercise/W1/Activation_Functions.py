import math

#Calculate Sigmoid, ReLU and ELU activation functions
def calculateSigmoid(x):
    return 1 / (1 + math.e**(-x))

def calculateReLU(x):
    return max(0, x)

def calculateELU(x):
    if x > 0:
        return x
    else:
        return 0.01 * (math.e**x - 1)
    
#Check if the input is number or not
def is_number(n):
    try:
        float(n)    #Type-casting the string to 'float'.
                    #If string is not a valid 'float' ,
                    #it ’ll raise 'ValueError' exception
    except ValueError:
        return False
    return True

#Print the value of activation function
def print_activation_function(value, activation_function):
    if activation_function == "Sigmoid":
        print("The value of Sigmoid function is:", calculateSigmoid(value)) 
    elif activation_function == "ReLU":
        print("The value of ReLU function is:", calculateReLU(value))
    elif activation_function == "ELU":
        print("The value of ELU function is:", calculateELU(value))
    else:
        print(activation_function, "is not supported")

#Main function
def main():
    value = input("Enter the value: ")
    if is_number(value):
        value = float(value)
    else:
        raise ValueError("Value must be a number")
    activation_funtion = input("Enter the activation function (Sigmoid | ReLU | ELU): ").strip() #strip() is used to remove the leading and trailing whitespaces
    print_activation_function(value, activation_funtion)

#Run the main function
if __name__ == "__main__":
    main()
