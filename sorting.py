def bubble(list):
    for i in range(len(list) - 1):
        for sort in range(len(list) - 1):
            if list[sort] > list[sort + 1]:
                temp = list[sort]
                list[sort] = list[sort + 1]
                list[sort + 1] = temp
        sort = 0
    return list
