import functions
import dataset_class

# Loading files from csv.
# Function functions.get_data_from_csv() requires type of data set [healthy or faulty] and return list of pandas DataFrame objects
# Returned data from function above is now assigned as data_from_csf parameter in dataset_class.Dataset()
healthy = dataset_class.Dataset(functions.get_data_from_csv(type="healthy"))
faulty = dataset_class.Dataset(functions.get_data_from_csv(type="faulty"))

# Now hamming window function is being computed for each item in data_from_csv parameter od Dataset()
# Elements are saved in new list (Dataset() parameter hamming_window_list )
healthy.computer_hamming_window()
faulty.computer_hamming_window()
