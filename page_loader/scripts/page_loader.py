#!/usr/bin/env python

import sys
import logging.config
from page_loader.page_loader import download
from page_loader.cli import create_parser
from page_loader.settings_logging import logger_config
from page_loader.custom_exseptions import AppInternalError


logging.config.dictConfig(logger_config)


def main():
    logger = logging.getLogger('app_logger')
    my_parser = create_parser()
    args = my_parser.parse_args()

    try:
        result = download(args.url, args.output)
        print()
        print('Page was successfully downloaded into -> ',
              result, end='\n\n')
        logger.debug('Finished')
        sys.exit(0)
    except AppInternalError as error:
        logger.exception(error)
        sys.exit(f'{error}')


if __name__ == '__main__':
    main()
