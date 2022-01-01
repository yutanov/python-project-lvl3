#! /usr/bin/env python3

from page_loader.name import gen_name
from page_loader.download import get_obj_and_change, download_obj
from page_loader.maker import make_page_dir, make_files_dir
import os

SITE_URL = 'https://riptutorial.com'
FILE_DIR = 'riptutorial-com_files'
OUTPUT = 'riptutorial'
RESOURSES_LIST = [
    {'old_value': '/Images/logo_rip_full_white.png', 'new_value': 'images-logo-rip-full-white.png'},
    {'old_value': '/Images/logo_rip_full_white.png', 'new_value': 'images-logo-rip-full-white.png'},
    {'old_value': '//m2d.m2.ai/pghb.riptutorial.home.js', 'new_value': 'm2d-m2-ai-pghb-riptutorial-home.js'},
    {'old_value': '/Images/logo_rip.png', 'new_value': 'images-logo-rip.png'},
    {'old_value': '/assets/css/master.min.css?v=1.0.0.21822', 'new_value': 'assets-css-master-min-css-v-1-0-0.21822'},
]


def test_gen_name():
    name = 'riptutorial-com'
    url = 'https://riptutorial.com'
    generated_name = gen_name(url)
    assert generated_name == name


def test_get_obj_and_change():
    make_page_dir(OUTPUT)
    file_dir = make_files_dir(SITE_URL, OUTPUT)
    resources = get_obj_and_change(SITE_URL, file_dir, OUTPUT)
    assert RESOURSES_LIST == resources


# def test_download():
#    list_of_objects = [
#    'images-logo-rip-full-white.png',
#    'images-logo-rip.png',
#    'm2d-m2-ai-pghb-riptutorial-home.js',
#    'assets-css-master-min-css-v-1-0-0.21822',
#    ]
#    download_obj(RESOURSES_LIST, SITE_URL, FILE_DIR)
#    list_of_downloaded = os.listdir('riptutorial/riptutorial-com_files')
#    assert list_of_objects == list_of_downloaded


def test_download():
    make_page_dir(OUTPUT)
    file_dir = make_files_dir(SITE_URL, OUTPUT)
    resources = get_obj_and_change(SITE_URL, file_dir, OUTPUT)
    download_obj(resources, SITE_URL, file_dir)
    name = gen_name(SITE_URL) + '.html'
    file_path = os.path.join(OUTPUT, name)
    f_test = open(file_path)
    file_example = 'tests/fixtures/riptutorial-com.html'
    f_example = open(file_example)
    assert f_test.read() == f_example.read()
