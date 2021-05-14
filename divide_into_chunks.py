from creating_chunks import *


def divide_into_chunks(data_set):
    for item in data_set:
        data = item.get_data()
        n = item.get_divider_for_chunks()

        chunk = list(create_chunks(list_name=data, n=n))
        item.set_chunks(chunk)