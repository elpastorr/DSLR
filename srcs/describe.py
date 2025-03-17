import pandas as pd
import sys
import matplotlib.pyplot as plt


RED = '\033[31m'
BLUE = '\033[34m'
ENDC = '\033[0m'

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
    minv = values[0]
    maxv = values[len(values) - 1]
    q1 = values[int(0.25 * count)]
    median = values[int(0.5 * count)]
    q3 = values[int(0.75 * count)]

    return (count, mean, std, minv, q1, median, q3, maxv)


def describe(data):
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

    headers = ['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']

    print(f"{BLUE}{'Column':<20} {'Count':<10} {'Mean':<10} {'Std':<10} {'Min':<10} {'25%':<10} {'50%':<10} {'75%':<10} {'Max':<10}")
    for column, stats in described_data.items():
        if isinstance(stats, dict):
            print(f"{BLUE}{column:<20} {ENDC}{stats['Count']:<10} {stats['Mean']:<10.2f} {stats['Std']:<10.2f} {stats['Min']:<10.2f} {stats['25%']:<10.2f} {stats['50%']:<10.2f} {stats['75%']:<10.2f} {stats['Max']:<10.2f}{ENDC}")
        else:
            print(f"{BLUE}{column:<20}{RED} {stats}")

def main():
    if len(sys.argv) != 2:
        print("Error: wrong arg number\nUsage: python3 describe.py datasets/dataset_train.csv")
        return

    try:
        data = pd.read_csv(sys.argv[1])
    except Exception as e:
        print(e)
        return
    
    describe(data)

if __name__ == "__main__":
    main()