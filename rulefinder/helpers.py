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


def attrListToRule(attrList, patient_data, header):
    def attrEq(attr):
        return f"{header[attr]} = {patient_data[attr]}"
    return f"{' ∧ '.join(map(attrEq, attrList))} ⇒ {attrEq(patient_data[-1])}" 

def getRules(data, progress_callback): # TODO: proper implementation
    progress_callback.emit(("Loading data...", 0))
    patient_data = np.array(data)
    progress_callback.emit(("Removing discrepancies...", 1))
    # remove discrepencies
    # fun something bla ble bla

    progress_callback.emit(("Removing duplicates...", 2))
    # get unique patient data
    patient_data = np.unique(patient_data, axis=0)

    # 

    progress_callback.emit(("Removing d", 1))

    
    progress_callback.emit(("Removing a", 2))

    progress_callback.emit(("Finished", 7))
    return ['a', 'b', 'c'] # should return list of strings that describe rules