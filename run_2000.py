import time


def timer(f, *args, **kwargs) -> float:
    """
    Function that receive a function and other parameters and measure how long it takes
    for the function to run with those parameters
    :param f: function
    :param args: unlimited arguments by location
    :param kwargs: unlimited arguments by name
    :return: execution time of function f
    """
    starting_time = time.time()
    f(*args, **kwargs)
    ending_time = time.time()
    return ending_time - starting_time


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
