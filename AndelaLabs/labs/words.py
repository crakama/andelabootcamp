"""
A function that For example for the input "olly olly in come free"

olly: 2
in: 1
come: 1
free: 1


"""

def words(wordlst):

    wordslist = wordlst.split()

    dict_ = {}

    for word in wordslist:
        if word.isdigit():
            word = int(word)
        if word in dict_:
            dict_[word] = dict_[word] + 1
        else:
            dict_[word] = 1

    return dict_

