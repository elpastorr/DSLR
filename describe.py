import pandas as pd
import sys


def get_stats(data):
    values = []
    tmp = 0

    for value in data:
        if pd.notnull(value):
            values.append(value)

    count = len(values)
    mean = sum(values) / count

    for value in data:
        if pd.notnull(value):
            tmp += (value - mean) ** 2

    std = (tmp / count) ** 0.5

    values.sort()
    q1 = values[int(0.25 * count)]
    median = values[int(0.5 * count)]
    q3 = values[int(0.75 * count)]

    return (count, mean, std, min(values), q1, median, q3, max(values))


def describe(filename):
    try:
        data = pd.read_csv(filename)
    except Exception as e:
        print(e)
        return

    described_data = {}

    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            stats = get_stats(data[column])
            described_data[column] = {
                'Count': stats[0],
                'Mean': stats[1],
                'Std': stats[2],
                'Min': stats[3],
                '25%': stats[4],
                '50%': stats[5],
                '75%': stats[6],
                'Max': stats[7],
            }
        else:
            described_data[column] = "Value non calculable"
    print(described_data)
# PRINT TOUT CA CLEAN

def main():
    if len(sys.argv) != 2:
        print("Error: wrong arg number\nUsage: python3 describe.py datasets/dataset_train.csv")
    else:
        describe(sys.argv[1])

if __name__ == "__main__":
    main()