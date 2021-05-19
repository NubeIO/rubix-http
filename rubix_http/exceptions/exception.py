class BadDataException(BaseException):
    def __init__(self, *args):
        super(BadDataException, self).__init__(*args)


class UnauthorizedException(BaseException):
    def __init__(self, *args):
        super(UnauthorizedException, self).__init__(*args)


class ForbiddenException(BaseException):
    def __init__(self, *args):
        super(ForbiddenException, self).__init__(*args)


class NotFoundException(BaseException):
    def __init__(self, *args):
        super(NotFoundException, self).__init__(*args)


class PreConditionException(BaseException):
    def __init__(self, *args):
        super(PreConditionException, self).__init__(*args)


class InternalServerErrorException(BaseException):
    def __init__(self, *args):
        super(InternalServerErrorException, self).__init__(*args)


class NotImplementedException(BaseException):
    def __init__(self, *args):
        super(NotImplementedException, self).__init__(*args)


class GatewayTimeoutException(BaseException):
    def __init__(self, *args):
        super(GatewayTimeoutException, self).__init__(*args)
