#liczymy róznice między dochodami wykonanymi dla JST za 2019 i 2020
def difference_pit(data2019, data2020):
    #łączenie w jedną tabele
    data = data2020.join(data2019.set_index('id'), on='id', how='left', lsuffix=" 2020", rsuffix=" 2019", sort=True)
    data['Różnica'] = data['Dochody wykonane 2020'] - data['Dochody wykonane 2019']
    if data2019.shape[0] != data2020.shape[0]:
        print("Liczby JST w plikach różnią się")
    return data