# -*- coding: utf-8 -*-

"""Local resources."""
import logging
import os

from page_loader.common import LOCAL_RESOURCES, create_dir, get_url, save
from page_loader.names import create_resource_name
from progress.bar import IncrementalBar

log = logging.getLogger(__name__)


def download_resources(resources, base_url, resources_dir_name):
    """Download local resources.

    Args:
        resources: list of resource names
        base_url: string, base url of resource
        resources_dir_name: string, output dir name
    """
    log.info('Saving local resources ...')
    create_dir(resources_dir_name)
    total_items = len(resources)

    with IncrementalBar('Downloading:', max=total_items) as progbar:
        progbar.suffix = '%(percent).1f%% (eta: %(eta)s)'  # noqa: WPS323
        for r in resources:
            url = f'{base_url}{r["old_value"]}'
            path = os.path.join(resources_dir_name, r['new_value'])
            save(path, get_url(url).content, 'wb')
            progbar.next()  # noqa: B305


def find_resources(soup, path):  # noqa: WPS231
    """Find local resources and replace paths in soup object.

    Args:
        soup: beautifulSoup object
        path: resource path

    Returns:
        tuple: beautifulSoup object, list of resources
    """
    resources = []
    for tag, attr in LOCAL_RESOURCES.items():
        for node in soup.find_all(tag):
            attr_val = node.get(attr)
            if attr_val is not None and attr_val.startswith('/'):
                base, ext = os.path.splitext(attr_val)
                if ext:
                    new_attr_val = create_resource_name(attr_val)
                    resources.append(
                        {'old_value': attr_val, 'new_value': new_attr_val},
                    )
                    node[attr] = os.path.join(path, new_attr_val)
    log.info(f'Found {len(resources)} local resource(s) to save.')
    return (soup, resources)
