def words_length(sentence):
    
    """

    :param sentence: string
    :return: list containing length of every words in sentence
    """
    return [len(word) for word in sentence.split()]


if __name__ == '__main__':
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
