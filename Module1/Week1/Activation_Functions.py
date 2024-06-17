import math

#Calculate Sigmoid, ReLU and ELU activation functions
def calculate_sigmoid(x):
    return 1 / (1 + math.e**(-x))

def calculate_relu(x):
    return max(0, x)

def calculate_elu(x):
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
        print("The value of Sigmoid function is:", calculate_sigmoid(value)) 
    elif activation_function == "ReLU":
        print("The value of ReLU function is:", calculate_relu(value))
    elif activation_function == "ELU":
        print("The value of ELU function is:", calculate_elu(value))
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
