class AppException(Exception):
    message = ""


class InvalidURLError(AppException):
    message = "Введите правильный url, https://...."


class BlackListError(AppException):
    message = "Данный url находиться в черном списке, попробуйте другой"
