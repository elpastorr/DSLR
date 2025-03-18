import pandas as pd
import sys

RED = "\033[31m"
BLUE = "\033[34m"
ENDC = "\033[0m"


def ft_sum(values):
    res = 0
    for value in values:
        res += value
    return res


def ft_len(array):
    res = 0
    for value in array:
        res += 1
    return res


def get_stats(data):
    values = []
    tmp = 0

    for value in data:
        if pd.notnull(value):
            values.append(value)

    count = ft_len(values)
    mean = ft_sum(values) / count

    for value in data:
        if pd.notnull(value):
            tmp += (value - mean) ** 2

    std = (tmp / count) ** 0.5

    values.sort()
    minv = values[0]
    maxv = values[ft_len(values) - 1]
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
                "Count": stats[0],
                "Mean": stats[1],
                "Std": stats[2],
                "Min": stats[3],
                "Q25%": stats[4],
                "Q50%": stats[5],
                "Q75%": stats[6],
                "Max": stats[7],
            }
        else:
            described_data[column] = "Value non calculable"

    print(
        f"{BLUE}{'Column':<30} {'Count':<10} {'Mean':<10} {'Std':<10} \
{'Min':<10} {'Q25%':<10} {'Q50%':<10} {'Q75%':<10} {'Max':<10}{ENDC}"
    )
    for column, stats in described_data.items():
        if isinstance(stats, dict):
            print(
                f"{BLUE}{column:<30} {ENDC}{stats['Count']:<10} \
{stats['Mean']:<10.2f} {stats['Std']:<10.2f} {stats['Min']:<10.2f} \
{stats['Q25%']:<10.2f} {stats['Q50%']:<10.2f} {stats['Q75%']:<10.2f} \
{stats['Max']:<10.2f}"
            )
        else:
            print(f"{BLUE}{column:<30}{RED} {stats}")


def main():
    if len(sys.argv) != 2:
        print(
            "Error: wrong arg number\nUsage: python3 describe.py datasets/dataset_train.csv"
        )
        return

    try:
        data = pd.read_csv(sys.argv[1])
    except Exception as e:
        print(e)
        return

    describe(data)


if __name__ == "__main__":
    main()
