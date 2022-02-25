import pandas as pd
from pit_pl.pit_package.dane_import import import_l_gmina, import_p_gmina, import_p_powiat, import_l_powiat, import_p_wojew,  import_l_wojew

def test_import_p():
    #testowanie, czy odczytana zosatnie zła ścieżka (pliki nie xlsx) przy czytaniu PITów
    pd.testing.assert_frame_equal(import_p_gmina("ścieżka.xlxx"), pd.DataFrame())
    pd.testing.assert_frame_equal(import_p_powiat("ścieżka.xlxx","ścieżka.xlxx"), pd.DataFrame())
    pd.testing.assert_frame_equal(import_p_wojew("ścieżka.xlxx"), pd.DataFrame())

def test_import_l():
    #testowanie, czy odczytana zosatnie zła ścieżka (pliki nie xlsx) przy czytaniu Ludności
    pd.testing.assert_frame_equal(import_l_gmina("ścieżka.xlxx"), pd.DataFrame())
    pd.testing.assert_frame_equal(import_l_powiat("ścieżka.xlxx"), pd.DataFrame())
    pd.testing.assert_frame_equal(import_l_wojew("ścieżka.xlxx"), pd.DataFrame())