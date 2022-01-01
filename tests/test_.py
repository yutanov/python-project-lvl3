import os
import pytest
import requests
import requests.exceptions
from pathlib import Path
from bs4 import BeautifulSoup # noqa
from page_loader.custom_exseptions import BadConnect, ErrorSystem
from page_loader.page_loader import download
from page_loader.web_data_processing import load_link_in_local_dir
from page_loader.normalize_data import (
    convert_path_name, convert_relative_link, add_suff_for_name_link
)


@pytest.mark.parametrize(
    'url, correct_value',
    [
        ('https://ru.hexlet.io/courses',
         'ru-hexlet-io-courses'),
        ('http://ru.hexlet.io/courses',
         'ru-hexlet-io-courses'),
        ('https://ru.hexlet.io/courses/page.html',
         'ru-hexlet-io-courses-page-html'),
        ('http://ru.hexlet.io/courses.page.html',
         'ru-hexlet-io-courses-page-html'),
        ('//ru.hexlet.io/courses',
         '--ru-hexlet-io-courses'),
    ]
)
def test_convert_path_name(url, correct_value):
    assert convert_path_name(url) == correct_value


@pytest.mark.parametrize(
    'link, correct_value',
    [
        ('https://ru.hexlet.io/courses',
         'https://ru.hexlet.io/courses'),
        ('/courses',
         'https://ru.hexlet.io/courses'),
        ('//ru.hexlet.io/courses',
         'https://ru.hexlet.io/courses'),
        ('//test.com/courses',
         '//test.com/courses')
    ]
)
def test_convert_relativ_link(link, correct_value):
    url = 'https://ru.hexlet.io/courses'
    assert convert_relative_link(link, url) == correct_value


def test_http_error(requests_mock, tmp_path):
    url = 'http://test404.com'
    dir_temp = tmp_path / 'sub'
    requests_mock.get(url, status_code=404)
    with pytest.raises(BadConnect):
        download(url, dir_temp)


def test_dir_exist(requests_mock, tmp_path):
    url = 'http://test.com'
    dir_temp = tmp_path / 'sub'
    requests_mock.get('http://test.com')
    with pytest.raises(ErrorSystem):
        download(url, dir_temp)


def test_bad_url(tmp_path):
    url = 'hps://test.com'
    dir_temp = tmp_path / 'sub'
    with pytest.raises(BadConnect):
        download(url, dir_temp)


def test_img_diff(requests_mock, tmp_path):
    data = {'http://test.com/img.jpg': 'tests/fixtures/img_web.jpg'}
    for link, path_for_link in data.items():
        with open(path_for_link, 'rb') as fo:
            content = fo.read()
        requests_mock.get(link, content=content)

    dir_temp = tmp_path / 'sub'
    dir_temp.mkdir()
    img_path = str(
        Path(dir_temp) / add_suff_for_name_link('http://test.com/img.jpg')
    )
    new_data = {'http://test.com/img.jpg': img_path}

    load_link_in_local_dir(new_data)
    for testing_file in data.values():
        with open(testing_file, 'rb') as f:
            img = f.read()

    assert img == requests.get(link).content


@pytest.fixture
def get_internet_file():
    page_from_internet = open('tests/fixtures/web_page_link.html',
                              'r', encoding='utf-8')
    text = page_from_internet.read()
    yield text
    page_from_internet.close()


@pytest.fixture
def get_check_file():
    check_page = open('tests/fixtures/web_page_result.html',
                      'r', encoding='utf-8')
    text = check_page.read()
    yield text
    check_page.close()


@pytest.fixture
def get_load_page(requests_mock, get_internet_file, tmp_path):
    requests_mock.get('http://test.com', text=get_internet_file)
    requests_mock.get('http://test.com/assets/application.css')
    requests_mock.get('http://test.com/courses')
    requests_mock.get('http://test.com/assets/professions/nodejs.png')
    requests_mock.get('http://test.com/packs/js/runtime.js')
    result = download('http://test.com', tmp_path)
    link_count = sum(len(files) for _, _, files in os.walk(tmp_path))
    with open(result, 'r', encoding='utf-8') as file:
        page_result = file.read()
    return page_result, link_count


def test_download(get_load_page, get_check_file):
    res, _ = get_load_page
    assert res == get_check_file


def test_number_links(get_load_page):  # checking by the number of links
    _, numb = get_load_page
    assert numb == 5
