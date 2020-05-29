class Error(Exception):
    pass


class HelloError(Error):
    def __init__(self, *args):
        self.message = args[0]
    