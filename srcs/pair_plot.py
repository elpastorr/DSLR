import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import sys
from collections import defaultdict

d = defaultdict(list)
d[0].append(1)

def pair_plot(data):
    data.dtypes

    # print unique values of data 
    data["Hogwarts House"].unique() 

    # convert some column into integer for representation in scatter matrix
    data["Hogwarts House"] = data["Hogwarts House"].convert_dtypes()

    data.head() 

    colors = {}
    if 'Ravenclaw' in data['Hogwarts House'].unique():
        colors['Ravenclaw'] = 'blue'
    if 'Slytherin' in data['Hogwarts House'].unique():
        colors['Slytherin'] = 'green'
    if 'Gryffindor' in data['Hogwarts House'].unique():
        colors['Gryffindor'] = 'red'
    if 'Hufflepuff' in data['Hogwarts House'].unique():
        colors['Hufflepuff'] = 'yellow'

    sns.pairplot(data, hue="Hogwarts House", palette= colors, height=1.0)
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Error: wrong arg number\nUsage: python3 describe.py datas/data_train.csv")
        return

    try:
        data = pd.read_csv(sys.argv[1])
        data.head()
    except Exception as e:
        print(e)
        return
    
    # Drop some unimportant columns in the dataset. 
    data.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], axis=1, inplace=True)

    pair_plot(data)


if __name__ == "__main__":
    main()