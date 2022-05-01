import string


def count_words(txt):
    
    """
    Function that receive a text and return a dictionary of every word in the text as key and the word length as value
    :param txt: string text
    :return: dictionary of word's length
    """
    lower_case = ''.join([x.lower() for x in txt if x not in string.punctuation])
    lower_case = lower_case.split()
    text_dict = {word: len(word) for word in lower_case}
    return text_dict


text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""


if __name__ == '__main__':
    print(count_words(text))





