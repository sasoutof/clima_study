def seek_data(file_reference, data_ref):
    import csv
    data_date_matrix = []
    file_path = "/home/santiago/Documentos/CLIMATOLOGIA/ESTUDIO CLIMATICO/DATOS PROCESADOS/GALICIA/" + file_reference + ".csv"
    with open(file_path, encoding="utf8", errors='ignore') as File:
        reader = csv.reader(File)
        for row in reader:
            data_date_matrix.append([row[0], row[data_ref]])
    return data_date_matrix
def limits_data(data, upper_date):
    # recorre el array de datos en busca de la fecha que coincida con la seleccionada
    #y almacena el índice de la misma.
    for row in data:
        date = row[0]
        index = data.index(row)
        if date == upper_date:
            index_del = index
    #elimina todos los registros anteriores al indice de la fecha coincidente.
    for i in range(index_del):
        del data[0]
    limited_data = data
    return limited_data
def set_up_date(data):
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
def covariance_processing(station1_code, station2_code, date, measure = 5):
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
covariance_data = covariance_processing('1428', '1475X', '1995-01-01', 5)

for row in covariance_data:
    with open("datos_covarianza.csv", 'w') as f:
        csv_writer = csv.writer(f, delimiter =',')
        for row in covariance_data:
            csv_writer.writerow(row)

# #----------------------------------------------A Coruña aeropuerto--------------------------------------------------
# coruña_aeropuerto = seek_data('1387E', 5)
# debugged_coruña_aeropuerto = set_up_date(coruña_aeropuerto)
# limited_coruña_aeropuerto = limits_data(debugged_coruña_aeropuerto, '1995-01-01', 0)
# #----------------------------------------------A Coruña--------------------------------------------------
# coruña = seek_data('1387', 5)
# debugged_coruña = set_up_date(coruña)
# limited_debugged_coruña = limits_data(debugged_coruña, '1995-01-01', 0)
# # ----------------------------------------------Cabo Vilan--------------------------------------------------
# cabo_vilan = seek_data('1393', 5)
# debugged_cabo_vilan = set_up_date(cabo_vilan)
# limited_cabo_vilan = limits_data(debugged_cabo_vilan, '1995-01-01', 0)
# # ----------------------------------------------Estaca de Vares--------------------------------------------------
# estaca_vares = seek_data('1351', 5)
# debugged_estaca_vares = set_up_date(estaca_vares)
# limited_estaca_vares = limits_data(debugged_estaca_vares, '1995-01-01', 0)
# # ----------------------------------------------Fisterra--------------------------------------------------
# fisterra = seek_data('1400', 5)
# debugged_fisterra = set_up_date(fisterra)
# limited_fisterra = limits_data(debugged_fisterra, '1995-01-01', 0)
# # ----------------------------------------------Santiago De Compostela--------------------------------------------------
# sdc = seek_data('1428', 5)
# debugged_sdc = set_up_date(sdc)
# limited_sdc = limits_data(debugged_sdc, '1995-01-01', 0)
# #----------------------------------------------Santiago De Compostela airport--------------------------------------------------
# sdc_airport = seek_data('1475X', 5)
# debugged_sdc_airport = set_up_date(sdc_airport)
# limited_sdc_airport = limits_data(debugged_sdc_airport, '1995-01-01', 0)
# #----------------------------------------------Padron--------------------------------------------------
# padron = seek_data('1473A', 5)
# debugged_padron = set_up_date(padron)
# limited_padron = limits_data(debugged_padron, '1995-01-01', 0)
# #----------------------------------------------Iroite--------------------------------------------------
# iroite = seek_data('1437O', 5)
# debugged_iroite = set_up_date(iroite)
# limited_iroite = limits_data(debugged_iroite, '1995-01-01', 0)
#
# for row in limited_coruña_aeropuerto:
#     with open("coruña_aeropuerto.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter =',')
#         for row in limited_coruña_aeropuerto:
#             csv_writer.writerow(row)
#
# # for row in limited_debugged_coruña:
# #     with open("coruña.csv", 'w') as f:
# #         csv_writer = csv.writer(f, delimiter =',')
# #         for row in limited_debugged_coruña:
#             csv_writer.writerow(row)
#
# for row in limited_cabo_vilan:
#     with open("cabo_vilan.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter =',')
#         for row in limited_cabo_vilan:
#             csv_writer.writerow(row)
#
# for row in limited_estaca_vares:
#     with open("esta_vares.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter =',')
#         for row in limited_estaca_vares:
#             csv_writer.writerow(row)
#
# for row in limited_fisterra:
#     with open("fisterra.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter =',')
#         for row in limited_fisterra:
#             csv_writer.writerow(row)
#
# for row in limited_sdc:
#     with open("sdc.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter =',')
#         for row in limited_sdc:
#             csv_writer.writerow(row)
#
# for row in limited_sdc_airport:
#     with open("sdc_airport.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter=',')
#         for row in limited_sdc_airport:
#             csv_writer.writerow(row)
#
# for row in limited_padron:
#     with open("padron.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter=',')
#         for row in limited_padron:
#             csv_writer.writerow(row)
#
# for row in limited_iroite:
#     with open("iroite.csv", 'w') as f:
#         csv_writer = csv.writer(f, delimiter=',')
#         for row in limited_iroite:
#             csv_writer.writerow(row)

# ATBB9JNXgQ9erPTWEyLNVhnJ8YNm4217D133