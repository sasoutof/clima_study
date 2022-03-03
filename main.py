import csv

#TMEDIA[5] TMAX[9] PRECIPITACION[6] TIEMPOSOL[15]
years = []
temperatures = []
date = []
year_matrix = ['1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008',
               '2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
temperatura = 20
column = 5

with open("ESTUDIO_TEMPERATURAS/SANTIAGO_AEROPUERTO.csv", newline='') as File:

    reader = csv.reader(File)
    for row in reader:
        if float(row[column]) >= temperatura:
            temperatures.append(row[column])
            date.append(row[0])

    for d in date:
        year = d.split('-')
        years.append(year[0])

for a in year_matrix:
    c = years.count(a)
    print('Año ' + a + ': ' + str(c) + ' días con temperatura media superior a ' + str(temperatura) + ' ºC')