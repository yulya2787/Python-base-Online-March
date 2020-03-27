def mapper(func, lists):

    """
    The function imitate original map python function.
    :param x: custom user list
    :param y: custom user list
    :return: the result of lists' split
    """

    list1 = []
    for i in range(len(lists[0])):
        list1.append(func(lists[0][i], lists[1][i], lists[2][i]))
    return list1


def func(a, b, c):
    return a + b + c


lists= [['3', '4', '5'], ['13', '44', '65'], ['2', '3', '3']]

x = mapper(func, lists)

print(x)

'''
def get_my_map(list1, list2):
    """
    The function imitate original map python function.
    :param list1: custom user list
    :param list2: custom user list
    :type list1: list
    :type list2: list
    :return: the result of lists' split
    """
    result_1 = [x + y for x, y in zip(list1, list2)]
    return result_1


list1 = input('Enter the first list:')
list2 = input('Enter the second list:')
result_1 = get_my_map(list1, list2)
print(result_1)
'''
'''
def mapper(func, sequences):

    """
    The function imitate original map python function.
    :param x: custom user list
    :param y: custom user list
    :return: the result of lists' split
    """

    list1 = []
    for i in sequences:
        list1.append(func(i))
    return list1


def func(n):
    ls = n + 1
    return ls


ls = [1, 2, 3]
x = mapper(func, ls)

print(x)
'''