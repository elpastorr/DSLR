import numpy as np
import pandas as pd


def sigmoid(z):
    """Compute the sigmoid of z"""
    return 1 / (1 + np.exp(-z))


def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        print(e)
        return None


def get_mean(column):
    values = []
    for value in column:
        if pd.notnull(value):
            values.append(value)
    return sum(values) / len(values)


def get_rid_of_nan(values):
    for i in range(values.shape[0]):
        mean = get_mean(values[i])
        for j in range(values.shape[1]):
            if pd.isnull(values[i, j]):
                values[i, j] = mean
    return values


def get_min_max(values):
    minv = []
    maxv = []


    # for i in range(values.shape[1]):
    #     for vals in values[:i]:
    #         minv.append(values[:i])
    #         print("minv=", minv)

    #         # for val in vals:
    #             # if minv[i]
    #                 # print("va:", val)
    # return 0, 0



def normalize_data(data):
    courses = [column for column in data.columns if column not in ['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand']]
    values = data[courses].values
    values = get_rid_of_nan(values)
    minv, maxv = get_min_max(values)

    # norm_values = (values - minv) / (maxv - minv)

    # return norm_values


def main():
    data = load_data("datasets/little_dataset_train.csv")
    if data is not None:
        norm_data = normalize_data(data)
        print(norm_data)


if __name__ == "__main__":
    main()