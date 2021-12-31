import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(description='page loader')
    parser.add_argument('url', type=str, help='name of website address')
    parser.add_argument('-o', '--output', type=str, default=os.getcwd(),
                        help='output directory')

    return parser
