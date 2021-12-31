import requests
from progress.bar import IncrementalBar
from page_loader.storage import save


def download_resources(resources, dir_path):
    bar = IncrementalBar('Resources loading: ', max=len(resources))
    for resource in resources:
        link, resource_path = resource
        save(requests.get(link).content, resource_path, mode='wb')
        bar.next()
    bar.finish()
