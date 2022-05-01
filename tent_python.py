from functools import reduce


def get_letters():
    
    """
    :return: list of all letters between a to z , and between A to Z using chr and ord
    """
    letters = [chr(i) for i in list(range(ord('a'), ord('z'))) + list(range(ord('A'), ord('Z')))]
    return letters


if __name__ == '__main__':
    print(get_letters())
