import pandas as pd
import os

def import_l_gmina(data_path):
    if os.path.exists(data_path):
        ludnosc = pd.read_excel(data_path, usecols=list(range(3)), skiprows=list(range(7)),
                                names=["Nazwa", "id", "Ludnosc"], dtype={0: str, 1: str}).dropna(how='any')
    else:
        return pd.DataFrame()
    return ludnosc


def import_p_gmina(data_path):
    if os.path.exists(data_path):
        gminy_p_rok = pd.read_excel(data_path, usecols=[0, 1, 2, 3, 4, 11], skiprows=list(range(6)),
                                      names=['WK', 'PK', 'GK', 'GT', 'Nazwa', 'Dochody wykonane'], dtype={0: str, 1: str, 2: str, 3: str, 4: str},
                                      engine='openpyxl').dropna(how='any')
        # id
        gminy_p_rok.insert(0, 'id', gminy_p_rok['WK'] + gminy_p_rok['PK']+ gminy_p_rok['GK']+ gminy_p_rok['GT'])
        gminy_p_rok = gminy_p_rok.drop(['WK', 'PK', 'GK', 'GT'], axis=1)
    else:
        return pd.DataFrame()
    return gminy_p_rok