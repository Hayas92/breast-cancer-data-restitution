import scipy.stats as stats
import csv

FILENAME = "data/dataset_1_brca.csv"
DELIMITER = ";"
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
