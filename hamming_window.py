import numpy as np


def make_hamming_window(data_set):
    for chunks_list in data_set:
        tmp_list = chunks_list.get_chunks()
        tmp_hamming_window_list = []
        for item in tmp_list:
            temp_hamming_window = help_function_returning_hamming_win(item=item)
            tmp_hamming_window_list.append(temp_hamming_window)
        chunks_list.set_hamming_window(tmp_hamming_window_list)
    return data_set


def help_function_returning_hamming_win(item):
    hamming_window_function_array = []
    current_array = np.array(item)
    hamming = np.hamming(len(item))
    hamming_window_function_array.append(current_array * hamming)
    return hamming_window_function_array

