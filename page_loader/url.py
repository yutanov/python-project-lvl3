import os
import re
from urllib.parse import urlparse


def to_file_name(base_url):
    _, ext = os.path.splitext(urlparse(base_url).path)
    if ext:
        url, ext = os.path.splitext(base_url)
    else:
        ext = '.html'
        url = base_url
    url_parts = re.split('[^a-zA-Z0-9]+', url)
    url_parts.pop(0)
    max_len = 10
    while len(url_parts) > max_len:
        url_parts.pop(0)
    return '-'.join(url_parts) + ext
