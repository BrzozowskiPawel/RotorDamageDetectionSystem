class DataSet():
    def __init__(self):
        self.data_from_csv = []
        self.datachunks = None

    # SETTERS
    def set_data_from_csv(self, data):
        self.data_from_csv.append(data)

    def set_datachunks(self, data):
        self.datachunks = data

    # GETTERS

    def get_data_from_csv(self):
        return self.data_from_csv
