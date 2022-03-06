import csv

class data:

    def __init__(self, station, data_type, data_type_study):
        self.station = station
        self.data_type = data_type
        self.stations_dictionary = {}
        self.data_type_study = data_type_study
        year_matrix = ['1993', '1992', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
                       '2004', '2005', '2006', '2007', '2008',
                       '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                       '2021', '2022']


    def fill_stations_dictionary(self):
        def execute(self):
            with open("ListadoEstaciones-20220206.csv", newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    self.stations_dictionary[row[0]] = row[2]
            return self.stations_dictionary
        return execute
    def date_data(self):
        def execute(self):
            with open("ListadoEstaciones-20220206.csv", newline='') as File:
                reader = csv.reader(File)
        return execute
    @fill_stations_dictionary
    def data_type_study(self):
        print("")
    @fill_stations_dictionary
    def get_stations_dictionary(self): return self.stations_dictionary

    def set_temperature(self, temperature): self.temperature = temperature

a = data('1387E',1,2)

class file_modify():

print(a)
print(a.get_stations_dictionary())