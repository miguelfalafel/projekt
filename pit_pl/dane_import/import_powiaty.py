import pandas as pd
import os

def import_l_powiat(data_path):
    if os.path.exists(data_path):
        ludnosc = pd.read_excel(data_path, usecols=list(range(3)), skiprows=list(range(7)), names=["Nazwa", "id", "Ludnosc"], dtype={0: str, 1: str}).dropna(how='any')
    else:
        return pd.DataFrame()
    return ludnosc


def import_p_powiat(data_path_pow, data_path_npp):
    if os.path.exists(data_path_pow) and os.path.exists(data_path_npp) :
        #powiaty
        powiaty_p_rok = pd.read_excel(data_path_pow, usecols=[0, 1, 4, 11], skiprows=list(range(6)),
                                      names=['WK', 'PK', 'Nazwa', 'Dochody wykonane'], dtype={0: str, 1: str, 2: str},
                                      engine='openpyxl').dropna(how='any')
        # id
        powiaty_p_rok.insert(0, 'id', powiaty_p_rok['WK'] + powiaty_p_rok['PK'])
        powiaty_p_rok = powiaty_p_rok.drop(['WK', 'PK'], axis=1)

        #npp
        powiaty_npp_p_rok = pd.read_excel(data_path_npp, usecols=[0, 1, 4,8,  11], skiprows=list(range(6)),
                                      names=['WK', 'PK', 'Nazwa', 'Rozdział', 'Dochody wykonane'], dtype={0: str, 1: str, 2: str},
                                      engine='openpyxl').dropna(how='any')
        #usuwanie rozdziału id=75622
        powiaty_npp_p_rok.drop_duplicates(subset=["WK", "PK"], ignore_index=True, inplace=True)
        powiaty_npp_p_rok.drop(labels="Rozdział", axis=1, inplace=True)
        #id
        powiaty_npp_p_rok.insert(0, 'id', powiaty_npp_p_rok['WK'] + powiaty_npp_p_rok['PK'])
        powiaty_npp_p_rok = powiaty_npp_p_rok.drop(['WK', 'PK'], axis=1)

        #łączenie obu
        powiaty_p_rok_oba = pd.concat([powiaty_p_rok, powiaty_npp_p_rok], ignore_index=True)
        powiaty_p_rok_oba = powiaty_p_rok_oba.sort_values(by=['id'], ignore_index=True)

    else:
        return pd.DataFrame()

    return powiaty_p_rok_oba