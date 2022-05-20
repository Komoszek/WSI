import csv
import random
from datetime import datetime
random.seed(datetime.now().second)

def probableFalse(probability = 95):
    return random.randrange(1, 101) > probability

class Disease:
    def __init__(self, biegunka, bol_brzucha, bol_gardla, bol_glowy, bol_miesni, 
    bol_stawow, bol_w_klatce, dusznosci, goraczka, kaszel, nudnosci, obrzek_konczyn, 
    zaburzenia_nastroju, zgaga, zmeczenie, zmiana_masy, zmiany_skorne, internistyczna):
        self.list = [biegunka, bol_brzucha, bol_gardla, bol_glowy, bol_miesni, bol_stawow, bol_w_klatce, dusznosci, goraczka, kaszel, nudnosci, obrzek_konczyn,zaburzenia_nastroju, zgaga, zmeczenie, 
        zmiana_masy, zmiany_skorne, internistyczna]
    def genRow(self):
        row = []
        for symptom in self.list:
            row.append(symptom ^ probableFalse())
        return row

def makeCSVFile(path, rowsNumber, delimiter=','):
    with open(path, 'w', newline='\n', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        header = ["biegunka", "ból brzucha", "ból gardła", "ból głowy", "ból mięśni", 
        "ból stawów", "ból w klatce piersiowej", "duszności", "gorączka", "kaszel", 
        "nudności", "obrzęk kończyn", "zaburzenia nastroju", "zgaga", "zmęczenie", 
        "nagła zmiana masy ciała", "zmiany skórne", "choroba internistyczna?"]
        writer.writerow(header)

        grypa = Disease(False, False, True, True, True, True, False, False, True,
            True, False, False, False, False, True, False, False, True)
        angina = Disease(False, False, True, True, False, True, False, False, True,
            True, False, False, False, False, True, False, False, True)
        astma = Disease(False, False, False, False, False, False, True, True, False, 
            True, False, False, True, True, False, False, False, True )
        choroby_serca = Disease(False, False, False, False, False, False, True, True, 
            False, False, False, True, False, False, True, False, False, True)
        choroby_tarczycy = Disease(True, False, False, False, False, False, False, True, 
            False, False, False, False, True, False, True, True, False, True)
        choroby_pokarmowe = Disease(True, True, False, False, False, False, True, False, 
            False, False, True, False, False, True, False, True, False, True)
        choroby_krwi = Disease(False, True, False, True, False, True, False, True, True, 
            False, True, False, False, False, True, True, True, True)
        reumatyzm = Disease(False, False, False, False, False, True, False, False, False, 
            False, False, True, False, False, False, False, False, True)
        # inne chroby (żeby czasem były falsy)
        choroby_psychiczne = Disease(False, False, False, False, False, False, False, False, 
            False, False, True, False, True, False, True, True, False, False)
        alergie = Disease(False, True, False, False, False, False, False, True, False, True, 
            False, False, False, False, False, False, True, False)
        nowotwory = Disease(True, True, False, False, False, False, False, False, True, False, 
            False, False, False, True, True, True, True, False)
        diseases = [grypa, angina, astma, choroby_serca, choroby_tarczycy, choroby_pokarmowe,
            choroby_krwi, reumatyzm, choroby_psychiczne, alergie, nowotwory]
        for _ in range(rowsNumber):
            writer.writerow(diseases[random.randrange(0, len(diseases))].genRow())
        csvfile.close()