import matplotlib.pyplot as plt
import pandas as pd
import sys

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
    data.drop(["Index", "First Name", "Last Name", "Birthday"], axis=1, inplace=True)

    compare_columns(data, 'Arithmancy', 'Astronomy')
    compare_columns(data, 'Astronomy', 'Defense Against the Dark Arts')
    # compare_columns(data, 'Charms', 'Care of Magical Creatures')


if __name__ == "__main__":
    main()