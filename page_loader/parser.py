import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str, help='Enter url')
    parser.add_argument('-o', '--output', type=str, help='Enter path')
    return parser
