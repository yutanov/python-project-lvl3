#! /usr/bin/env python3

from page_loader.parser import arg_parser
# from page_loader.name import gen_name
from page_loader.maker import make_page_dir, make_files_dir
from page_loader.pager import download_page
import logging
import sys
import os


logging.basicConfig(
    filename='example.log', encoding='utf-8',
    # handlers=[logging.StreamHandler(sys.stdout)],
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    )


def download(site_url, file_dir, output):
    page = download_page(site_url, file_dir, output)
    return page


def main():
    try:
        site_url = arg_parser().parse_args().url
        output = arg_parser().parse_args().output
        if output is None:
            output = os.getcwd()
        make_page_dir(output)
        file_dir = make_files_dir(site_url, output)
        download(site_url, file_dir, output)
        #resources = get_obj_and_change(site_url, file_dir, output)
        #download_obj(resources, site_url, file_dir)
    except Exception as e:
        if 'url' in str(e.args):
            print('Wrong URL')
            sys.exit(1)
        elif 'Permission denied' in str(e.args):
            print('Permission denied to the specified directory')
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
