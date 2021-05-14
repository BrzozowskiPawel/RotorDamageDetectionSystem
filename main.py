import pandas as pd
from merge_function import merge_into_one_list
from names_sorting import *
from hamming_window import *
from dataset_class import *
from divide_into_chunks import *
import main_data_set

# Returning dictionary of sorted fields names
files_names = data_names_sorting()

# Declaration of main datasets containers
healthy_data_5A = main_data_set.DataSet()
healthy_data_10A = main_data_set.DataSet()
faulty_data_5A = main_data_set.DataSet()
faulty_data_10A = main_data_set.DataSet()
distorted_data_5A = main_data_set.DataSet()
distorted_data_10A = main_data_set.DataSet()

# Getting data from specific files and putting it in adequate dataset class -> data_from_csv argument
# TODO - PUT THAT IN SEPARATE FUNCTION - best case to return all datasets already fulfilled
for file_name in files_names:
    for item in files_names[file_name]:
        file_path = './Pomiary_BLDG/'+item
        data = pd.read_csv(file_path)
        tmp = Dataset(data=data, data_path=file_path, parent_name=item)
        if file_name == "healthy_data_5A":
            healthy_data_5A.set_data_from_csv(tmp)
        if file_name == "healthy_data_10A":
            healthy_data_10A.set_data_from_csv(tmp)
        if file_name == "faulty_data_5A":
            faulty_data_5A.set_data_from_csv(tmp)
        if file_name == "faulty_data_10A":
            faulty_data_10A.set_data_from_csv(tmp)
        if file_name == "distorted_data_5A":
            distorted_data_5A.set_data_from_csv(tmp)
        if file_name == "distorted_data_10A":
            distorted_data_10A.set_data_from_csv(tmp)

# Dividing all data from each data set into smaller list (chunks)
# Now data from csv is being cut into smaller chunks and is is stored as list of chunks -> datachunks
data = divide_into_chunks(healthy_data_5A.get_data_from_csv())
healthy_data_5A.set_datachunks(data)
data2 = divide_into_chunks(healthy_data_10A.get_data_from_csv())
healthy_data_10A.set_datachunks(data2)
data3 = divide_into_chunks(faulty_data_5A.get_data_from_csv())
faulty_data_5A.set_datachunks(data3)
data4 = divide_into_chunks(faulty_data_10A.get_data_from_csv())
faulty_data_10A.set_datachunks(data4)
data5 = divide_into_chunks(distorted_data_5A.get_data_from_csv())
distorted_data_5A.set_datachunks(data5)
data6 = divide_into_chunks(distorted_data_10A.get_data_from_csv())
distorted_data_10A.set_datachunks(data6)

# Z CZEGO TWORZYMY HAMMING WINDOW???
# DO TEGO MIEJSCA ZROBILEM

# Making hamming window from chunks that were previously created
healthy_data_5A = make_hamming_window(healthy_data_5A)
healthy_data_10A = make_hamming_window(healthy_data_10A)
faulty_data_5A = make_hamming_window(faulty_data_5A)
faulty_data_10A = make_hamming_window(faulty_data_10A)
distorted_data_5A = make_hamming_window(distorted_data_5A)
distorted_data_10A = make_hamming_window(distorted_data_10A)

# Merging chunks of hamming window into one list for each main dataset
healthy_data_5A = merge_into_one_list(healthy_data_5A)
healthy_data_10A = merge_into_one_list(healthy_data_10A)
faulty_data_5A = merge_into_one_list(faulty_data_5A)
faulty_data_10A = merge_into_one_list(faulty_data_10A)
distorted_data_5A = merge_into_one_list(distorted_data_5A)
distorted_data_10A = merge_into_one_list(distorted_data_10A)






