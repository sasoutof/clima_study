import csv
import re
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

class data:

    def __init__(self, station, data_type):
        self.station = station
        self.data_type = data_type
        self.stations_dictionary = {}
        self.data = []
        self.data_out = []
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
            for row in reader:self.data.append([row[colum],row[0]])
    def analyze_data(self, type_of_analyze, valor):
        self.type_of_analyze = type_of_analyze
        self.valor = valor
        if self.type_of_analyze == 0:
            for row in self.data:
                #print(re.findall("[^0123456789.]", str(row[0])))
                if self.valor <= float(row[0]):
                    self.data_out.append(row[0])
    def draw_data(self):
        x_data_array = 0
        y_data_array = 0
        for row in self.data:
            # x_data_array = np.append(x_data_array, float(row[1]))
            y_data_array = np.append(y_data_array, float(row[0]))
        y_data = pd.Series(y_data_array)
        fig, axes = plt.subplots()
        y_data.plot(ax=axes[0], kind='bar', title='bar')
        plt.show()
        # min = np.amin(y_data_array)
        # max = np.amax(y_data_array)

        # len = y_data_array.size

        # y_axis = np.array(y_data_array)
        # x_axis = np.linspace(1,len,len)
        # print(len)
        # print(y_axis.size)
        # print(x_axis.size)
        # print(x_axis[5800])
        # fig, ax = plt.subplots()
        # ax.stem(x_axis, y_axis)
        # ax.set(xlim=(0, maxpicadura de la cobra gay pato bailando), xticks=np.arange(1, max),
        #         ylim=(0, len), yticks=np.arange(1, len))
        # plt.show()

    @fill_stations_dictionary
    def get_stations_dictionary(self): return self.stations_dictionary
    def get_data(self):return self.data
    def get_data_out(self):return self.data_out

t_max_1351 = data('1351',0)
t_max_1387 = data('1387',0)
t_max_1387E = data('1387E',0)
t_max_1393 = data('1393',0)
t_max_1400 = data('1400',0)

t_max_1351.obtain_data()
t_max_1387.obtain_data()
t_max_1387E.obtain_data()
t_max_1393.obtain_data()
t_max_1400.obtain_data()

t_max_1351.analyze_data(0,21)
t_max_1387.analyze_data(0,21)
t_max_1387E.analyze_data(0,21)
t_max_1393.analyze_data(0,21)
t_max_1400.analyze_data(0,21)


print(t_max_1351.get_data())
print(t_max_1387.get_data())
print(t_max_1387E.get_data())
print(t_max_1393.get_data())
print(t_max_1400.get_data())
t_max_1393.draw_data()