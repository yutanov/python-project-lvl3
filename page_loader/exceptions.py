#! /usr/bin/env python3

class AppInternalError(Exception):
    pass


class BadConnect(AppInternalError):
    pass


class ErrorSystem(AppInternalError):
    pass
