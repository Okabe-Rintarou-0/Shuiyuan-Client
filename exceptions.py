class ResponseDataFormatErrorException(Exception):
    def __init__(self) -> None:
        super().__init__('Response data format error! Please check whether cookies are correctly set.')

class TooManyOperationsException(Exception):
    def __init__(self) -> None:
        super().__init__('Too many operations')