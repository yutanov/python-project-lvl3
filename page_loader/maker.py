from page_loader.name import gen_name
import logging
import os
import sys

log = logging.getLogger(__name__)


def make_page_dir(output):
    cur_dir = os.getcwd()
    path = os.path.join(cur_dir, output)
    if os.path.exists(path) is False:
        try:
            os.makedirs(path)
        except:
            log.debug('Page directory is created')
            raise('Wrong directory!')
            sys.exit(1)
    log.debug('Page directory is created')


def make_files_dir(site_url, output):
    file_dir = gen_name(site_url) + '_files'
    path = os.path.join(output, file_dir)
    if os.path.exists(path) is False:
        os.makedirs(path)
    log.debug('Files directory is created')
    return path
