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
    patient_data = np.array(data.data)
    progress_callback.emit(("Removing discrepancies...", 1))
    # remove discrepencies
    patient_data = lower_approximation(patient_data)

    progress_callback.emit(("Removing duplicates...", 2))
    # get unique patient data
    patient_data = np.unique(patient_data, axis=0)

    # 
    print(patient_data)

    progress_callback.emit(("Removing d", 1))

    
    progress_callback.emit(("Removing a", 2))

    progress_callback.emit(("Finished", 7))
    return []

def separate_uncertain_rows(data):
    uncertain = []
    certain = []
    true_certain_count = 0
    false_certain_count = 0
    # sort by columns
    tmp_data = data[np.lexsort(data.T[::-1])]
    # get number of rows and columns
    row = np.shape(tmp_data)[0]
    sameRowCount = 0
    isCertain = True
    for i in range(row):
        sameRowCount += 1
        if i == row - 1:
            if isCertain:
                certain.append(tmp_data[i])
                if tmp_data[i,-1]:
                    true_certain_count += sameRowCount
                else:
                    false_certain_count += sameRowCount
            else:
                uncertain.append(tmp_data[i])
        else:
            currRow = tmp_data[i,:-1]
            nextRow = tmp_data[i+1,:-1]

            if np.array_equal(currRow, nextRow):
                
                if isCertain and tmp_data[i,-1] != tmp_data[i+1,-1]:
                    isCertain = False
            else:
                if isCertain:
                    certain.append(tmp_data[i])

                    if tmp_data[i,-1]:
                        true_certain_count += sameRowCount
                    else:
                        false_certain_count += sameRowCount
                else:
                    uncertain.append(tmp_data[i])
                sameRowCount = 0
                isCertain = True
    return certain, uncertain, true_certain_count, false_certain_count

def lower_approximation(data):
    rows_count = len(data)
    certain_rows, uncertain_rows, true_rows_count, false_rows_count = separate_uncertain_rows(data)
    
    if len(uncertain_rows) == 0:
        return certain_rows

    decision = true_rows_count/rows_count >= false_rows_count/rows_count

    for i in range(len(uncertain_rows)):
        uncertain_rows[i][-1] = decision

    if len(certain_rows) != 0:
        return np.concatenate((certain_rows, uncertain_rows))

    return uncertain_rows