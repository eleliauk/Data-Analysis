import numpy as np

num_rows = 11
num_cols = 8

with open('data_HW1.txt', 'r') as f:
    lines = f.readlines()
    columns = [[] for i in range(num_cols)]
    for line in lines[1:]:
        numbers = line.strip().split('\t')
        for i, number in enumerate(numbers):
            columns[i].append(float(number))
            
    for i, column in enumerate(columns):
        print(f'{i}-th column')
        print('std: ', np.std(column))
        print('avg: ', sum(column) / len(column))