def words(phrase):
    wordsplit = phrase.split()

    dict_ = {}

    for word in wordsplit:
        if dict_.get(word):
            dict_ += 1
        else:
            dict_ = 1
    return dict_
