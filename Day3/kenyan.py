from person import Person


class Kenyan(Person):
    corrupt = False
    """docstring for ClassName"""
    # def __init__(self, arg):
    #   super(ClassName, self).__init__()
    #   self.arg = arg

    def probe(self, corrupt):
        self.corrupt = corrupt

    def is_corrupt(self):
        if self.corrupt:
            return "YES"
        return "NO"
