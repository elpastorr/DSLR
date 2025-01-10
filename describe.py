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
    q1 = values[int(0.25 * count)]
    median = values[int(0.5 * count)]
    q3 = values[int(0.75 * count)]

    return (count, mean, std, min(values), q1, median, q3, max(values))


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



def compare_columns(data, col1, col2):
    if col1 not in data.columns or col2 not in data.columns:
        print(f"Error: Columns {col1} and/or {col2} not found in the dataset")
        return

    if not pd.api.types.is_numeric_dtype(data[col1]) or not pd.api.types.is_numeric_dtype(data[col2]):
        print(f"Error: Columns {col1} and/or {col2} are not numeric")
        return
    if 'Hogwarts House' not in data.columns:
        print("Error: 'Hogwarts House' column not found in the dataset")
        return
    colors = {}
    if 'Ravenclaw' in data['Hogwarts House'].unique():
        colors['Ravenclaw'] = 'blue'
    if 'Slytherin' in data['Hogwarts House'].unique():
        colors['Slytherin'] = 'green'
    if 'Gryffindor' in data['Hogwarts House'].unique():
        colors['Gryffindor'] = 'red'
    if 'Hufflepuff' in data['Hogwarts House'].unique():
        colors['Hufflepuff'] = 'yellow'
    houses = data['Hogwarts House'].unique()
    for house in houses:
        plt.scatter([], [], c=[colors[house]], label=house)
    plt.legend()
    plt.scatter(data[col1], data[col2], alpha=0.8, c=data['Hogwarts House'].apply(lambda x: colors[x]))
    plt.title(f"Comparison between {col1} and {col2}")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()

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
    # Example usage
    compare_columns(data, 'Arithmancy', 'Astronomy')

if __name__ == "__main__":
    main()