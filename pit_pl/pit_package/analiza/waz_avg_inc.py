
def w_avg_inc(small,big):
    suma_wazona=[]
    small1=small
    #usunięcie gmin, gdzie jest podwójnie liczona ludność - przypadek gmin M-W
    small1 = small1[-small1.id.str.match('......4')]
    small1 = small1[-small1.id.str.match('......5')]
    small1['waga'] =  small1['avg_income'] * small1['Ludnosc']
    for i in list(big['id']):
        suma_wazona.append(small1[small1.id.str.match(i)]['waga'].sum())
    result = big
    result['waz_avg_inc'] = suma_wazona / result['Ludnosc']
    #usunięcie pustych wartości (powstałych dla M NPP)
    result = result[result.waz_avg_inc!=0]
    return result