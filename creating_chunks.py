def create_chunks(list_name, n):
    for i in range(0, len(list_name), n):
        yield list_name[i:i + n]