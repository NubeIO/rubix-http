class NotFoundException(BaseException):
    def __init__(self, *args):
        super(NotFoundException, self).__init__(*args)


class BadDataException(BaseException):
    def __init__(self, *args):
        super(BadDataException, self).__init__(*args)