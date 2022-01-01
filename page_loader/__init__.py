#! /usr/bin/env python3

from page_loader.pager import download_page
import os

NAME = 'page_loader'


def download(site_url, file_dir, output):
    if output is None:
        output = os.getcwd()
    page = download_page(site_url, file_dir, output)
    return page
