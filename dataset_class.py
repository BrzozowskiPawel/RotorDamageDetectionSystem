
class Dataset:
    def __init__(self, data, data_path, parent_name):
        self.hamming_window = None
        self.data_chunks = None
        self.data = data
        self.parent_name = parent_name

        # Checking if frequency is predefined
        if "kHz" in data_path:
            if "100" in data_path:
                self.frequency = 100
                print(f'SET FREQ 100 in {self.parent_name} (this is not a default value)')
            elif "200" in data_path:
                self.frequency = 200
                print(f'SET FREQ 200 in {self.parent_name} (this is not a default value)')
            elif "400" in data_path:
                self.frequency = 400
                print(f'SET FREQ 400 in {self.parent_name} (this is not a default value)')
        # Setting frequency 400 by default
        else:
            self.frequency = 400
        self.len = len(data)

    def get_chunks(self):
        return self.data_chunks

    def get_len(self):
        return self.len

    def get_divider_for_chunks(self):
        return self.frequency*2

    def get_data(self):
        return self.data

    def set_chunks(self, chunk):
        self.data_chunks = chunk

    def set_hamming_window(self, data):
        self.hamming_window = data
