import os
#from termcolor import colored

# This function is searching for specific characters in names of datasets.
# It returns dictionary of main data sets and as parameter names of different files corresponding with the main one.


def data_names_sorting():
    # Importing files names to list
    # TODO - add option to send this function different path and catch errors
    data_names = os.listdir('./Pomiary_BLDG/')


    # Sorting data_names to 10A or 5A + Healthy, Faulty or Distorted
    healthy_data_5A = []
    healthy_data_10A = []
    faulty_data_5A = []
    faulty_data_10A = []
    distorted_data_5A = []
    distorted_data_10A = []

    for item in data_names:
        item_tmp = item.lower()
        if "10A" in item:
            if "healthy" in item_tmp:
                healthy_data_10A.append(item)
            if "faulty" in item_tmp:
                faulty_data_10A.append(item)
            if "distorted" in item_tmp:
                distorted_data_10A.append(item)

        elif "5A" in item:
            if "healthy" in item_tmp:
                healthy_data_5A.append(item)
            if "faulty" in item_tmp:
                faulty_data_5A.append(item)
            if "distorted" in item_tmp:
                distorted_data_5A.append(item)
        else:
            print('CLASSIFICATION ERROR! \n')
            print("non recognised item: ", item, '\n ')

    # Checking if number of data is the same before and after sorting
    num_data_before_sort = len(data_names)
    num_data_after_sort = len(healthy_data_5A)
    num_data_after_sort += len(healthy_data_10A)
    num_data_after_sort += len(faulty_data_5A)
    num_data_after_sort += len(faulty_data_10A)
    num_data_after_sort += len(distorted_data_5A)
    num_data_after_sort += len(distorted_data_10A)

    # Printing info about sorting status
    if num_data_before_sort == num_data_after_sort:
        no_error_message = "Number of data sets before and after sort are the same (" + str(
            num_data_before_sort) + ":" + str(num_data_after_sort) + ") -> NO DATA MISSING"
        #print(colored(no_error_message, 'green'))
    else:
        #print(colored("FATAL ERROR \nMISSING DATA AFTER SORT", 'red'))
        print("Please check error in data names/sorting data names\n")
        exit(1)

    # Printing info about files names // inst required this could be commented out
    print("Sorted files info:")
    print("-----------------------------------------------------------------------------")
    print(f"Names of files healthy 5A: {healthy_data_5A}")
    print(f"Names of files healthy 10A: {healthy_data_10A}")
    print(f"Names of files faulty 5A: {faulty_data_5A}")
    print(f"Names of files faulty 10A: {faulty_data_10A}")
    print(f"Names of files distorted 5A: {distorted_data_5A}")
    print(f"Names of files distorted 10A: {distorted_data_10A}")
    print("-----------------------------------------------------------------------------")

    # Formating data
    all_data_files = {
        "healthy_data_5A": healthy_data_5A,
        "healthy_data_10A": healthy_data_10A,
        "faulty_data_5A": faulty_data_5A,
        "faulty_data_10A": faulty_data_10A,
        "distorted_data_5A": distorted_data_5A,
        "distorted_data_10A": distorted_data_10A
    }
    print("\n")
    return all_data_files