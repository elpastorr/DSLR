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


def gradient_descent(data, binary, weights):
    epochs = 500
    learning_rate = 0.1
    m = len(binary)

    for epoch in range(epochs):
        # shuffle des donnés
        permutation = np.random.permutation(m)
        shuffled_data = data[permutation]
        shuffled_binary = binary[permutation]

        # calcul des predictions
        tmp = np.dot(shuffled_data, weights[1:]) + weights[0]
        predictions = sigmoid(tmp)

        # calcul du gradient
        gradient = np.zeros(len(weights))
        gradient[0] = (1 / m) * np.sum(predictions - shuffled_binary).item()
        gradient[1:] = (1 / m) * shuffled_data.T @ (predictions - shuffled_binary)

        # weights MAJ
        weights -= learning_rate * gradient

        # calcul du cout
        tmp = np.dot(data, weights[1:]) + weights[0]
        predictions = sigmoid(tmp)
        cost = (-1 / m) * np.sum(binary * np.log(predictions) + (1 - binary) * np.log(1 - predictions))

    return weights


def train(data, houses, data_houses):
    all_weights = {}

    for house in houses:
        binary = (data_houses == house).astype(int)
        weights = np.random.randn(data.shape[1] + 1) * 0.01
        weights = gradient_descent(data, binary, weights)
        all_weights[house] = weights
    return  all_weights


def save_weights(weights):
    with open("weights.txt", "w") as f:
        for house, weight in weights.items():
            f.write(f"{house}:{','.join(map(str, weight))}\n")


def main():
    data = load_data("datasets/dataset_train.csv")
    if data is None:
        print("Error: could not load data")
        return    
    norm_data = normalize_data(data)
    weights = train(norm_data, list(data['Hogwarts House'].unique()), data['Hogwarts House'].values)
    save_weights(weights)
    print("Weights saved in weights.txt")


if __name__ == "__main__":
    main()