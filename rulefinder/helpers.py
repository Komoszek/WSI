import csv
from turtle import update

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

def getRules(data, progress_callback): # TODO: proper implementation
    import time
    progress_callback.emit(("Removing d", 1))
    time.sleep(2)
    progress_callback.emit(("Removing a", 2))
    time.sleep(2)
    progress_callback.emit(("Removing c", 7))

    return ['a', 'b', 'c'] # should return list of strings that describe rules