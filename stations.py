import csv
class stations_file:
    def __init__(self):
        self.stations_dictionary = {}

    def fill_stations_dictionary(self):
        def execute(self):
            with open("ListadoEstaciones-20220206.csv", newline='') as File:
                reader = csv.reader(File)
                for row in reader:
                    self.stations_dictionary[row[0]] = row[3]
            return self.stations_dictionary
        return execute

    @fill_stations_dictionary
    def get_sations_dictionary(self): return self.stations_dictionary

