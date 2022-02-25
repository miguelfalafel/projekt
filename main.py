# import pandas as pd
# import os
#
# #data_path =  "C:\\Users\\micha\\Downloads\\20210215_Gminy_2_za_2020(1).xlsx"
# # def import_p_wojew(data_path):
# #     if os.path.exists(data_path):
# #         wojew_p_rok = pd.read_excel(data_path, usecols=[0,1,2,3,11], skiprows=list(range(6)), names = ['WK', 'PK', 'GK', 'GT', 'Dochody wykonane'], engine = 'openpyxl')
# #     else:
# #         return pd.DataFrame()
# #
# #     return wojew_p_rok
# #
# # zmienna = import_p_wojew(data_path)
# # print(zmienna)
#
# data_path = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210211_Powiaty_za_2020.xlsx"
# # def import_l(data_path):
# #     if os.path.exists(data_path):
# #         ludnosc = pd.read_excel(data_path, usecols=list(range(3)),  skiprows=list(range(7)), names = ["Nazwa", "id", "ludnosc"]) # wczytywanie pliku excel
# #     else:
# #         return pd.DataFrame()
# #     return ludnosc
# #
# # def import_lw(data_path):
# #     if os.path.exists(data_path):
# #         ludnosc = pd.read_excel(data_path, usecols=list(range(2)), skiprows=list(range(7)),  names = ["Nazwa",  "ludnosc"])
# #     else:
# #         return pd.DataFrame()
# #     # ludnosc = ludnosc_raw[:]
# #     return ludnosc[0:16,]
# #
# # print(import_lw(data_path))
#
# def import_p_wojew(data_path):
#     if os.path.exists(data_path):
#         wojew_p_rok = pd.read_excel(data_path, usecols=[0,4,11], skiprows=list(range(6)), names = ['id', 'Nazwa', 'Dochody wykonane'], engine = 'openpyxl', dtype={0: str, 1: str})
#     else:
#         return pd.DataFrame()
#     return wojew_p_rok
# # print(import_p_wojew(data_path))
#
# data_pathlpow = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\Ludnosc\\Tabela_III.xls"
#
# def import_lw(data_path):
#     if os.path.exists(data_path):
#         ludnosc = pd.read_excel(data_path, usecols=list(range(2)), skiprows=list(range(7)),  names = ["Nazwa",  "ludnosc"], dtype={0: str}, nrows= 16)
#         #dodanie WK
#         WK = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32']
#         ludnosc.insert(loc=0, column="WK", value=WK)
#     else:
#         return pd.DataFrame()
#     return ludnosc
# # print(import_lw(data_pathl))
#
# def import_lp(data_path):
#     if os.path.exists(data_path):
#         ludnosc = pd.read_excel(data_path, usecols=list(range(3)),  skiprows=list(range(7)), names = ["Nazwa", "id", "Ludnosc"], dtype={0: str, 1: str}).dropna(how='any')
#     else:
#         return pd.DataFrame()
#     return ludnosc
#
# # print(import_lp(data_pathl))
# data_path_powiaty = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210211_Powiaty_za_2020.xlsx"
# data_path_npp = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210215_Miasta_NPP_2_za_2020.xlsx"
# def import_p_powiat(data_path_pow, data_path_npp):
#     if os.path.exists(data_path_pow) and os.path.exists(data_path_npp):
#         # powiaty
#         powiaty_p_rok = pd.read_excel(data_path_pow, usecols=[0, 1, 4, 11], skiprows=list(range(6)),
#                                       names=['WK', 'PK', 'Nazwa', 'Dochody wykonane'], dtype={0: str, 1: str, 2: str},
#                                       engine='openpyxl').dropna(how='any')
#         # id
#         powiaty_p_rok.insert(0, 'id', powiaty_p_rok['WK'] + powiaty_p_rok['PK'])
#         powiaty_p_rok = powiaty_p_rok.drop(['WK', 'PK'], axis=1)
#
#         # npp
#         powiaty_npp_p_rok = pd.read_excel(data_path_npp, usecols=[0, 1, 4, 8, 11], skiprows=list(range(6)),
#                                           names=['WK', 'PK', 'Nazwa', 'Rozdział', 'Dochody wykonane'],
#                                           dtype={0: str, 1: str, 2: str},
#                                           engine='openpyxl').dropna(how='any')
#         # usuwanie rozdziału id=75622
#         powiaty_npp_p_rok.drop_duplicates(subset=["WK", "PK"], ignore_index=True, inplace=True)
#         powiaty_npp_p_rok.drop(labels="Rozdział", axis=1, inplace=True)
#         # id
#         powiaty_npp_p_rok.insert(0, 'id', powiaty_npp_p_rok['WK'] + powiaty_npp_p_rok['PK'])
#         powiaty_npp_p_rok = powiaty_npp_p_rok.drop(['WK', 'PK'], axis=1)
#
#         # łaćzenie obu
#         powiaty_p_rok_oba = pd.concat([powiaty_p_rok, powiaty_npp_p_rok], ignore_index=True)
#         powiaty_p_rok_oba = powiaty_p_rok_oba.sort_values(by=['id'], ignore_index=True)
#
#     else:
#         return pd.DataFrame()
#
#     return powiaty_p_rok_oba
# # print(import_p_powiat(data_path,data_path_npp))
# data_path_gminy = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210215_Gminy_2_za_2020.xlsx"
# data_path_gminy_l = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\Ludnosc\\Tabela_IV.xls"
# def import_p_gminy(data_path):
#     if os.path.exists(data_path):
#         gminy_p_rok = pd.read_excel(data_path, usecols=[0, 1, 2, 3, 4, 11], skiprows=list(range(6)),
#                                       names=['WK', 'PK', 'GK', 'GT', 'Nazwa', 'Dochody wykonane'], dtype={0: str, 1: str, 2: str, 3: str, 4: str},
#                                       engine='openpyxl').dropna(how='any')
#         # id
#         gminy_p_rok.insert(0, 'id', gminy_p_rok['WK'] + gminy_p_rok['PK']+ gminy_p_rok['GK']+ gminy_p_rok['GT'])
#         gminy_p_rok = gminy_p_rok.drop(['WK', 'PK', 'GK', 'GT'], axis=1)
#     else:
#         return pd.DataFrame()
#     return gminy_p_rok
# # print(import_p_gminy(data_path_gminy))
#
# def import_l_gmina(data_path):
#     if os.path.exists(data_path):
#         ludnosc = pd.read_excel(data_path, usecols=list(range(3)), skiprows=list(range(7)),
#                                 names=["Nazwa", "id", "Ludnosc"], dtype={0: str, 1: str}).dropna(how='any')
#     else:
#         return pd.DataFrame()
#     return ludnosc
# #tax
# t= 0.17
# #working percent
# wp = 0.55
# def avg_income(pity, ludnosc):
#     # #Zapobiegniecie zmian argumentow
#     # pity = pity.copy(deep=True)
#     # ludnosc = ludnosc.copy(deep=True)
#     pit = pity[['id', 'Dochody wykonane']].join(ludnosc.set_index('id'), on='id',how='left', sort=True)
#     pit['avg_income'] = pit['Dochody wykonane'] / (pit['Ludnosc'] * wp * t)
#     if pity.shape[0] != ludnosc.shape[0]:
#         print("Liczby JST w plikach różnią się")
#     return pit
#
# # print(avg_income(import_p_gminy(data_path_gminy),import_l_gmina(data_path_gminy_l)))
#
# def difference_pit(data2019, data2020):
#     data = data2020.join(data2019.set_index('id'), on='id', how='left', lsuffix=" 2020", rsuffix=" 2019", sort=True)
#     data['Różnica'] = data['Dochody wykonane 2020'] - data['Dochody wykonane 2019']
#     if data2019.shape[0] != data2020.shape[0]:
#         print("Liczby JST w plikach różnią się")
#     return data
# data_pow_2020 = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210211_Powiaty_za_2020.xlsx"
# data_pow_2019 = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2019\\20200214_Powiaty_za_2019.xlsx"
# data_2019 = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2019\\20200214_Gminy_za_2019.xlsx"
# data_2020 = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210215_Gminy_2_za_2020.xlsx"
# # print(difference_pit(import_p_gminy(data_pow_2019),import_p_gminy(data_pow_2020)))
# def import_l_powiat(data_path):
#     if os.path.exists(data_path):
#         ludnosc = pd.read_excel(data_path, usecols=list(range(3)), skiprows=list(range(7)), names=["Nazwa", "id", "Ludnosc"], dtype={0: str, 1: str}).dropna(how='any')
#     else:
#         return pd.DataFrame()
#     return ludnosc
#
# small = avg_income(import_p_gminy(data_2020),import_l_gmina(data_path_gminy_l))
# big = avg_income(import_p_powiat(data_pow_2020,data_path_npp),import_l_powiat(data_pathlpow))
# def var_income(small,big):
#     variance=[]
#     for i in list(big['id']):
#         variance.append(small[small.id.str.match(i)]['avg_income'].var())
#     result = big
#     result['variance'] = variance
#     result = result.dropna(how='any')
#     return result
#
# # print(var_income(small,big))
# def w_avg_inc(small,big):
#     suma_wazona=[]
#     small1=small
#     small1 = small1[-small1.id.str.match('......4')]
#     small1 = small1[-small1.id.str.match('......5')]
#     small1['waga'] =  small1['avg_income'] * small1['Ludnosc']
#     for i in list(big['id']):
#         suma_wazona.append(small1[small1.id.str.match(i)]['waga'].sum())
#     result = big
#     result['waz_avg_inc'] = suma_wazona / result['Ludnosc']
#     result = result[result.waz_avg_inc!=0]
#     return result
# # print(w_avg_inc(small,big))
# import numpy as np
# import matplotlib.pyplot as plot
# def bar(data, nazwa):
#     dane = data.sort_values(by=['avg_income'])
#     xy = len(dane['id'])
#     # y_pos = np.arange(len(data['average_income']))
#     plot.bar(x=np.arange(xy), height=dane['avg_income'], align='center')
#     if xy == 16:
#         labels = dane['Nazwa']
#         plot.xticks(np.arange(xy),labels, rotation='vertical')
#     plot.ylabel('Średni dochód')
#     plot.title(nazwa)
#     # fig = plt.gcf()
#     # fig.set_size_inches(10, 8)
#     plot.show()
#
# def import_l_wojew(data_path):
#     if os.path.exists(data_path):
#         ludnosc = pd.read_excel(data_path, usecols=list(range(2)), skiprows=list(range(7)),  names = ["Nazwa",  "Ludnosc"], dtype={0: str}, nrows= 16)
#         #dodanie WK
#         WK = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32']
#         ludnosc.insert(loc=0, column="id", value=WK)
#     else:
#         return pd.DataFrame()
#     return ludnosc
# data_wojew_p = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\pit2020\\20210211_Województwa_za_2020.xlsx"
# data_wojew_l = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data\\Ludnosc\\Tabela_II.xls"
# smallw = avg_income(import_p_wojew(data_wojew_p),import_l_wojew(data_wojew_l))
#
# # bar(smallw, "tytuł")
# def pie_diff(data, nazwa):
#         plot.pie(x=(data['Różnica'] > 0).value_counts())
#         plot.title(nazwa)
#         plot.legend(loc='lower center', labels=['Większe dochody w 2020', 'Większe dochody w 2019'])
#         plot.gcf().set_size_inches(8, 8)
#         plot.show()
#
# data_diff = difference_pit(import_p_gminy(data_2019),import_p_gminy(data_2020))
# # pie_diff(data_diff, "Nazwa")
#
# path = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data"
# def export_excel(df, path, nazwa):
#     df.to_excel(excel_writer=path + "\\" + nazwa + ".xlsx", engine="openpyxl")
#     return 0
#
# export_excel(w_avg_inc(small,big),path, "wavginc")
#
#%%

