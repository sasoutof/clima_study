def seek_data(file_reference, data_ref):
    #esta función se encarga de localizar el archivo solicitado y guardar un array
    #con los datos indicados en 'data_ref'
    import csv
    data_date_matrix = []
    file_path = "/home/santiago/Documentos/CLIMATOLOGIA/ESTUDIO CLIMATICO/DATOS PROCESADOS/GALICIA/" + file_reference + ".csv"
    with open(file_path, encoding="utf8", errors='ignore') as File:
        reader = csv.reader(File)
        for row in reader:
            data_date_matrix.append([row[0], row[data_ref]])
    return data_date_matrix

def limits_data(data, upper_date, lower_date):
    #recorre el array de datos en busca de la fecha que coincida con la seleccionada y almacena el índice de la misma.
    #en este bucle recorre todo el array de datos y localiza el indice de la fecha indicada
    #para posteriormente eliminar todos los registros anteriores a ese indice
    for row in data:
        date = row[0]
        index = data.index(row)
        if date == upper_date:
            upper_index_del = index
    # #elimina todos los registros anteriores al indice de la fecha coincidente.
    for i in range(upper_index_del):
        del data[0]
    #se hace el mismo procedimiento que en el caso anterior pero para localizar el indice de la fecha inferior
    #con el nuevo array en el cual ya se han eliminado las fechas anteriores.
    for row in data:
        date = row[0]
        index = data.index(row)
        if date == lower_date:
            lower_index_del = index
    limited_data = []
    #cogemos los datos que nos interesan y los guardamos ene l array definitivo
    for i in range(0, lower_index_del + 1):
        limited_data.append(data[i])
    return limited_data

def set_up_date(data):
    # los arrays que cogemos de las bbdd muchas veces vienen sin alguna fecha
    # esta función rellena esas fechas que faltan y como valor para esa fecha pone cero
    import pandas as pd
    data_len = len(data) - 1
    initial_date = data[1][0]
    final_date = data[data_len][0]
    date_hour_array = pd.date_range(start = initial_date, end = final_date, freq = 'D')
    date = []
    for date_hour in date_hour_array:
        date_str = str(date_hour)
        # date.append(date_str[0:10])
        date.extend([[date_str[0:10], '']])
    for date_hour_data in data:
        index = data.index(date_hour_data) - 1
        xdate = date_hour_data[0]
        xdata = date_hour_data[1]
        if xdata != '' and xdata != 'FECHA' and xdata != 'TMEDIA':
            station_date = date[index][0]
            # station_data = date[index][1]
            if xdate == station_date:
                date[index][1] = xdata
            else:
                while xdate != station_date:
                    index = index + 1
                    station_date = date[index][0]
                date[index][1] = xdata
    debugged_data = date
    return debugged_data

def fill_data_gaps(station_code, station_2_code, date, measure = 5):
    import csv
    # En esta funcion rellenamos los datos vacios con datos de otra estacion
    data_station = seek_data(station_code, measure)
    debugged_data_station = set_up_date(data_station)
    limited_data_station = limits_data(debugged_data_station, date)
    file_path = "/home/santiago/Documentos/CLIMATOLOGIA/ESTUDIO CLIMATICO/DATOS PROCESADOS/GALICIA/" + '/' + station_2_code + ".csv"
    # En primer lugar lugar cambiamos las celdas con '0' por ''
    for data in limited_data_station:
        if data[1] == '0':
            limited_data_station[limited_data_station.index(data)][1] = ''
    # Rellena las celdas vacias con datos de otras estaciones
    for data in limited_data_station:
        if data[1] == '':
            date_to_seek = data[0]
            with open(file_path, newline = '', encoding = 'utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
                for row in reader:
                    if date_to_seek == row[0]:
                        data_to_gap = row[1]
            index = limited_data_station.index(data)
            limited_data_station[index][1] = data_to_gap
    return limited_data_station

def covariance_processing(station1_code, station2_code, date, measure = 5):
    # Esta función prerara los datos para poder calcular la covarianza entre 2 estaciones
    data_station_1 = seek_data(station1_code, measure)
    data_station_2 = seek_data(station2_code, measure)
    debugged_data_station_1 = set_up_date(data_station_1)
    debugged_data_station_2 = set_up_date(data_station_2)
    limited_data_station_1 = limits_data(debugged_data_station_1, date)
    limited_data_station_2 = limits_data(debugged_data_station_2, date)
    data_array = []
    for i in range(len(limited_data_station_1)):
        if limited_data_station_1[i][1] != '' and limited_data_station_2[i][1] != '':
            data_array.append([limited_data_station_1[i][0], limited_data_station_1[i][1], limited_data_station_2[i][1]])
    return data_array

import csv
# covariance_data = covariance_processing('1475X', '1428', '1995-01-01', 5)

# for row in covariance_data:
#     with open("datos_covarianza.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter =',')
#         for row in covariance_data:
#             csv_writer.writerow(row)

#----------------------------------------------A Coruña aeropuerto--------------------------------------------------
# coruña_aeropuerto = seek_data('1387E', 5)
# debugged_coruña_aeropuerto = set_up_date(coruña_aeropuerto)
# limited_coruña_aeropuerto = limits_data(debugged_coruña_aeropuerto, '1975-01-01')
# final_data_coruna_aeropuerto = fill_data_gaps('1351', '1475X', '1975-01-01')

#----------------------------------------------Santiago De Compostela airport--------------------------------------------------
# sdc_airport = seek_data('1428', 5)
# debugged_sdc_airport = set_up_date(sdc_airport)
# limited_sdc_airport = limits_data(debugged_sdc_airport, '1995-01-01')
# final_data_santiago_aeropuerto = fill_data_gaps('1351', '1475X', '1975-01-01')

# #----------------------------------------------Pontevedra (Instituto)--------------------------------------------------
# pontevedra = seek_data('1484', 5)
# debugged_pontevedra = set_up_date(pontevedra)
# limited_pontevedra = limits_data(debugged_pontevedra, '1995-01-01')
#
# for row in final_data_coruna_aeropuerto:
#     with open("coruña_aeropuerto.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter =',')
#         for row in final_data_coruna_aeropuerto:
#             csv_writer.writerow(row)
#
# for row in limited_sdc_airport:
#     with open("sdc_airport.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter=',')
#         for row in limited_sdc_airport:
#             csv_writer.writerow(row)

# Oetn4SoF9yfiZ0n5aBBg

