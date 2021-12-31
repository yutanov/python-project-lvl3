from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin
from page_loader.url import to_file_name


tags = {'link': 'href', 'img': 'src', 'script': 'src'}


def prepare_assets(base_url, page, dir_path):
    dir_path, dir_name = os.path.split(dir_path)
    soup = BeautifulSoup(page, 'html.parser')
    resources = []
    elements = filter(lambda x: is_local(x, base_url),
                      soup.find_all(list(tags)))
    for element in elements:
        tag = tags[element.name]
        link = urljoin(base_url, element.get(tag))
        resource_path = os.path.join(dir_name, to_file_name(link))
        element[tag] = resource_path
        resources.append((link, os.path.join(dir_path, resource_path)))
    return resources, soup.prettify(formatter='html5')


def is_local(element, base_url):
    link = element.get(tags[element.name])
    netloc1 = urlparse(base_url).netloc
    netloc2 = urlparse(urljoin(base_url, link)).netloc
    return netloc1 == netloc2