# %load_ext autoreload
# %autoreload 2

#%%

# Import potrzebnych paczek
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import pit_pl.pit_package as pit_p

#%%

#Ustalenie stałej ścieżki do danych i eksportu
path = "C:\\Users\\micha\\Desktop\\Śmiecie\\studia\\wężyk\\projekt\\data"

#Wgranie danych za PIT i Ludność
#PIT 2020
data_g_p_20 = pit_p.dane_import.import_gminy.import_p_gmina(path+ "\\pit2020\\20210215_Gminy_2_za_2020.xlsx")
data_p_p_20 = pit_p.dane_import.import_powiaty.import_p_powiat(path+ "\\pit2020\\20210211_Powiaty_za_2020.xlsx", path + "\\pit2020\\20210215_Miasta_NPP_2_za_2020.xlsx")
data_w_p_20 = pit_p.dane_import.import_wojew.import_p_wojew(path+ "\\pit2020\\20210211_Województwa_za_2020.xlsx")
#PIT 2019
data_g_p_19 = pit_p.dane_import.import_gminy.import_p_gmina(path+ "\\pit2019\\20200214_Gminy_za_2019.xlsx")
data_p_p_19 = pit_p.dane_import.import_powiaty.import_p_powiat(path+ "\\pit2019\\20200214_Powiaty_za_2019.xlsx", path + "\\pit2019\\20200214_Miasta_NPP_za_2019.xlsx")
data_w_p_19 = pit_p.dane_import.import_wojew.import_p_wojew(path+ "\\pit2019\\20200214_Wojewodztwa_za_2019.xlsx")
#Ludność 2020
data_g_l_20 = pit_p.dane_import.import_gminy.import_l_gmina(path + "\\Ludnosc\\Tabela_IV.xls")
data_p_l_20 = pit_p.dane_import.import_powiaty.import_l_powiat(path + "\\Ludnosc\\Tabela_III.xls")
data_w_l_20 = pit_p.dane_import.import_wojew.import_l_wojew(path + "\\Ludnosc\\Tabela_II.xls")



