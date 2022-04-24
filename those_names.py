from itertools import product


def full_names(first, last, min_length=0):
    """
    Function that receives a list of first names and a list of last names
    and return all unique combinations of firstnames and lastnames in a list
    :param first: list of first names
    :param last: list of last names
    :param min_length: (optional) minimum length of name combination
    :return: combination list
    """
    return [firstnames[0].upper() + firstnames[1::] + ' ' + lastnames[0].upper() + lastnames[1::]
            for firstnames, lastnames in list(product(first, last)) if (len(firstnames) + len(lastnames) >= min_length -1)]


first_names = ['avi', 'moshe', 'yaakov']
last_names = ['cohen', 'levi', 'mizrahi']


if __name__ == '__main__':
    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names))
