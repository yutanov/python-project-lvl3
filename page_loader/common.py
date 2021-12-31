# -*- coding: utf-8 -*-

"""Common entities of the project."""
import logging
import os
from functools import wraps

import requests

log = logging.getLogger(__name__)

LOCAL_RESOURCES = {  # noqa: 407
    'link': 'href',
    'script': 'src',
    'img': 'src',
}


def get_url(url):
    """Get response from url.

    Args:
        url: string

    Raises:
        requests.HTTPError: on HTTP error

    Returns:
        requests.models.Response object
    """
    try:  # noqa: WPS229
        res = requests.get(url)
        res.raise_for_status()
    except requests.HTTPError as err:
        log.exception(
            str(err.args),
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise
    return res


def create_dir(path):
    """Create directory.

    Args:
        path: string
    """
    if not os.path.exists(path):
        os.makedirs(path)


def save(path, file_content, mode='w'):
    """Save provided data.

    Args:
        path: string that represents file path
        file_content: file content
        mode: file writing mode

    Raises:
        PermissionError: on write permission errors
    """
    try:
        with open(path, mode) as f:
            f.write(file_content)
    except PermissionError:
        log.exception(
            'Permission denied',
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise


def debug_logger(func):
    """Log decorator function.

    Args:
        func: function, that will be decorated

    Returns:
        function-wrapper around decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):  # noqa: WPS430
        func_name = f'[{func.__name__:>30}]'

        log.debug(f'{func_name} :: input: {args} {kwargs}')
        res = func(*args, **kwargs)
        log.debug(f'{func_name} :: return: {str(res)}')
        return res
    return wrapper