#%%

#Zaczynamy analizę
#Najpierw policzymy i zaprezentujemy na wykresach różnice w dochodach JST dla gmin, powiatów i województw,
#czyli odpowiemy na pytanie jaki odsetek JST z poszczególnych kategorii miał dochody większe w 2020, a jaki w  2019.
#Na koniec zapiszemy otrzymane arkusze do excela
diff_g = pit_p.analiza.difference_pit(data_g_p_19,data_g_p_20)
diff_p = pit_p.analiza.difference_pit(data_p_p_19,data_p_p_20)
diff_w = pit_p.analiza.difference_pit(data_w_p_19,data_w_p_20)

#%%

#wykresy
pit_p.analiza.charts.pie_diff(diff_g, "Różnice w gmiach")
pit_p.analiza.charts.pie_diff(diff_p, "Różnice w powiatach")
pit_p.analiza.charts.pie_diff(diff_w, "Różnice w województwach")

#%%

#zapisywanie do exceli
pit_p.dane_export.export_excel(diff_g, path, "Różnice gminy")
pit_p.dane_export.export_excel(diff_p, path, "Róznice powiaty")
pit_p.dane_export.export_excel(diff_w, path, "Róznice wojew")

#%%

#teraz policzmy średni dochód opodatkowany dla JST
#poniżej przedstawimy wykresy przentujące jak rozkładały się średnie dochody dla każdego z typów JST
#na koniec zapiszemy pliki do excela
#w obliczeniach przyjęto odsetek populacji, który pracuje jako 55%, a podatek dochodowy liniowe 17%
avg_inc_g = pit_p.analiza.avg_income(data_g_p_20,data_g_l_20)
avg_inc_p = pit_p.analiza.avg_income(data_p_p_20,data_p_l_20)
avg_inc_w = pit_p.analiza.avg_income(data_w_p_20,data_w_l_20)
#Wykresy
pit_p.analiza.charts.bar_avg(avg_inc_g, "Avg Income Gminy")
pit_p.analiza.charts.bar_avg(avg_inc_p, "Avg Income Powiaty")
pit_p.analiza.charts.bar_avg(avg_inc_w, "Avg Income Województwo")

