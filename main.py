import functions
import dataset_class
import prediction

# Loading files from csv.
# Function functions.get_data_from_csv() requires type of data set [healthy or faulty] and return list of pandas DataFrame objects
# Returned data from function above is now assigned as data_from_csf parameter in dataset_class.Dataset()
healthy = dataset_class.Dataset(functions.get_data_from_csv(type="healthy"), data_type="healthy")
faulty = dataset_class.Dataset(functions.get_data_from_csv(type="faulty"), data_type="faulty")


# Now hamming window function is being computed for each item in data_from_csv parameter od Dataset()
# Elements are saved in new list (Dataset() in parameter hamming_window_list
healthy.compute_hamming_window()
faulty.compute_hamming_window()


# Creating wawelets and computing standard deviation for each list of wawelets
healthy.create_wavelet_packet()
faulty.create_wavelet_packet()


# A function that accepts healthy and faulty sets as arguments.
# With the help of sklearn, we create a model and then, using the random forest,
# we try to predict whether the given data sets represent a defective rotor or a healthy one.
# The function returns nothing, but prints the confusion matrix and displays the graphical interpretation of the results
prediction.predict_values(healthy=healthy,faulty=faulty)

