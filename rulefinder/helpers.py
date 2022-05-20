import csv
import itertools

import numpy as np

class PatientsTableData:
    def __init__(self, header=None, data=None):
        self.header = header
        self.data = data


def readCSVFile(path, delimiter=','):
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        header = None
        data = []
        for row in reader:
            if header is None:
                header = row
            else:
                data.append(row)
        return PatientsTableData(header, data)


def separate_uncertain_rows(data):
    uncertain = []
    certain = []

    tmp_data = np.array(data)
    enum_list = [(i, tmp_data[i]) for i in range(len(tmp_data))]
    similar = []
    for a, b in itertools.combinations(enumerate(tmp_data), 2):

        is_similar = ((a[1][:-1] == b[1][:-1]).all())

        if is_similar:
            is_similar = a[1][-1] != b[1][-1]
            if is_similar:
                similar.append(a[0])
                similar.append(b[0])

    similar = np.unique(similar)
    for i in range(len(tmp_data)):
        if i in similar:
            uncertain.append(data[i])
        else:
            certain.append(data[i])
    return certain, uncertain


def count_decisions(array):
    count_true = 0
    count_false = 0
    for i in array:
        if i[-1]:
            count_true += 1
        else:
            count_false += 1
    return count_true, count_false


def lower_approximation(data):
    rows_count = len(data)
    certain_rows, uncertain_rows = separate_uncertain_rows(data)
    true_rows_count, false_rows_count = count_decisions(certain_rows)
    decision = True
    if true_rows_count/rows_count < false_rows_count/rows_count:
        decision = False
    for i in uncertain_rows:
        i[-1] = decision
    data = list(itertools.chain(certain_rows, uncertain_rows))
    return data


def getRules(data): # TODO: proper implementation
    data.data = lower_approximation(data.data)
    print(data.data)
    unique_data = np.unique(data.data, axis=0)

    return ['a', 'b', 'c'] # should return list of strings that describe rules