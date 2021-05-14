import pandas as pd
from all_data import merge_into_one_list
from names_sorting import *
from hamming_window import *
from dataset_class import *
from divide_into_chunks import *

# Returning dictionary of sorted fields names
files_names = data_names_sorting()

# Declaration of main datasets containers
healthy_data_5A = []
healthy_data_10A = []
faulty_data_5A = []
faulty_data_10A = []
distorted_data_5A = []
distorted_data_10A = []

# Getting data from specific files and putting it in adequate dataset container
# TODO - PUT THAT IN SEPARATE FUNCTION - best case to return all datasets already fulfilled
for file_name in files_names:
    for item in files_names[file_name]:
        file_path = './Pomiary_BLDG/'+item
        data = pd.read_csv(file_path)
        tmp = Dataset(data=data, data_path=file_path, parent_name=item)
        if file_name == "healthy_data_5A":
            healthy_data_5A.append(tmp)
        if file_name == "healthy_data_10A":
            healthy_data_10A.append(tmp)
        if file_name == "faulty_data_5A":
            faulty_data_5A.append(tmp)
        if file_name == "faulty_data_10A":
            faulty_data_10A.append(tmp)
        if file_name == "distorted_data_5A":
            distorted_data_5A.append(tmp)
        if file_name == "distorted_data_10A":
            distorted_data_10A.append(tmp)


healthy_data_5A = divide_into_chunks(healthy_data_5A)
healthy_data_10A = divide_into_chunks(healthy_data_10A)
faulty_data_5A = divide_into_chunks(faulty_data_5A)
faulty_data_10A = divide_into_chunks(faulty_data_10A)
distorted_data_5A = divide_into_chunks(distorted_data_5A)
distorted_data_10A = divide_into_chunks(distorted_data_10A)


healthy_data_5A = make_hamming_window(healthy_data_5A)
healthy_data_10A = make_hamming_window(healthy_data_10A)
faulty_data_5A = make_hamming_window(faulty_data_5A)
faulty_data_10A = make_hamming_window(faulty_data_10A)
distorted_data_5A = make_hamming_window(distorted_data_5A)
distorted_data_10A = make_hamming_window(distorted_data_10A)



healthy_data_5A = merge_into_one_list(healthy_data_5A)
healthy_data_10A = merge_into_one_list(healthy_data_10A)
faulty_data_5A = merge_into_one_list(faulty_data_5A)
faulty_data_10A = merge_into_one_list(faulty_data_10A)
distorted_data_5A = merge_into_one_list(distorted_data_5A)
distorted_data_10A = merge_into_one_list(distorted_data_10A)




