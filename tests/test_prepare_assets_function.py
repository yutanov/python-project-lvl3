import sys
import requests_mock
from page_loader.assets import prepare_assets
import os
from urllib.parse import urljoin
import requests
import tempfile


BASE_URL = 'https://test.com'
DIR_NAME = 'test-com_files'
RESOURCES_URL = [urljoin(BASE_URL, '/assets/application.css'),
                 urljoin(BASE_URL, '/assets/professions/nodejs.png'),
                 urljoin(BASE_URL, '/runtime.js')]

EXPECTED_CONTENT = RESOURCES_URL[:]


with open(os.path.join(sys.path[0], 'fixtures/page_after.html'), 'r') as file:
    expected_page = file.read()


def test_page_loading():
    with open(os.path.join(sys.path[0], 'fixtures/page_before.html'),
              'r') as file:
        testing_page = file.read()
    with tempfile.TemporaryDirectory() as tmpdirname:
        with requests_mock.Mocker() as m:
            m.get(BASE_URL, text=testing_page)
            [m.get(url, text=content) for url, content
             in zip(RESOURCES_URL, EXPECTED_CONTENT)]
            resources, page = prepare_assets(BASE_URL, testing_page,
                                             os.path.join(tmpdirname,
                                                          DIR_NAME))
            for resource, content in zip(resources, EXPECTED_CONTENT):
                link, _ = resource
                assert requests.get(link).text == content
            assert page == expected_page
