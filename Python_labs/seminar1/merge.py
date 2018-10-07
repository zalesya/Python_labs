def merge(list_1, list_2):
    count_list_1 = 0
    count_list_2 = 0
    result_sorted_list = []

    while count_list_1 < list_1.__len__() and count_list_2 < list_2.__len__():
        if list_1[count_list_1] <= list_2[count_list_2]:
            result_sorted_list.append(list_1[count_list_1])
            count_list_1 += 1
        else:
            result_sorted_list.append(list_2[count_list_2])
            count_list_2 += 1

    remained = list_1[count_list_1:] + list_2[count_list_2:]
    result_sorted_list.extend(remained)

    return result_sorted_list


#if __name__ == '__main__':
    #s1 = input()
    #s2 = input()

    #l1 = tuple(map(int, s1.split(' ')))
    #l2 = tuple(map(int, s2.split(' ')))
    #print(merge(l1, l2))
