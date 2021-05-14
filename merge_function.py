def merge_into_one_list(data):
    tmp = []
    for item in data:
        x = item.get_chunks()
        for item2 in x:
            tmp.append(item2)
    return tmp