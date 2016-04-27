def data_type(datatype_):
    """
    For strings, return its length.
    For None return string 'no value'
    For booleans return the boolean
    For integers return a string showing how it compares to hundred e.g.
    For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
    For lists return the 3rd item, or None if it doesn't exist

    """

    if datatype_ is None:

        return 'no value'

    elif isinstance(datatype_, str):

        return len(datatype_)

    elif isinstance(datatype_, bool):

        return datatype_



        elif isinstance(datatype_, int):

            if datatype_ < 100:

                return 'less than 100'

            return 'more than 100'

        elif isinstance(datatype_, list):

            if len(datatype_) > 2:

                return datatype_[2]
            else:
                return None
