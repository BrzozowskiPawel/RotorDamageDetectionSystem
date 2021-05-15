import pandas as pd
from dataset_class import *
import main_data_set
from termcolor import colored
import os


def merge_into_one_list(data):
    tmp = []
    for item in data:
        x = item.get_chunks()
        for item2 in x:
            tmp.append(item2)
    return tmp


def create_chunks(list_name, n):
    for i in range(0, len(list_name), n):
        yield list_name[i:i + n]


def divide_into_chunks(data_set):
    for item in data_set:
        data = item.get_data()
        n = item.get_divider_for_chunks()

        chunk = list(create_chunks(list_name=data, n=n))
        item.set_chunks(chunk)


# This function is searching for specific characters in names of datasets.
# It returns dictionary of main data sets and as parameter names of different files corresponding with the main one.
def data_names_sorting():
    print('Starting to find name of a file')
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
        print(colored(no_error_message, 'green'))
    else:
        print(colored("FATAL ERROR \nMISSING DATA AFTER SORT", 'red'))
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
    print(colored(f'FINDING NAMES DONE, total: {num_data_after_sort} items', 'blue'))
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


def fulfill_main_data_set_container(files_names):
    # Declaration of main datasets containers and storing it inside container
    healthy_data_5A = main_data_set.Main_Dataset('healthy_data_5A')
    healthy_data_10A = main_data_set.Main_Dataset('healthy_data_10A')
    faulty_data_5A = main_data_set.Main_Dataset('faulty_data_5A')
    faulty_data_10A = main_data_set.Main_Dataset('faulty_data_10A')
    distorted_data_5A = main_data_set.Main_Dataset('distorted_data_5A')
    distorted_data_10A = main_data_set.Main_Dataset('distorted_data_10A')

    for file_name in files_names:
        for item in files_names[file_name]:
            file_path = './Pomiary_BLDG/' + item
            data = pd.read_csv(file_path)
            tmp = Small_Dataset(data=data, data_path=file_path, parent_name=item)
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

    main_dataset_container = []
    main_dataset_container.append(healthy_data_5A)
    main_dataset_container.append(healthy_data_10A)
    main_dataset_container.append(faulty_data_5A)
    main_dataset_container.append(faulty_data_10A)
    main_dataset_container.append(distorted_data_5A)
    main_dataset_container.append(distorted_data_10A)

    number_of_data_sets = 0
    print('\n')
    for item in main_dataset_container:
        print(f"Container name: {item.name_of_container}, contains: {len(item.get_data_from_csv())} items")
        number_of_data_sets += len(item.get_data_from_csv())
    print(colored(f"Total number of items in main_dataset_container: {number_of_data_sets}", 'blue'))

    return main_dataset_container

# This function is searching for specific characters in names of datasets.
# It returns dictionary of main data sets and as parameter names of different files corresponding with the main one.
def data_names_sorting():
    print('Starting to find name of a file')
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
        print(colored(no_error_message, 'green'))
    else:
        print(colored("FATAL ERROR \nMISSING DATA AFTER SORT", 'red'))
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
    print(colored(f'FINDING NAMES DONE, total: {num_data_after_sort} items', 'blue'))
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