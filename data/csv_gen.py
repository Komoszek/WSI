import csv
import random
from datetime import datetime
random.seed(datetime.now().second)

def probableFalse(probability = 95):
    return random.randrange(1, 101) > probability

class Disease:
    def __init__(self, bol_brzucha, bol_gardla, bol_glowy, bol_miesni, bol_stawow, 
    bol_w_klatce, dreszcze, dusznosci, goraczka, kaszel, niezyt_nosa, nudnosci, 
    obrzek_konczyn, zaburzenia_nastroju, zgaga, zmeczenie, zmiana_masy, czy_chory):
        self.list = [bol_brzucha, bol_gardla, bol_glowy, bol_miesni, bol_stawow, 
    bol_w_klatce, dreszcze, dusznosci, goraczka, kaszel, niezyt_nosa, nudnosci, 
    obrzek_konczyn, zaburzenia_nastroju, zgaga, zmeczenie, zmiana_masy, czy_chory]
    def genRow(self):
        row = []
        for symptom in self.list:
            row.append(symptom ^ probableFalse())
        return row

def makeCSVFile(path, rowsNumber, delimiter=','):
    with open(path, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        header = ["bol brzucha", "bol gardla", "bol glowy", "bol miesni", "bol stawow", 
        "bol w klatce piersiowej", "dreszcze", "dusznosci", "goraczka", "kaszel", 
        "niezyt nosa", "nudnosci", "obrzek konczyn", "zaburzenia nastroju", "zgaga", 
        "zmeczenie", "nagla zmiana masy ciala", "chory?"]
        writer.writerow(header)

        grypa = Disease(False, True, True, True, True, False, True, False, True,
            True, True, False, False, False, False, True, False, True)
        angina = Disease(False, True, True, False, True, False, False, False, True,
            True, False, False, False, False, False, True, False, True)

        diseases = [grypa, angina]
        for _ in range(rowsNumber):
            writer.writerow(diseases[random.randrange(0, len(diseases))].genRow())
        csvfile.close()

makeCSVFile("test.csv", 5)



