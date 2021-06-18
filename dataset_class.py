import time
import statistics
import numpy as np
import Cython
import pywt

class Dataset:
    def __init__(self, data, data_type):
        self.data_type = data_type
        self.data_from_csv = data
        self.hamming_window_list = []
        self.wavelet_list = []
        self.std_deviation_list = []
        self.target_list = []

    def standard_deviation(self):
        for item in self.wavelet_list:
            self.std_deviation_list.append(statistics.stdev(item))

    def compute_hamming_window(self):
        for item in self.data_from_csv:
            temporary_hamming_window = []
            current_array = np.array(item)
            hamming = np.hamming(len(item))

            hamming = hamming.tolist()
            current_array = current_array.tolist()

            len_of_lists = len(current_array)
            for i in range(len_of_lists):
                tmp_compute = current_array[i][0]*hamming[i]
                temporary_hamming_window.append(tmp_compute)
            self.hamming_window_list.append(temporary_hamming_window)
        print(f'Hamming window created {[self.data_type]}')

    def get_hamming_window_list(self):
        return self.hamming_window_list


    def create_wavelet_packet(self):
        for item in self.hamming_window_list:
            item = np.array(item)
            wp = pywt.WaveletPacket(data=item, wavelet='db1', mode='symmetric', maxlevel=4)
            self.wavelet_list.append(wp['aaaa'].data)
            self.wavelet_list.append(wp['aaad'].data)
            self.wavelet_list.append(wp['aada'].data)
            self.wavelet_list.append(wp['aadd'].data)
            self.wavelet_list.append(wp['adaa'].data)
            self.wavelet_list.append(wp['adad'].data)
            self.wavelet_list.append(wp['adda'].data)
            self.wavelet_list.append(wp['addd'].data)
            self.wavelet_list.append(wp['daaa'].data)
            self.wavelet_list.append(wp['daad'].data)
            self.wavelet_list.append(wp['dada'].data)
            self.wavelet_list.append(wp['dadd'].data)
            self.wavelet_list.append(wp['ddaa'].data)
            self.wavelet_list.append(wp['ddad'].data)
            self.wavelet_list.append(wp['ddda'].data)
            self.wavelet_list.append(wp['dddd'].data)

        self.standard_deviation()
        print(f'Wavelet packet created + calculated std. deviation from this data {[self.data_type]}')

    def get_std_deviation_list(self):
        return self.std_deviation_list

    def get_target(self):
        num_of_targets = len(self.std_deviation_list)
        if self.data_type == "healthy":
            target = 1
        elif self.data_type == "faulty":
            target = 0
        for i in range(num_of_targets):
            self.target_list.append(target)

        return self.target_list



