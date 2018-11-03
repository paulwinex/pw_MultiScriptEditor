

# context completer
class contextCompleterClass(object):
    def __init__(self, name, complete, end=None):
        self.name = name
        self.complete = complete
        self.end_char = end