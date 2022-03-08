import csv
def seek_data(reference, data_ref):
    data_date_matrix = []
    file_path = "DATOS PROCESADOS/GALICIA/" + reference + ".csv"
    with open(file_path, encoding="utf8", errors='ignore') as File:
        reader = csv.reader(File)
        for row in reader:
            data_date_matrix.append({row[0], row[data_ref]})

#seek_data('1351', 5)
