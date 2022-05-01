def get_positive_numbers():
    
    """
    Function that request as input a list of numbers separated with a comma
    :return: List of only positive number from the list
    """
    input_list = input("Enter number list separated with comma")
    lst = list(map(lambda x: int(x), input_list.split(',')))
    positive_list = list(filter(lambda x: x > 0, lst))
    return positive_list


print(get_positive_numbers())

