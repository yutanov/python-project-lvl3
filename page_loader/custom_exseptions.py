class AppInternalError(Exception):
    pass


class BadConnect(AppInternalError):
    pass


class ErrorSystem(AppInternalError):
    pass
