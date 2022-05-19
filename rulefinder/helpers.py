import csv
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
                booleanRow = [string == "True" for string in row]
                data.append(booleanRow)
        return PatientsTableData(header, data)

def getRules(data): # TODO: proper implementation
    matrix = np.array(data)
    return ['a', 'b', 'c'] # should return list of strings that describe rules