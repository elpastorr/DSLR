import sys
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        print(e)
        return None


def get_mean(data):
    values = []
    for value in data:
        if pd.notnull(value):
            values.append(value)
    return sum(values) / len(values)


def get_vars(group_data):
    vars = []
    for i in range(0, 4):
        var = 0
        values = group_data.iloc[i]
        mean = get_mean(values)
        for value in values:
            if pd.notnull(value):
                var += (value - mean) ** 2
        var /= len(values) - 1
        vars.append(var)
    return vars


def find_homogeneous_distrib(data):
    houses = data['Hogwarts House'].unique()
    courses = [column for column in data.columns if column not in ['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand']]
    homo_distrib = None
    min_var = float('inf')

    for course in courses:
        group_data = data.groupby('Hogwarts House')[course].apply(list)
        data_vars = get_vars(group_data)
        total_var = sum(data_vars) / len(data_vars)
        if total_var < min_var:
            min_var = total_var
            homo_distrib = course

    return homo_distrib


def main():
    if len(sys.argv) != 2:
        print("Error: wrong arg number\nUsage: python3 histogram.py datasets/dataset_train.csv")
        return
    data = load_data(sys.argv[1])
    if data is not None:
        homogeneous_distrib = find_homogeneous_distrib(data)
        if homogeneous_distrib:
            print(f"The course with the more homogeneous score distribution between all four houses is : {homogeneous_distrib}")
            # plot_histogram(data, homogeneous_distrib)
        else:
            print("No homogeneous score distribution found")


if __name__ == "__main__":
    main()