import functions


# functions.data_names_sorting() ~ HOW IT WORKS
# Returning dictionary of sorted fields names
files_names = functions.data_names_sorting()

# functions.fulfill_main_data_set_container() ~ HOW IT WORKS
# Putting data into specific container and all that containers into one main container
# For example main_dataset_container[] -> healthy 5A[] -> data_from_csv[]
main_dataset_container = functions.fulfill_main_data_set_container(files_names=files_names)

# functions.divide_into_chunks() ~ HOW IT WORKS
# Dividing all data from each data set into smaller list (chunks)
# First of all argument for divide_into_chunks is list inside main_dataset_container ex. main_dataset_container[] -> healthy 5A[]
# Then for each list inside (ex. healthy 5A[]) is created chunk of data (specific number of data in list), this is dependent of sampling frequency (default is 400)
# Then for each item (Small_Dataset ex. main_dataset_container[] -> healthy 5A[] -> data_from_csv[sets of data HERE]), parameter chunk is set. Basically from 1 long list (ex 2000 records) there are created 3 smaller lists.
# At the end we have ex. main_dataset_container[] -> healthy 5A[] -> 5A Healthy4.csv_data[] -> chunks[] if there was 2000 records inside a 5A Healthy4.csv_data[] now ifs a list containing for example 3 or 4 list that together contain 2000 records

# VARIABLE DESCRIPTION
# container is list of specific type csv files ex. healthy 5A: ['5A Healthy 4.csv', '5A Healthy 5.csv', '5A Healthy 1.csv', '5A Healthy 2.csv', '5A Healthy 3.csv']
# Each file inside container is 1 single file with big number of records (aprox. 2k)
# In this step we are converting this 1 big list into couple smaller lists (CHUNKS),
for container in main_dataset_container:
    functions.divide_into_chunks(container.get_data_from_csv())

# set_merged_chunks() ~ HOW IT WORKS
# Merging chunks into one list for each main dataset.
# Now main_dataset_container have specific type containers that contain all merged chunks from each csv file
# ex. main_dataset_container[] -> healthy 5A[] ->  \all merged chunks into one\
for container in main_dataset_container:
    container.set_merged_chunks()



# Making hamming window from chunks that were previously created
# healthy_data_5A = make_hamming_window(healthy_data_5A)
# healthy_data_10A = make_hamming_window(healthy_data_10A)
# faulty_data_5A = make_hamming_window(faulty_data_5A)
# faulty_data_10A = make_hamming_window(faulty_data_10A)
# distorted_data_5A = make_hamming_window(distorted_data_5A)
# distorted_data_10A = make_hamming_window(distorted_data_10A)








