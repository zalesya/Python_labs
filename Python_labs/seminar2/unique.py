def compress(list2):
    list2 = sorted(list2)
    answer = {list2[i]: 0 for i in range(list2.__len__())}
    i = 0
    keys = answer.keys()
    for key in keys:
        count = 0
        while i < list2.__len__() and key == list2[i]:
            count += 1
            i += 1
        answer.update({key: count})
    return list(answer.items())



