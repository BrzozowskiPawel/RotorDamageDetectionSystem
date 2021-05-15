import functions

# Returning dictionary of sorted fields names
files_names = functions.data_names_sorting()

# Putting data into specific container and all that containers into one main container
main_dataset_container = functions.fulfill_main_data_set_container(files_names=files_names)

# Dividing all data from each data set into smaller list (chunks)
# Now data from csv is being cut into smaller chunks and is is stored as list of chunks -> data_chunks
for container in main_dataset_container:
    functions.divide_into_chunks(container.get_data_from_csv())

# PREVIOUS CODE:
# divide_into_chunks(healthy_data_5A.get_data_from_csv())
# divide_into_chunks(healthy_data_10A.get_data_from_csv())
# divide_into_chunks(faulty_data_5A.get_data_from_csv())
# divide_into_chunks(faulty_data_10A.get_data_from_csv())
# divide_into_chunks(distorted_data_5A.get_data_from_csv())
# divide_into_chunks(distorted_data_10A.get_data_from_csv())

# Merging chunks into one list for each main dataset
for container in main_dataset_container:
    container.set_merged_chunks()

# PREVIOUS CODE:
# healthy_data_5A.set_merged_chunks()
# healthy_data_10A.set_merged_chunks()
# faulty_data_5A.set_merged_chunks()
# faulty_data_10A.set_merged_chunks()
# distorted_data_5A.set_merged_chunks()
# distorted_data_10A.set_merged_chunks()



# Making hamming window from chunks that were previously created
# healthy_data_5A = make_hamming_window(healthy_data_5A)
# healthy_data_10A = make_hamming_window(healthy_data_10A)
# faulty_data_5A = make_hamming_window(faulty_data_5A)
# faulty_data_10A = make_hamming_window(faulty_data_10A)
# distorted_data_5A = make_hamming_window(distorted_data_5A)
# distorted_data_10A = make_hamming_window(distorted_data_10A)








