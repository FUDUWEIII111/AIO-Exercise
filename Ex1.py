#Calculates the Precision, Recall and F1-Score based on the input of True Positive, False Positive and False Negative values
def calculatePrecision(tp, fp):
    precision = tp/(tp + fp)
    return precision
    
def calculateRecall(tp, fn):
    recall = tp/(tp+fn)
    return recall
    
def calculateF1score(tp, fp, fn):
    precision = calculatePrecision(tp, fp)
    recall = calculateRecall(tp, fn)
    f1_score = 2*((precision * recall) / (precision + recall))
    return f1_score

#Check if the input is integer or not and convert it to integer
def checkInteger(tp, fp, fn):
    if tp.isdigit():
        tp = int(tp)
    else:
        print("tp must be integer")
    if fp.isdigit():
        fp = int(fp)
    else:
        print("fp must be integer")
    if fn.isdigit():
        fn = int(fn)
    else:
        print("fn must be integer")
    return tp, fp, fn

#Print the result of Precision, Recall and F1-Score
def printResult(tp, fp, fn):
    print("Precision is:", calculatePrecision(tp, fp))
    print("Recall is:", calculateRecall(tp, fn))
    print("F1-Score is:", calculateF1score(tp, fp, fn))
    
#Main function
def main():
    true_positive = input("Enter the value of True Positive: ")
    false_positive = input("Enter the value of False Positive: ")
    false_negative = input("Enter the value of False Negative: ")
    TP, FP, FN = checkInteger(true_positive, false_positive, false_negative)
    printResult(TP, FP, FN)

#Run the main function
if __name__ == "__main__":
    main()
