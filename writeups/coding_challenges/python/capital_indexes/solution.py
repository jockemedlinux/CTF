def capital_indexes(string_):
    indexlist = []
    for index, value in enumerate(string_):
        if value.isupper(): indexlist.append(index)
    print(indexlist)
    return indexlist
            
capital_indexes("HeLlO")