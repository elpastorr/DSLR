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


def get_mean(values, j):
    tmp = []
    for i in range(values.shape[0]):
        for k in range(values.shape[1]):
            if pd.notnull(values[i, k]) and k == j:
                tmp.append(values[i, k])
    return sum(tmp) / len(tmp)


def get_rid_of_nan(values):
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if pd.isnull(values[i, j]):
                values[i, j] = get_mean(values, j)
    return values


def get_min_max(values):
    minv = []
    maxv = []

    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if i == 0:
                minv.append(values[i, j])
                maxv.append(values[i, j])
            else:
                if values[i, j] < minv[j]:
                    minv[j] = values[i, j]
                if values[i, j] > maxv[j]:
                    maxv[j] = values[i, j]
            # print("i=", i, "j=", j, "value=", values[i, j])
            # print("min:", minv)
            # print("max:", maxv)
    return minv, maxv


def normalize_values(values, minv, maxv):
    norm_values = np.zeros(values.shape)
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            norm_values[i, j] = (values[i, j] - minv[j]) / (maxv[j] - minv[j])
    return norm_values


def normalize_data(data):
    courses = [column for column in data.columns if column not in ['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand']]
    values = data[courses].values
    values = get_rid_of_nan(values)
    minv, maxv = get_min_max(values)

    norm_values = normalize_values(values, minv, maxv)

    return norm_values


def train(data, houses):
    for house in houses:
        



def main():
    data = load_data("datasets/little_dataset_train.csv")
    if data is not None:
        norm_data = normalize_data(data)
    weights = train(norm_data, list(data['Hogwarts House'].unique()))

if __name__ == "__main__":
    main()