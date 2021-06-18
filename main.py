import time
import numpy as np
import functions
import dataset_class
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

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

# for item in healthy.wavelet_list:
#     print(type(item))
#     time.sleep(5)
#Dane - zbior cech rpzetowroznych z kazdego okna. Wyciagniemy je z okna hamminga
#Target - H czy F (binarnie 1 lub 0)x


DANE = healthy.get_std_deviation_list() + faulty.get_std_deviation_list()
TARGET = healthy.get_target() + faulty.get_target()
DANE = np.reshape(DANE, (len(DANE), 1))

X_train, X_test, y_train, y_test = train_test_split(DANE, TARGET, test_size = 0.3)
model = RandomForestClassifier(n_estimators=20)
model.fit(X_train, y_train)
model.score(X_test, y_test)

y_predict = model.predict(X_test)
cm = confusion_matrix(y_test, y_predict)
 



