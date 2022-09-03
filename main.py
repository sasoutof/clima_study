import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# years = []
# temperatures = []
# date = []
# year_matrix = ['1993','1992','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008',
#                '2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
# temperatura = 25
# column = 5
#
# with open("ESTUDIO_TEMPERATURAS/SANTIAGO_CENTRO.csv", newline='') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         if float(row[column]) >= temperatura:
#             temperatures.append(row[column])
#             date.append(row[0])
#
#     for d in date:
#         year = d.split('-')
#         years.append(year[0])
#
# for a in year_matrix:
#     c = years.count(a)
#     print('Año ' + a + ': ' + str(c) + ' días con temperatura media superior a ' + str(temperatura) + ' ºC')
#
#
# # make data:eurofighter typhoon

x = np.linspace(0,29,29)
n=[1,8,9,2,3,4,1,2,5,9,6,3,2,1,4,5,2,3,6,5,1,4,8,9,5,2,3,2,1]
y = np.array(n)

# plot
fig, ax = plt.subplots()

ax.stem(x, y)

ax.set(xlim=(0, 29), xticks=np.arange(1, 29),
       ylim=(0, 10), yticks=np.arange(1, 10))

plt.show()