#eksport plików do excela
def export_excel(df, path):
    df.to_excel(excel_writer=path + "/" + df.name + ".xlsx", engine="openpyxl")
    return 0