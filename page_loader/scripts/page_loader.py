#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Page loader script."""

import sys

from page_loader.cli import make_parser
from page_loader.downloader import download
from page_loader.logging import configure_logger


def main():
    """Download and save specified webpage."""
    args = make_parser().parse_args()
    configure_logger(args.log_level)
    try:
        download(args.output, args.url)
    except Exception as e:
        if 'url' in str(e.args):
            sys.exit(1)
        elif 'Permission denied' in str(e.args):
            sys.exit(2)
    sys.exit(0)


if __name__ == '__main__':
    main()
