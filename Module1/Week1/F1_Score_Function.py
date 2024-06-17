#Calculates the Precision, Recall and F1-Score based on the input of True Positive, False Positive and False Negative values
def calculate_precision(tp, fp):
    precision = tp/(tp + fp)
    return precision
    
def calculate_recall(tp, fn):
    recall = tp/(tp+fn)
    return recall
    
def calculate_f1score(tp, fp, fn):
    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)
    f1_score = 2*((precision * recall) / (precision + recall))
    return f1_score

#Check if the input is integer or not and convert it to integer
def check_integer(tp, fp, fn):
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
def print_result(tp, fp, fn):
    print("Precision is:", calculate_precision(tp, fp))
    print("Recall is:", calculate_recall(tp, fn))
    print("F1-Score is:", calculate_f1score(tp, fp, fn))
    
#Main function
def main():
    true_positive = input("Enter the value of True Positive: ")
    false_positive = input("Enter the value of False Positive: ")
    false_negative = input("Enter the value of False Negative: ")
    TP, FP, FN = check_integer(true_positive, false_positive, false_negative)
    print_result(TP, FP, FN)

#Run the main function
if __name__ == "__main__":
    main()
