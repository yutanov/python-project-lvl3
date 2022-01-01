import os
import os.path
from page_loader.custom_exseptions import ErrorSystem
import re
import logging.config
from pathlib import Path
from urllib.parse import urlparse, urljoin
from page_loader.settings_logging import logger_config


logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def is_local_link(url_link, url_page):
    return urlparse(url_link).netloc == urlparse(url_page).netloc


def convert_relative_link(link, url):
    domain_name = urlparse(url).netloc
    if link.startswith('http'):
        pass
    elif urlparse(link).netloc == domain_name:
        link = urljoin(url, link)
    elif re.match(r'/\w', link):
        link = urljoin(url, link)
    else:
        pass
    return link


def convert_path_name(path):
    path = str(path)
    if path.startswith('http'):

        _, path = re.split('://', path)
    if path.endswith('/'):
        path = path[:-1]
    return re.sub(r'[\W_]', '-', path)


def add_suff_for_name_link(name):
    part, suff = os.path.splitext(name)
    if not suff:
        suff = '.html'
    # removes the characters after ? (for example, "/image.png?c=3.2.5")
    try:
        position = suff.index('?')
        suff = suff[:position]
    except ValueError:
        pass

    return convert_path_name(part) + suff


def create_dir_for_links(path, url):
    try:
        dir_name = convert_path_name(url) + '_files'
        dir_path = Path(path) / dir_name
        Path(dir_path).mkdir()
        logger.debug(f'Function return {dir_path}')
        return dir_path
    except OSError as err:
        raise ErrorSystem('Error occurred!') from err


def get_path_for_tags(path):
    parts = Path(path).parts
    path = Path(parts[-2]) / parts[-1]
    logger.debug(f'parts: {parts}, return path: {str(path)} ')
    return str(path)
