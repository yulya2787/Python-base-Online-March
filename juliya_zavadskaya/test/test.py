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