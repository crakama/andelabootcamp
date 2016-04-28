def find_max_min(list_):

    max_ = list_[0]
    min_ = list_[0]
    arrayMinMax = []

    for value in list_:
        if value < min_:
            min_ = value
        elif value > max_:
            max_ = value

    if max_ == min_:
        arrayMinMax.append(len(list_))
        return arrayMinMax
    else:
        arrayMinMax.append(min_)
        arrayMinMax.append(max_)
        return arrayMinMax
