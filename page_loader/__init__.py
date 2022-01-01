#! /usr/bin/env python3

from page_loader.pager import download_page

NAME = 'page_loader'

def download(site_url, file_dir, output):
    page = download_page(site_url, file_dir, output)
    return page
