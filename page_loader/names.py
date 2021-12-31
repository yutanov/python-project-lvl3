# -*- coding: utf-8 -*-

"""Names generator functions."""

import logging
import os
import re
from urllib.parse import urlparse

from page_loader.common import debug_logger

log = logging.getLogger(__name__)


@debug_logger
def create_resources_dir_name(path):
    """Create local resources dir name.

    Args:
        path: string

    Returns:
        string: path with replaced values
    """
    return path.replace('.html', '_files')


@debug_logger
def create_resource_name(res):
    """Create local resource file name.

    Args:
        res: string

    Returns:
        string
    """
    base, ext = os.path.splitext(res)
    base = re.sub(r'[\W_]', '-', base.replace('/', '', 1))
    return f'{base}{ext}'


@debug_logger
def create_html_file_name(res):
    """Create html page file name.

    Args:
        res: string

    Returns:
        string
    """
    parsed = urlparse(res)
    scheme = parsed.scheme
    page_name = parsed.geturl().lstrip(f'{scheme}://')
    page_name = re.sub(r'[\W_]', '-', page_name)
    return f'{page_name}.html'
