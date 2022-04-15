def get_positive_numbers():
    """
    Function that ask the user to enter a list of number
    separated with comma
    :return: list of only positive number from the list
    """
    input_list = input("enter number list separated with comma")
    lst = list(map(lambda x: int(x), input_list.split(',')))
    positive_list = list(filter(lambda x: x > 0, lst))
    return positive_list


print(get_positive_numbers())

