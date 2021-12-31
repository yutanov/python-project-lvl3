from page_loader.cli import get_parser
from page_loader import download, PageLoadingError
from page_loader.logging import logging
import sys


def main():
    parser = get_parser()
    args = parser.parse_args()
    try:
        file_path = download(args.url, args.output)
        print(f'Page saved in {file_path}')
    except PageLoadingError as e:
        logging.error(e.error_message)
        sys.exit(1)
    except PermissionError:
        logging.error('Not enough access rights')
        sys.exit(1)
    except FileNotFoundError:
        logging.error('No such file or directory')
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
