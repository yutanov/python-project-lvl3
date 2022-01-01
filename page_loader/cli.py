import argparse
import os


def create_parser():
    my_parser = argparse.ArgumentParser(
        description='download the page from the web')
    my_parser.add_argument(
        '-o', '--output',
        help='Specify the directory to save the page in'
        '(by default, in the program launch directory)',
        default=os.getcwd()
    )
    my_parser.add_argument('url', type=str, help='Add a download page')
    return my_parser
