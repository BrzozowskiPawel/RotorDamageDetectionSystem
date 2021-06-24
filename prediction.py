import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix


def predict_values(healthy, faulty):
    # DATA - a collection of features from each window. In the basic case, we will take them out of the hamming window
    # Target - a set of healthy or faulty features (written in binary as 1 or 0)

    # Creating DATA and TARGET variables.
    DATA = healthy.get_std_deviation_list() + faulty.get_std_deviation_list()
    TARGET = healthy.get_target() + faulty.get_target()
    DATA = np.reshape(DATA, (len(DATA), 1))

    # Creating train and test variables and then random forest model.
    X_train, X_test, y_train, y_test = train_test_split(DATA, TARGET, test_size=0.3)
    model = RandomForestClassifier(n_estimators=20)
    classifier = model.fit(X_train, y_train)
    model.score(X_test, y_test)

    # Predicting data and calculating it's accuracy
    y_predict = model.predict(X_test)
    acc = accuracy_score(y_test, y_predict)
    print(f'accuracy: {round(acc*100, 2)} % \n')
    cm = confusion_matrix(y_test, y_predict)

    # Creating plots to visualize data
    class_names = ['healty', 'faulty']
    titles_options = [("Confusion matrix, without normalization", None),
                      ("Normalized confusion matrix", 'true')]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(classifier, X_test, y_test, display_labels=class_names, cmap=plt.cm.Blues,normalize=normalize)
        disp.ax_.set_title(title)
        print(title)
        print(disp.confusion_matrix)
    plt.show()