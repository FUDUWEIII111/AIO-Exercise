import random
import math

#calculate MAE, MSE and RMSE
def calculateMAE(predict, target, number_of_samples):
    MAE = 0
    for i in range(number_of_samples):
        MAE = MAE + abs(target[i] - predict[i])
    return MAE/number_of_samples

def calculateMSE(predict, target, number_of_samples):
    MSE = 0
    for i in range(number_of_samples):
        MSE = MSE + (target[i] - predict[i])**2
    return MSE/number_of_samples
    
def calculateRMSE(predict, target, number_of_samples):
    MSE = calculateMSE(predict, target, number_of_samples)
    return math.sqrt(MSE)

#create sample of Predicts
def generatePredict(number_samples):
    predict = []
    for i in range(number_samples):
        x = random.uniform(0,10)
        predict.append(x)
    return predict

#create sample of Target
def generateTarget(number_of_sample):
    target = []
    for i in range(number_of_sample):
        x = random.uniform(0,10)
        target.append(x)
    return target

#print value of target and predict
def printSamples(predict, target, number_of_samples):
    for i in range(number_of_samples):
        print("Sample-" + str([i]) + ": predict(" + str(predict[i]) + ") | target(" + str(target[i]) + ")")

def Result_Loss_Function(loss_function, predict, target, number_of_samples):
    if loss_function == "MAE":
        print("Loss:", calculateMAE(predict, target, number_of_samples))
    elif loss_function == "MSE":
        print("Loss", calculateMSE(predict, target, number_of_samples))
    elif loss_function == "RMSE":
        print("Loss:", calculateRMSE(predict, target, number_of_samples))
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
    predict = generatePredict(num_samples)
    target = generateTarget(num_samples)
    printSamples(predict, target, num_samples)
    Result_Loss_Function(loss_function, predict, target, num_samples)

if __name__ == "__main__":
    main()
    