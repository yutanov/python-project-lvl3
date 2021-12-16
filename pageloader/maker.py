from pageloader.name import gen_name
import logging
import os

log = logging.getLogger(__name__)


def make_page_dir(output):
    cur_dir = os.getcwd()
    path = os.path.join(cur_dir, output)
    if os.path.exists(path) == False:
        os.makedirs(path)
    log.debug('Page directory is created')


def make_files_dir(site_url):
    file_dir = gen_name(site_url) + '_files'
    if os.path.exists(file_dir) == False:
        os.makedirs(file_dir)
    FILES_DIR = file_dir
    log.debug('Files directory is created')
    return file_dir
