import csv

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

def getRules(data): # TODO: proper implementation
    return ['a', 'b', 'c'] # should return list of strings that describe rules