import merge_function


class DataSet():
    def __init__(self):
        self.data_from_csv = []
        # self.data_chunks = None
        self.merged_chunks = []

    # SETTERS
    def set_data_from_csv(self, data):
        self.data_from_csv.append(data)

    # def set_data_chunks(self, data):
    #     self.data_chunks = data

    def set_merged_chunks(self):
        tmp = merge_function.merge_into_one_list(self.data_from_csv)
        self.merged_chunks.append(tmp)

    # GETTERS

    def get_data_from_csv(self):
        return self.data_from_csv

    # def get_data_chunks(self):
    #     return self.data_chunks

    def get_merged_chunks(self):
        return self.merged_chunks
