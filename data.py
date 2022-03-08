import csv

class data:

    def __init__(self, station,data_type):
        self.station = station
        self.data_type = data_type
        self.stations_dictionary = {}

        self.data = []
        self.year_matrix = ['1993', '1992', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
                       '2004', '2005', '2006', '2007', '2008',
                       '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                       '2021', '2022']
    def fill_stations_dictionary(self):
        #CREA UN DICCIONARIO CON LA REFERENCIA DE CADA ESTACION Y SU DENOMINACION
        def execute(self):
            with open("ListadoEstaciones-20220206.csv", newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    self.stations_dictionary[row[0]] = row[2]
            return self.stations_dictionary
        return execute
    def obtain_data(self):
        file_path = "DATOS PROCESADOS/GALICIA/" + self.station + ".csv"
        with open(file_path, encoding="utf8", errors='ignore') as File:
            reader = csv.reader(File)
            #Se selecciona estudio de temperatura media
            if self.data_type == 0: colum = 5
            if self.data_type == 1: colum = 9
            if self.data_type == 2: colum = 6
            if self.data_type == 3: colum = 16
            for row in reader:
                    self.data.append({row[colum],row[0]})

    @fill_stations_dictionary
    def get_stations_dictionary(self): return self.stations_dictionary
    def get_data(self):return self.data

T_Media = data('1387E',0)
T_Max = data('1387E',1)
T_Max.obtain_data()
T_Media.obtain_data()
print(T_Max.get_data())
print(T_Media.get_data())