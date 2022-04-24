def my_filter(func, iterable):
    """
    Function implementing filter
    :param func: boolean condition function
    :param iterable: iterable
    :return: list with only the elements of iterable for wich the function returns True
    """
    return [element for element in iterable if func(element)]



