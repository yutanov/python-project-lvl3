from page_loader.web_data_processing import (get_soup, save_content)
from page_loader.normalize_data import create_dir_for_links


def download(url, path):
    soup = get_soup(url)
    dir_for_links = create_dir_for_links(path, url)
    result = save_content(dir_for_links, url, soup)
    return result
