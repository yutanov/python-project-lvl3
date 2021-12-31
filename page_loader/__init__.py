import os
import requests
from page_loader.url import to_file_name
from page_loader.storage import save
from page_loader.resources import download_resources
from page_loader.assets import prepare_assets
import logging


class PageLoadingError(requests.exceptions.HTTPError):
    def __init__(self, error_message):
        self.error_message = error_message


def download(base_url, output_path):
    path_to_file = os.path.join(output_path, to_file_name(base_url))
    try:
        request = requests.get(base_url)
        requests.Response.raise_for_status(request)
    except requests.exceptions.HTTPError as e:
        raise PageLoadingError(e) from e

    dir_path = os.path.splitext(path_to_file)[0] + '_files'
    resources, page = prepare_assets(base_url, request.text, dir_path)
    save(page, path_to_file)

    if os.path.isdir(dir_path):
        logging.warning(f'{dir_path} already exists. Content can be changed')
    else:
        os.mkdir(dir_path)

    if resources:
        download_resources(resources, dir_path)
    return path_to_file
