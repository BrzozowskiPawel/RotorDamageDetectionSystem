import time

import numpy as np
import Cython
import pywt

class Dataset:
    def __init__(self, data):
        self.data_from_csv = data
        self.hamming_window_list = []
        self.wavelet_list = []


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
        print('Hamming window created')

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



        print('Wavelet packet created')


