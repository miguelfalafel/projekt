#tax
t= 0.17
#working percent
wp = 0.55
def avg_income(pity, ludnosc):
    #łączenie w jedną tabele
    pit = pity[['id', 'Dochody wykonane']].join(ludnosc.set_index('id'), on='id', how='left', sort=True)
    pit['avg_income'] = pit['Dochody wykonane'] / (pit['Ludnosc'] * wp * t)
    if pity.shape[0] != ludnosc.shape[0]:
        print("Liczby JST w plikach różnią się")
    return pit