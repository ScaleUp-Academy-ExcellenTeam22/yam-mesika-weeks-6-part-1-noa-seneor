def my_filter(func, lst):
    """
    function implementing filter using tail recursion
    :param func: boolean function
    :param lst: list
    :return: list with only the elements from lst that func return True for them
    """
    def tail_filter(function, lst1, lst2):
        if not len(lst1):
            return lst2
        if function(lst1[0]):
            lst2 += [lst1[0]]
        return tail_filter(function, lst1[1::], lst2)
    return tail_filter(func, lst, [])


