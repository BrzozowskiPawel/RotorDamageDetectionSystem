import pandas as pd
import os


def get_data_from_csv(type):
    #Checing if type of files is correct [there are only 2 options as this was specyfied in task]
    if type != 'healthy' or type != 'faulty':

        # Loading list of files names
        files_names = os.listdir(f'./datasets/{type}')
        dataset_list = []

        # Loading csv files from directory and appending it into the list
        for file_path in files_names:
            with open(f"./datasets/{type}/{file_path}", 'r') as file:
                df = pd.read_csv(file)
                dataset_list.append(df)
        print(f'Downloaded {len(dataset_list)} files in {type} data completed')

        # Returning list of all loaded files as list of DataFrame objects
        return dataset_list

    # In case of wrong type no files will be loaded
    else:
        print('Sorry your type is incorrect, please choose healthy or faulty')