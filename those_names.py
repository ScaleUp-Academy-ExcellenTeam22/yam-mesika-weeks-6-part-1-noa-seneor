import string
from itertools import product


def full_names(first, last, min_length=0):
    """
    :param first: list of first names
    :param last: list of last names
    :param min_length: (optional) minimum length of name combination
    :return: return all unique combinations of firstnames and lastnames
    """
    return [f[0].upper() + f[1::] + ' ' + l[0].upper() + l[1::] for f, l in list(product(first, last)) if (len(f) + len(l) >= min_length -1)]


first_names = ['avi', 'moshe', 'yaakov']
last_names = ['cohen', 'levi', 'mizrahi']


if __name__ == '__main__':
    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names))
