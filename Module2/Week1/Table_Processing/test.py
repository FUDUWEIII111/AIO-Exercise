import numpy as np
import pandas as pd

def question_15(df):
    max_value = df['Sales'].max()
    max_index = df['Sales'].idxmax()
    print(f'The maximum sales value is {max_value} and the index is {max_index}')

def question_16(df):
    average_value = df['TV'].mean()
    print(f'The average value of TV is {average_value}')

def question_17(df):
    count = [value for value in df['Sales'] if value >= 20]
    print(f'Number of values that greater than 20 in Sales columns is: {len(count)}')

def question_18(df):
    index = [index for index, value in enumerate(df['Sales']) if value >= 15]
    value = [value for value in df.loc[index, 'Radio']]
    average = np.mean(value)
    print(f'The average of Radio when Sales is greater than 15 is: {average}')

def question_19(df):
    average_newspaper = df['Newspaper'].mean()
    index = [index for index, value in enumerate(df['Newspaper']) if value > average_newspaper]
    value = [value for value in df.loc[index, 'Sales']]
    sum_value = np.sum(value)
    print(f'The sum of Sales when Newspaper is greater than average is: {sum_value}')

def question_20(df):
    average = df['Sales'].mean()
    scores = []
    for value in df['Sales']:
        if value > average:
            scores.append('Good')
        elif value < average:
            scores.append('Bad')
        else:
            scores.append('Average')
    print(scores[7:10])

def question_21(df):
    average = df['Sales'].mean()
    a = df['Sales'].iloc[0]
    for value in df['Sales']:
        if np.abs(value - average) < np.abs(a - average):
            a = value
    
    scores = []
    for value in df['Sales']:
        if value > a:
            scores.append('Good')
        elif value < a:
            scores.append('Bad')
        else:
            scores.append('Average')

    print(scores[7:10])

        


def main():
    df = pd.read_csv('D:\\AIO\\AIO-Exercise\\AIO-Exercise\\Module2\\Week1\\Table_Processing\\advertising.csv')
    question_15(df)
    question_16(df)
    question_17(df)
    question_18(df)
    question_19(df)
    question_20(df)
    question_21(df)

if __name__ == '__main__':
    main()