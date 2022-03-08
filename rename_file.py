import os

filepath = "DATOS PROCESADOS/"

for file in os.listdir(filepath):
    if os.path.isfile(os.path.join(filepath,file)) == True:
        station_reference = file.split('-')
        new_name = station_reference[0] + '.csv'
        os.rename(os.path.join(filepath, file), os.path.join(filepath, new_name))
        os.close()



