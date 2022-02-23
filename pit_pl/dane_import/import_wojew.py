import pandas as pd
import os

def import_l_wojew(data_path):
    if os.path.exists(data_path):
        ludnosc = pd.read_excel(data_path, usecols=list(range(2)), skiprows=list(range(7)),  names = ["Nazwa",  "Ludnosc"], dtype={0: str}, nrows= 16)
        #dodanie WK
        WK = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32']
        ludnosc.insert(loc=0, column="WK", value=WK)
    else:
        return pd.DataFrame()
    return ludnosc


def import_p_wojew(data_path):
    if os.path.exists(data_path):
        wojew_p_rok = pd.read_excel(data_path, usecols=[0,4,11], skiprows=list(range(6)), names = ['WK', 'Nazwa', 'Dochody wykonane'], engine = 'openpyxl', dtype={0: str, 1: str})
    else:
        return pd.DataFrame()
    return wojew_p_rok