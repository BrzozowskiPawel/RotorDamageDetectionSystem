import numpy as np

class Dataset:
    def __init__(self, data):
        self.data_from_csv = data
        self.hamming_window_list = []

    def computer_hamming_window(self):
        for item in self.data_from_csv:
            temporary_hamming_window = []
            current_array = np.array(item)
            hamming = np.hamming(len(item))
            temporary_hamming_window.append(current_array * hamming)
            self.hamming_window_list.append(temporary_hamming_window)
