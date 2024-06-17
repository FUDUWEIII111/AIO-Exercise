import random
import math

#calculate MAE, MSE and RMSE
def calculate_mean_absolute_error(predict, target, number_of_samples):
    MAE = 0
    for i in range(number_of_samples):
        MAE = MAE + abs(target[i] - predict[i])
    return MAE/number_of_samples

def calculate_mean_squared_error(predict, target, number_of_samples):
    MSE = 0
    for i in range(number_of_samples):
        MSE = MSE + (target[i] - predict[i])**2
    return MSE/number_of_samples
    
def calculate_root_mean_squared_error(predict, target, number_of_samples):
    MSE = calculate_mean_squared_error(predict, target, number_of_samples)
    return math.sqrt(MSE)

#create sample of Predicts
def generate_predict(number_samples):
    predict = []
    for i in range(number_samples):
        x = random.uniform(0,10)
        predict.append(x)
    return predict

#create sample of Target
def generate_target(number_of_sample):
    target = []
    for i in range(number_of_sample):
        x = random.uniform(0,10)
        target.append(x)
    return target

#print value of target and predict
def print_samples(predict, target, number_of_samples):
    for i in range(number_of_samples):
        print("Sample-" + str([i]) + ": predict(" + str(predict[i]) + ") | target(" + str(target[i]) + ")")

def result_loss_function(loss_function, predict, target, number_of_samples):
    if loss_function == "MAE":
        print("Loss:", calculate_mean_absolute_error(predict, target, number_of_samples))
    elif loss_function == "MSE":
        print("Loss", calculate_mean_squared_error(predict, target, number_of_samples))
    elif loss_function == "RMSE":
        print("Loss:", calculate_root_mean_squared_error(predict, target, number_of_samples))
    else:
        print(loss_function, "not supported")

#main function
def main():
    num_samples = input("Enter number of samples: ")
    if num_samples.isnumeric():
        num_samples = int(num_samples)
    else:
        raise ValueError("Number of samples must be an integer number")
    loss_function = input("Enter the name of regression loss function (MAE | MSE | RMSE): ").strip()
    
    print("Loss name:", loss_function)
    predict = generate_predict(num_samples)
    target = generate_target(num_samples)
    print_samples(predict, target, num_samples)
    result_loss_function(loss_function, predict, target, num_samples)

if __name__ == "__main__":
    main()
    