#%%

#Zapisywanie do excela
pit_p.dane_export.export_excel(avg_inc_g, path, "Avg_Inc gminy")
pit_p.dane_export.export_excel(avg_inc_p, path, "Avg_Inc powiaty")
pit_p.dane_export.export_excel(avg_inc_w, path, "Avg_Inc wojew")

#%%

#Teraz policzmy wariancje dochodu w podległych JST, tj. dla odpowiednio powiatów i województw
var_p = pit_p.analiza.var_income(avg_inc_g,avg_inc_p)
var_w = pit_p.analiza.var_income(avg_inc_p,avg_inc_w)
#Zapisujemy do excela
pit_p.dane_export.export_excel(var_p, path, "Wariancja powiaty")
pit_p.dane_export.export_excel(var_w, path, "Wariancja województwa")

#%%

#Teraz policzymy średni dochód dla powiatów i województw, ważony odpowiednio ludnością w gminach i powiatach
#Pórwnanie z dochodem wyliczonym znajdziemy w arkuszach excela, któych eksport nastąpi poniżej
waz_avg_inc_p = pit_p.analiza.w_avg_inc(avg_inc_g,avg_inc_p)
waz_avg_inc_w = pit_p.analiza.w_avg_inc(avg_inc_p,avg_inc_w)
#Eksport do excela
pit_p.dane_export.export_excel(waz_avg_inc_p, path, "Ważone avg_inc powiaty")
pit_p.dane_export.export_excel(waz_avg_inc_w, path, "Ważone avg_inc województwa")

#%%


