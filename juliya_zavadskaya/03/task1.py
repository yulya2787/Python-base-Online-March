def get_def_function(list1, list2):
    """
    The function subtracts one list from another and returns the result.
    It should remove all values (all of its occurrences) from one list, which are present in the another list.
    :param list1: custom user list
    :param list2: custom user list
    :type list1: list
    :type list2: list
    :return: the result of lists' subtracts
    """
    list_result = []
    while True:
        for i in list1:
            for j in list2:
                if i != j:
                    list_result.append(i)
        else:
            break
    return list_result

help(get_def_function)


list1 = input('Enter the first list:')
list2 = input('Enter the second list:')
list_result = get_def_function(list1, list2)
print(list_result)