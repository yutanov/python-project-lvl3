import string
import logging

log = logging.getLogger(__name__)


def gen_name(url):
    url = url.lower()
    low_letters = string.ascii_lowercase
    nums = [str(i) for i in range(10)]
    name = ''
    if url[:8] == 'https://':
        url = url[8:]
    elif url[:7] == 'http://':
        url = url[7:]
    elif url[:2] == '//':
        url = url[2:]
    elif url[:1] == '/':
        url = url[1:]
    for sym in url:
        if sym in low_letters or sym in nums:
            name += sym
        else:
            name += '-'
    log.debug('Name for {0} generated'.format(url))
    return name
