#eksport plików do excela
def export_excel(df, path, nazwa):
    df.to_excel(excel_writer=path + "\\" + nazwa + ".xlsx", engine="openpyxl")
    return 0