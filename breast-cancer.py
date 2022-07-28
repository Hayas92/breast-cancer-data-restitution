import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from math import *

FILENAME = "data/dataset_1_brca.csv"
DELIMITER = ","
# FILTERED_HEADERS = ['']
# MISSING_VALUES = [-1]

# pandas options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def gender_plot_pie(data, labels):
    data = data
    colors = sns.color_palette('muted')
    plt.title('Cancer du seins par sexe')
    plt.pie(data, colors=colors, labels=labels, autopct='%.2f%%', shadow=True)
    plt.savefig('savefig/gender_plot_pie.png')
    
    plt.show()


if __name__ == "__main__":
    # Import CSV file
    breast_data_df = pd.read_csv(FILENAME, delimiter=DELIMITER)
    # Drop undesirable columns
    breast_data_df = breast_data_df.drop(columns=['Protein1', 'Protein2', 'Protein3', 'Protein4'])
    # Remove NaN values
    breast_data_df = breast_data_df.replace(np.nan, -1)
    # Convert `Age` to int
    breast_data_df['Age'] = breast_data_df['Age'].astype(int, errors='ignore')

    # Convert `Date_of_Surgery` and `Date_of_Last_Visit` in the right format
    breast_data_df['Date_of_Surgery'] = pd.to_datetime(breast_data_df['Date_of_Surgery'])
    breast_data_df['Date_of_Last_Visit'] = pd.to_datetime(breast_data_df['Date_of_Last_Visit'])

    # Print NaN sum
    print(breast_data_df.isna().sum())
    # Checkout of the types of the different column
    print(breast_data_df.dtypes)
    # Print df head
    print(breast_data_df.head())

    # Gender Plot Pie
    data = breast_data_df['Gender'].value_counts()
    labels = breast_data_df['Gender'].unique()
    gender_plot_pie(data, labels)
