import math

# Calculate the single Minkowski Distance normalized Relative Error
def calculate_multidimensional_nre(y, y_hat, n, p):
    return ((math.pow(y, 1/n) - math.pow(y_hat, 1/n)))**p

# Check the input
def check_input(y, y_hat, n, p):
    try:
        float(y)
        float(y_hat)
        int(n)
        int(p)
        if int(n) > 0 or int(p) > 0:
            return float(y), float(y_hat), int(n), int(p)
    except ValueError:
        print("Invalid input")

# Main function
def main():
    y = input("Enter the value of y: ")
    y_hat = input("Enter the value of y_hat: ")
    n = input("Enter the value of n: ")
    p = input("Enter the value of p: ")
    y, y_hat, n, p = check_input(y, y_hat, n, p)
    print("The value of single MD-nRE is:", calculate_multidimensional_nre(y, y_hat, n, p))

if __name__ == "__main__":
    main()
