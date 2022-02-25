import pandas as pd
from pit_pl.pit_package.analiza import avg_income, difference_pit, var_income, w_avg_inc


def test_avg_inc():
    # testowanie funkcji liczącej średni dochód, wp =0.55 r = 0.17
    # dane
    test_p = pd.DataFrame({'id': ['02', '04'], 'Nazwa': ['WojewX', 'WojewY'], 'Dochody wykonane': [1000, 1500]})
    test_l = pd.DataFrame({'id': ['02', '04'], 'Nazwa': ['WojewX', 'WojewY'], 'Ludnosc': [100, 100]})
    wynik = pd.DataFrame({'id': ['02', '04'], 'Dochody wykonane': [1000, 1500], 'Nazwa': ['WojewX', 'WojewY'], 'Ludnosc': [100, 100], 'avg_income': [1000 / (100 * 0.55 * 0.17), 1500 / (100 * 0.55 * 0.17)]})
    # Test
    pd.testing.assert_frame_equal(avg_income(test_p, test_l), wynik)

def test_waz_avg():
    # Testowanie funkcji o ważonym śrendim dochodzie w jednostce większej (big)
    # dane
    test_big = pd.DataFrame({'id': ['02'], 'Dochody wykonane': [1000], 'Nazwa': ['WojewX'], 'Ludnosc': [100], 'avg_income': [100]})
    test_small = pd.DataFrame({'id': ['0201,0202'], 'Dochody wykonane': [800, 200], 'Nazwa': ['PowX, PowY'], 'Ludnosc': [50, 50], 'avg_income': [100, 150] })
    wynik = pd.DataFrame({'id': ['02'], 'Dochody wykonane': [1000], 'Nazwa': ['WojewX'], 'Ludnosc': [100], 'avg_income': [100], 'variance': [300], 'waz_avg_inc': [150] })
    # test
    pd.testing.assert_frame_equal(w_avg_inc(test_small, test_big), wynik)

def test_var():
    # Testowanie funkcji o wariancji dochodu w jednostakch mniejszych (small) wchodzących w skłąd jednostki większej (big)
    # dane
    test_big = pd.DataFrame({'id': ['02'], 'Dochody wykonane': [1000], 'Nazwa': ['WojewX'], 'Ludnosc': [100], 'avg_income': [100]})
    test_small = pd.DataFrame({'id': ['0201,0202'], 'Dochody wykonane': [800, 200], 'Nazwa': ['PowX, PowY'], 'Ludnosc': [50, 50], 'avg_income': [100, 150]})
    wynik = pd.DataFrame({'id': ['02'], 'Dochody wykonane': [1000], 'Nazwa': ['WojewX'], 'Ludnosc': [100], 'avg_income': [100], 'variance': [300]})
    # test
    pd.testing.assert_frame_equal(var_income(test_small, test_big), wynik)

def test_diff():
    # testowanie funkcji liczącej różnice dochodu w tych smaych JST w różnych latach
    # dane
    test_19 = pd.DataFrame({'id': ['02', '04'], 'Nazwa': ['WojewX', 'WojewY'], 'Dochody wykonane': [1000, 1500]})
    test_20 = pd.DataFrame({'id': ['02', '04'], 'Nazwa': ['WojewX', 'WojewY'], 'Dochody wykonane': [1200, 1300]})
    wynik = pd.DataFrame({'id': ['02', '04'], 'Nazwa 2020': ['WojewX', 'WojewY'], 'Dochody wykonane 2020': [1200, 1300],
                          'Nazwa 2019': ['WojewX', 'WojewY'], 'Dochody wykonane 2019': [1000, 1500], 'Różnica': [200, -200]})
    # Test
    pd.testing.assert_frame_equal(difference_pit(test_19, test_20), wynik)
