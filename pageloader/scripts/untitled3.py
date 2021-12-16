from bs4 import BeautifulSoup
from urllib.parse import urlparse
from progress.bar import Bar
import requests
import string
import argparse
import os
import logging
import sys


BAR = Bar('Processing', max=10, suffix='%(percent)d%%')
CURRENT_DIR = os.getcwd()
logging.basicConfig(
    filename='example.log', encoding='utf-8',
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', level=logging.DEBUG,
    )


def check_status(page):
    status = page.status_code
    if status != 200:
        sys.exit('Error! Status is not 200')
    return status


def get_obj(page):
    BAR.next()
    soup = BeautifulSoup(page, 'html.parser')
    img_tags = soup.find_all('img')
    return img_tags, soup


def make_page_dir(output):
    BAR.next()
    cur_dir = os.getcwd()
    path = os.path.join(cur_dir, output)
    if os.path.exists(path) == False:
        os.makedirs(path)


def make_files_dir(site_url):
    BAR.next()
    file_dir = gen_name(site_url) + '_files'
    if os.path.exists(file_dir) == False:
        os.makedirs(file_dir)
    FILES_DIR = file_dir
    return file_dir


def change_page(url_list, site_url, output, file_dir):
    BAR.next()
    page = requests.request('GET', site_url)
    status = check_status(page)
    page = page.text
    img_tags, soup = get_obj(page)
    path = os.path.join(CURRENT_DIR, output)
    name = gen_name(site_url) + '.html'
    for i, tag in enumerate(img_tags):
        tag['src'] = file_dir + '/' + url_list[i]
    page = str(soup)
    with open(os.path.join(path, name), 'w') as p:
        p.write(page)
    print('\nDone')


def get_img(site_url):
    BAR.next()
    page = requests.request('GET', site_url).text
    img_tags, soup = get_obj(page)
    urls = [img['src'] for img in img_tags]
    file_dir = make_files_dir(site_url)
    os.chdir(file_dir)
    url_list = []
    for url in urls:
        if 'http' not in url:
            url = site_url + url
        response = requests.get(url)
        f_name = urlparse(url)
        filename, file_extension = os.path.splitext(f_name.path)
        file_name = gen_name(filename) + file_extension
        with open(file_name, 'wb') as f:
            f.write(response.content)
        url_list.append(file_name)
    return url_list, file_dir


def main():
    BAR.next()
    site_url = arg_parser().parse_args().url
    output = arg_parser().parse_args().output
    if output[:1] == '/':
        output = output[1:]
    make_page_dir(output)
    url_list, file_dir = get_img(site_url)
    change_page(url_list, site_url, output, file_dir)


def arg_parser():
    BAR.next()
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('--output', help='Enter path')
    parser.add_argument('url', help='Enter url')
    args = parser.parse_args()
    return parser


def gen_name(url):
    BAR.next()
    url = url.lower()
    low_letters = string.ascii_lowercase
    nums = [str(i) for i in range(10)]
    name = ''
    if url[:8] == 'https://':
        url = url[8:]
    elif url[:7] == 'http://':
        url = url[7:]
    elif url[:2] == '//':
        url = url[2:]
    elif url[:1] == '/':
        url = url[1:]
    for sym in url:
        if sym in low_letters or sym in nums:
            name += sym
        else:
            name += '-'
    return name


if __name__ == "__main__":
    main()
