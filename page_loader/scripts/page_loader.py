#! /usr/bin/env python3

from page_loader.parser import arg_parser
from page_loader.maker import make_page_dir, make_files_dir
from page_loader import download
import logging
import sys


logging.basicConfig(
    filename='example.log', encoding='utf-8',
    # handlers=[logging.StreamHandler(sys.stdout)],
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    )


def main():
    site_url = arg_parser().parse_args().url
    output = arg_parser().parse_args().output

    try:
        make_page_dir(output)
        file_dir = make_files_dir(site_url, output)
        download(site_url, file_dir, output)
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
