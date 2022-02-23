import pandas as pd
import os

#data_path =  "C:\\Users\\micha\\Downloads\\20210215_Gminy_2_za_2020(1).xlsx"
# def import_p_wojew(data_path):
#     if os.path.exists(data_path):
#         wojew_p_rok = pd.read_excel(data_path, usecols=[0,1,2,3,11], skiprows=list(range(6)), names = ['WK', 'PK', 'GK', 'GT', 'Dochody wykonane'], engine = 'openpyxl')
#     else:
#         return pd.DataFrame()
#
#     return wojew_p_rok
#
# zmienna = import_p_wojew(data_path)
# print(zmienna)

data_path = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210211_Powiaty_za_2020.xlsx"
# def import_l(data_path):
#     if os.path.exists(data_path):
#         ludnosc = pd.read_excel(data_path, usecols=list(range(3)),  skiprows=list(range(7)), names = ["Nazwa", "id", "ludnosc"]) # wczytywanie pliku excel
#     else:
#         return pd.DataFrame()
#     return ludnosc
#
# def import_lw(data_path):
#     if os.path.exists(data_path):
#         ludnosc = pd.read_excel(data_path, usecols=list(range(2)), skiprows=list(range(7)),  names = ["Nazwa",  "ludnosc"])
#     else:
#         return pd.DataFrame()
#     # ludnosc = ludnosc_raw[:]
#     return ludnosc[0:16,]
#
# print(import_lw(data_path))

def import_p_wojew(data_path):
    if os.path.exists(data_path):
        wojew_p_rok = pd.read_excel(data_path, usecols=[0,4,11], skiprows=list(range(6)), names = ['WK', 'Nazwa', 'Dochody wykonane'], engine = 'openpyxl', dtype={0: str, 1: str})
    else:
        return pd.DataFrame()

    return wojew_p_rok
# print(import_p_wojew(data_path))

data_pathlpow = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\Ludnosc\\Tabela_III.xls"

def import_lw(data_path):
    if os.path.exists(data_path):
        ludnosc = pd.read_excel(data_path, usecols=list(range(2)), skiprows=list(range(7)),  names = ["Nazwa",  "ludnosc"], dtype={0: str}, nrows= 16)
        #dodanie WK
        WK = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32']
        ludnosc.insert(loc=0, column="WK", value=WK)
    else:
        return pd.DataFrame()
    return ludnosc
# print(import_lw(data_pathl))

def import_lp(data_path):
    if os.path.exists(data_path):
        ludnosc = pd.read_excel(data_path, usecols=list(range(3)),  skiprows=list(range(7)), names = ["Nazwa", "id", "Ludnosc"], dtype={0: str, 1: str}).dropna(how='any')
    else:
        return pd.DataFrame()
    return ludnosc

# print(import_lp(data_pathl))
data_path_powiaty = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210211_Powiaty_za_2020.xlsx"
data_path_npp = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210215_Miasta_NPP_2_za_2020.xlsx"
def import_p_powiat(data_path_pow, data_path_npp):
    if os.path.exists(data_path_pow) and os.path.exists(data_path_npp):
        # powiaty
        powiaty_p_rok = pd.read_excel(data_path_pow, usecols=[0, 1, 4, 11], skiprows=list(range(6)),
                                      names=['WK', 'PK', 'Nazwa', 'Dochody wykonane'], dtype={0: str, 1: str, 2: str},
                                      engine='openpyxl').dropna(how='any')
        # id
        powiaty_p_rok.insert(0, 'id', powiaty_p_rok['WK'] + powiaty_p_rok['PK'])
        powiaty_p_rok = powiaty_p_rok.drop(['WK', 'PK'], axis=1)

        # npp
        powiaty_npp_p_rok = pd.read_excel(data_path_npp, usecols=[0, 1, 4, 8, 11], skiprows=list(range(6)),
                                          names=['WK', 'PK', 'Nazwa', 'Rozdział', 'Dochody wykonane'],
                                          dtype={0: str, 1: str, 2: str},
                                          engine='openpyxl').dropna(how='any')
        # usuwanie rozdziału id=75622
        powiaty_npp_p_rok.drop_duplicates(subset=["WK", "PK"], ignore_index=True, inplace=True)
        powiaty_npp_p_rok.drop(labels="Rozdział", axis=1, inplace=True)
        # id
        powiaty_npp_p_rok.insert(0, 'id', powiaty_npp_p_rok['WK'] + powiaty_npp_p_rok['PK'])
        powiaty_npp_p_rok = powiaty_npp_p_rok.drop(['WK', 'PK'], axis=1)

        # łaćzenie obu
        powiaty_p_rok_oba = pd.concat([powiaty_p_rok, powiaty_npp_p_rok], ignore_index=True)
        powiaty_p_rok_oba = powiaty_p_rok_oba.sort_values(by=['id'], ignore_index=True)

    else:
        return pd.DataFrame()

    return powiaty_p_rok_oba
# print(import_p_powiat(data_path,data_path_npp))
data_path_gminy = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210215_Gminy_2_za_2020.xlsx"

def import_p_gminy(data_path):
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
print(import_p_gminy(data_path_gminy))