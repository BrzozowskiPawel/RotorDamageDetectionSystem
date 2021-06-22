import time
import numpy as np
import functions
import dataset_class
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

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

X_train, X_test, y_train, y_test = train_test_split(DANE, TARGET, test_size = 0.2)
model = RandomForestClassifier(n_estimators=20)
classifier = model.fit(X_train, y_train)
model.score(X_test, y_test)

y_predict = model.predict(X_test)
acc = accuracy_score(y_test, y_predict)
print(f'accuracy: {acc} \n')
cm = confusion_matrix(y_test, y_predict)

class_names = ['healty', 'faulty']
titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(classifier, X_test, y_test, display_labels=class_names, cmap=plt.cm.Blues, normalize=normalize)
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

plt.show()


