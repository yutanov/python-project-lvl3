from pathlib import Path
import requests
import logging.config
from bs4 import BeautifulSoup
from page_loader.custom_exseptions import BadConnect, ErrorSystem
from progress.bar import Bar
from page_loader.settings_logging import logger_config
from page_loader.normalize_data import (
    convert_relative_link, get_path_for_tags,
    add_suff_for_name_link, convert_path_name, is_local_link
)


logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

ATTR_TAGS = ['href', 'src']
TAGS = {
    'script': 'src',
    'link': 'href',
    'img': 'src'
}


def get_response_server(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        # assert type(response) is not None
        # # ! https://www.rupython.com/63038-63038.html
        return response
    except requests.RequestException as error:
        logger.exception(error)
        raise BadConnect('Connection Error occurred!') from error


def get_soup(url):
    html_doc = get_response_server(url).text
    soup = BeautifulSoup(html_doc, "html.parser")
    return soup


def edit_tags_with_relative_link(dir_to_download, url, soup):
    links_to_load = {}

    for k, v in TAGS.items():
        for link in soup.find_all({k: v}):
            for attribute in ATTR_TAGS:
                url_tag = link.attrs.get(attribute)

                if not url_tag:
                    continue

                url_tag = convert_relative_link(url_tag, url)

                if is_local_link(url_tag, url):
                    link_path = str(
                        Path(dir_to_download) / add_suff_for_name_link(url_tag)
                    )
                    link[attribute] = link_path
                    links_to_load[url_tag] = link[attribute]
                    # long path to save to the dictionary links_to_load
                    link[attribute] = get_path_for_tags(link_path)
                    # short path to save to the soup
                    logger.debug(f'Change attribute tag {attribute} '
                                 f'to {url_tag}')
                else:
                    continue
            else:
                logger.debug(f'{attribute} not found in {url}')
    return soup, links_to_load


def load_link_in_local_dir(links_to_load):
    for link, path_for_link in links_to_load.items():
        bar = Bar(f'Download {link}...', suffix='%(percent)d%%', color='blue')
        response = get_response_server(link)

        try:
            with open(path_for_link, 'wb') as file:
                for chunk in response.iter_content(chunk_size=10000):
                    file.write(chunk)
                    file.flush()  # Cброс данных из буфера в файл
                    bar.next()
            bar.finish()
            logger.debug(f'Download link {link}')
        except OSError as error:
            logger.exception(error)
            raise ErrorSystem('Error occurred!') from error

    logger.debug('Links saved in local directory')


def save_content(dir_for_links, url, soup):
    soup, links_to_load = edit_tags_with_relative_link(
        dir_for_links, url, soup
    )

    new_html = soup.prettify()
    web_page = Path(dir_for_links.parent) / (convert_path_name(url) + '.html')

    try:
        Path(web_page).write_text(new_html)
    except OSError as error:
        logger.exception(error)
        raise ErrorSystem('Error occurred!') from error

    load_link_in_local_dir(links_to_load)

    return str(web_page)
