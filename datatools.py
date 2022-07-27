import matplotlib.pyplot as plt
import scipy.stats as stats
import csv
import numpy
import random

from math import *

FILENAME = "data/dataset_1_brca.csv"
DELIMITER = ","
FILTERED_HEADERS = ['']
MISSING_VALUES = [-1]


def getColumn(data, index):
    res = []
    for line in data:
        res.append(line[index])
    return res


def convertToNumeric(data):
    res = []
    for d in data:
        try:
            res.append(int(d))
        except:
            try:
                res.append(float(d.replace(',', '.')))
            except:
                return False

    for i in range(len(data)):
        data[i] = res[i]

    return True


def convertToHistogram(data):
    histo = {}
    for d in data:
        if d in histo:
            histo[d] += 1
        else:
            histo[d] = 1
    return histo


class UnivariateStats:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.isNumeric = convertToNumeric(self.data)

        if self.name in FILTERED_HEADERS:
            self.data = list(filter(lambda x: x not in MISSING_VALUES, self.data))

        self.histo = convertToHistogram(self.data)

        if self.isNumeric:
            self.skew = stats.skew(self.data)
            self.kurtosis = stats.kurtosis(self.data)

    def __repr__(self):
        res = f'{self.name}'

        nbValues = len(self.histo)
        res += f'\n   {nbValues} values'
        if nbValues == len(self.data):
            res += f'\n   INDEX'
        elif nbValues > 1:
            res += f'\n   {min(self.data)} ... {max(self.data)}'
        else:
            res += f'\n   {self.data[0]}'

        if self.isNumeric:
            res += f'\n   S:{self.skew:.1f}\tK:{self.kurtosis:.1f}'
        return res


if __name__ == "__main__":
    data = []
    with open(FILENAME, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=DELIMITER)
        headers = reader.fieldnames

        for row in reader:
            data.append([])
            for header in row:
                data[-1].append(row[header])

    # Data shape
    print(f'{len(headers)} variables x {len(data)} lines')

    variables = {}
    for i in range(len(headers)):
        uv = UnivariateStats(headers[i], getColumn(data, i))
        variables[headers[i]] = uv
        print(uv)

    # Show all histograms
    axSize = ceil(sqrt(len(variables)))
    fig, axes = plt.subplots(axSize, axSize)

    i, j = 0, 0
    for header in variables:
        axes[i, j].set_title(header)

        if len(variables[header].histo) <= 5:
            values = variables[header].histo.values()
            labels = list(variables[header].histo.keys())
            axes[i, j].pie(values, labels=labels, autopct="%4.2f%%", shadow=True)

        elif len(variables[header].histo) <= 10:
            axes[i, j].hist(variables[header].data)

        # Move towards the grid display
        i += 1
        if i >= axSize:
            i = 0
            j += 1

    plt.show()
