import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


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


def checkfile(filename):
    if not os.path.isfile(filename):
        print(f"File {filename} not found")
        exit(1)


def load_data(filename):
    try:
        raw_data = pd.read_csv(filename)
        return raw_data
    except Exception as e:
        print(e)
        return None


def process_data(raw_data):
    classes = [ 'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts',
                'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
                'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']

    data = raw_data[classes].values
    data = get_rid_of_nan(data)


    data = StandardScaler().fit_transform(data)
    return data


def load_weights(filename):
    weights = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                house, values = line.strip().split(':')
                splited_values = np.array([float(x) for x in values.split(",")])
                weights[house] = splited_values
    except FileNotFoundError:
        print(f"File {filename} not found")
        exit(1)
    return weights


def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)


def predict(train_data, weights, houses):
    predictions = []

    for data in train_data:
        scores = []
        
        for house, values in weights.items():
            score = np.dot(data, values[1:]) + values[0]
            scores.append(score)

        probs = softmax(np.array(scores))

        predicted_house = houses[np.argmax(probs)]
        predictions.append(predicted_house)

    return predictions


def save_predictions(predictions, filename):
    result = pd.read_csv(filename)[['Index']]
    result['Hogwarts House'] = predictions
    result.to_csv('houses.csv', index=False)
    print("Predictions saved in houses.csv")


def main():
    filename = 'datasets/dataset_test.csv'

    checkfile(filename)
    raw_data = load_data(filename)
    if raw_data is None:
        print("Error: could not load data")
        return
    train_data = process_data(raw_data)

    weights = load_weights('weights.txt')

    houses = list(weights.keys())

    predictions = predict(train_data, weights, houses)

    save_predictions(predictions, filename)

if __name__ == "__main__":
    main()