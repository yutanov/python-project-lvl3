from bs4 import BeautifulSoup
from pathlib import Path
# from urllib.parse import urlparse
# from page_loader.maker import make_files_dir
from page_loader.name import gen_name
from progress.bar import IncrementalBar
import logging
import requests
import os
import sys


log = logging.getLogger(__name__)
CURRENT_DIR = os.getcwd()
TAG_DICT = {
    "img": "src",
    "script": "src",
    "link": 'href',
}


def check_status(page):
    status = page.status_code
    if status != 200:
        print('Error! Status is not 200')
        sys.exit(1)
    return


def download_obj(resources, site_url, file_dir):
    with IncrementalBar('Downloading:', max=len(resources)) as progbar:
        for el in resources:
            url = f'{site_url}{el["old_value"]}'
            path = os.path.join(file_dir, el['new_value'])
            with open(path, 'wb') as f:
                f.write(requests.get(url).content)
            progbar.next()
    log.debug('Odjects downloaded')


def get_obj_and_change(site_url, file_dir, output):
    resources = []
    page = requests.request('GET', site_url)
    # status = check_status(page)
    check_status(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    for tag, source in TAG_DICT.items():
        for el in soup.find_all(tag):
            source_value = el.get(source)
            if source_value is not None and source_value.startswith('/'):
                base, ext = os.path.splitext(source_value)
                if ext:
                    new_value = f'{gen_name(base)}{ext}'
                    resources.append(
                        {'old_value': source_value, 'new_value': new_value},
                    )
                    el[source] = os.path.join(os.getcwd(), file_dir, new_value)
    name = gen_name(site_url) + '.html'
    web_page = Path(output) / name
    Path(web_page).write_text(soup.prettify())
    # with open(os.path.join(output, name), 'w') as p:
    #    p.write(str(soup.prettify()))
    log.debug('Page is changed')
    return resources
