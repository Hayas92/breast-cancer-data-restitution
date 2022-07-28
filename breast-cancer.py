import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from math import *

from matplotlib import pyplot

FILENAME = "data/dataset_1_brca.csv"
DELIMITER = ","
# FILTERED_HEADERS = ['']
# MISSING_VALUES = [-1]

# Pandas options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def gender_plot_pie(data, labels):
    colors = sns.color_palette('muted')
    plt.title('Répartition par genre')
    plt.pie(data, colors=colors, labels=labels, autopct='%.2f%%', shadow=True)
    plt.legend(bbox_to_anchor=(0.95, 0.95), ncol=1)
    plt.savefig('savefig/gender_plot_pie.png')

    plt.show()


def slice_age_histo(data):
    plt.subplots(figsize=(20, 10))
    plt.title('Tranche d\'âge')
    plt.hist([i for i in data.values.ravel().tolist() if i != -1], bins=10, color='skyblue')

    plt.xlabel("Age")
    plt.ylabel("Nombre de personne")
    plt.savefig('savefig/slice_age_histo.png')
    plt.show()


def death_by_tumour_stage(df):
    sns.set(font_scale=1.4)
    df["Tumour_Stage"].value_counts().plot(kind='bar', figsize=(15, 10), rot=0)
    plt.xlabel("Tumour_Stage", labelpad=14)
    plt.ylabel("Patient_Status", labelpad=14)
    plt.title("Nombre de morts par état du cancer", y=1.02)

    plt.savefig('savefig/death_by_tumour_stage.png')
    plt.show()


def last_visit_count(data, year):
    plt.subplots(figsize=(20, 10))
    plt.title('Nombre de dernière visite par années')
    plt.hist([i for i in data.values.ravel().tolist() if i != -1], bins=10)

    plt.xlabel("Année")
    plt.ylabel("Nombre de personne")
    plt.savefig(f'savefig/last_visit_count_{year}.png')
    plt.show()


def histology_plot_pie(data, labels):
    plt.subplots(figsize=(20, 10))
    colors = sns.color_palette('muted')
    plt.title('Répartition par type de cancer')
    plt.pie(data, colors=colors, labels=labels, autopct='%.1f%%', shadow=True)
    plt.legend(bbox_to_anchor=(0.95, 0.95), ncol=1)
    plt.savefig('savefig/histology_plot_pie.png')

    plt.show()


'''def operation_tumour_stage(df1, x1, x2, x3):
    df1["Tumour_Stage"].value_counts().plot(kind='bar', figsize=(15, 10), rot=0)
    labels = ['Surgery_type']
    x1 = tumour_I_df['Tumour_Stage']
    x2 = tumour_II_df['Tumour_Stage']
    x3 = tumour_III_df['Tumour_Stage']

    x = (len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, x1, width, label='Stage I')
    rects2 = ax.bar(x + width / 2, x2, width, label='Stage II')
    rects3 = ax.bar(x + width / 2, x3, width, label='Stage III')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('score')
    ax.set_title('Operation Done within the tumour stage')
    ax.set_xticks(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.show()'''


'''def operation_tumour_stage1(df1, x1, x2, x3):
    df1["Surgery_type"].value_counts().plot(kind='bar', figsize=(15, 10), rot=0)
    x1 = tumour_I_df['Tumour_Stage']
    x2 = tumour_II_df['Tumour_Stage']
    x3 = tumour_III_df['Tumour_Stage']


    bins = [x + 60, x + 60, x + 60]
    pyplot.hist([x1, x2, x3], bins=bins, color=['yellow', 'green', 'blue'],
                edgecolor='red', hatch='/', label=['x1', 'x2', 'x3'],
                histtype='barstacked')
    pyplot.ylabel('Patient_Status')
    pyplot.xlabel('Surgery_type')
    pyplot.title('Operation Done within the tumour stage')
    pyplot.legend()
    pyplot.show()'''

def operation_tumour_stage1(df1, x1, x2, x3):
    df1["Surgery_type"].value_counts().plot(kind='bar', figsize=(15, 10), rot=0)
    #df1["Tumour_Stage"].value_counts().plot(kind='bar', figsize=(15, 10), rot=0)
    x1 = tumour_I_df['Tumour_Stage']
    x2 = tumour_II_df['Tumour_Stage']
    x3 = tumour_III_df['Tumour_Stage']

    bins = [x - 2 for x in range(0, 6)]
    pyplot.hist([x1, x2, x3], bins=bins, color=['yellow', 'green', 'blue'],
                edgecolor='red', hatch='/', label=['Stage 1', 'Stage 2', 'Stage 3'],
                histtype='bar')  # bar est le defaut
    pyplot.ylabel('Patient_Status')
    pyplot.xlabel('Surgery_type')
    pyplot.title('Operation Done within the tumour stage')
    pyplot.legend()
    pyplot.show()

if __name__ == "__main__":
    # Import CSV file
    breast_data_df = pd.read_csv(FILENAME, delimiter=DELIMITER)
    # Drop undesirable columns
    breast_data_df = breast_data_df.drop(columns=['Protein1', 'Protein2', 'Protein3', 'Protein4'])
    # Uppercases only first letters
    breast_data_df.Gender = breast_data_df.Gender.str.capitalize()
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

    # Slice Age Histogramme
    print(breast_data_df['Age'].values.ravel().tolist())
    slice_age_histo(breast_data_df['Age'])

    # Number of deaths according to tumor stage
    # Replace '-1' by 'Unknown'
    breast_data_df['Tumour_Stage'] = breast_data_df['Tumour_Stage'].replace(-1, 'Unknown')
    breast_data_df['Patient_Status'] = breast_data_df['Patient_Status'].replace(-1, 'Unknown')

    # We recover only data from deceased patients
    dead_patients_df = breast_data_df.query('Patient_Status == "Dead"')
    print(dead_patients_df)
    death_by_tumour_stage(dead_patients_df)

    # Number of last visits per year
    year = 2019
    breast_data_df['year_month'] = breast_data_df['Date_of_Last_Visit'].dt.strftime(f'%m/{year}')
    print(breast_data_df['year_month'].unique())
    data = breast_data_df['year_month'].sort_values()

    last_visit_count(data, year)

    # Histology Plot Pie
    data = breast_data_df['Histology'].value_counts()
    labels = breast_data_df['Histology'].unique()
    histology_plot_pie(data, labels)

    tumour_I_df = breast_data_df.query('Tumour_Stage == "I"')
    tumour_II_df = breast_data_df.query('Tumour_Stage == "II"')
    tumour_III_df = breast_data_df.query('Tumour_Stage == "III"')
    operation_tumour_stage1(breast_data_df, tumour_I_df, tumour_II_df, tumour_III_df)