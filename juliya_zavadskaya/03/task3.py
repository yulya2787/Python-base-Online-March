def cust_filter(func, lists):

    """
    The function imitate original map python function.
    :param x: custom user list
    :param y: custom user list
    :return: the result of lists' split
    """

    list1 = []
    for i in range(len(lists[0])):
        if lists[0][i] != lists[1][i]:
            list1.append(func(lists[0][i], lists[1][i]))
    return list1


def func(a, b):
    return a, b


lists= [['3', '45', '5'], ['3', '44', '65']]

x = cust_filter(func, lists)

print(x)
