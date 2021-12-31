# -*- coding: utf-8 -*-

"""Basic tests."""

import os
from tempfile import TemporaryDirectory

import pytest
from requests.exceptions import HTTPError

from page_loader.downloader import download
from page_loader.cli import make_parser


def read_file(path):
    with open(path) as f:
        return f.read()


@pytest.mark.parametrize('args', (
    ['-o', '/tmp/', 'https://example.com'],
    ['--output', '/tmp/', 'https://example.com'],
    ['-o', '/tmp/', '-l', 'INFO', 'https://example.com'],
    ['-o', '/tmp/', '-l', 'DEBUG', 'https://example.com'],
))
def test_parse_args(args):
    make_parser().parse_args(args)


def test_download():
    with TemporaryDirectory() as tmpdir:
        download(tmpdir, 'http://example.com')
        actual = read_file(os.path.join(tmpdir, 'example-com.html'))
        expected = read_file('./tests/fixtures/example-com.html')
        assert actual == expected


def test_has_local_resources():
    with TemporaryDirectory() as tmpdir:
        download(tmpdir, 'https://clojure.org')
        expected = os.path.join(
            tmpdir,
            'clojure-org_files',
        )
        assert len(os.listdir(os.path.join(expected))) != 0


def test_404_exception():
    with TemporaryDirectory() as tmpdir:
        with pytest.raises(HTTPError) as excinfo:
            url = 'https://grishaev.me/bookshelf2'
            download(tmpdir, url)
        assert '404 Client Error' in str(excinfo.value)


def test_permissions_exception():
    with TemporaryDirectory() as tmpdir:
        os.chmod(tmpdir, 400)
        with pytest.raises(PermissionError) as excinfo:
            url = 'https://hexlet.io/courses'
            download(tmpdir, url)
        assert 'Permission denied' in str(excinfo.value)
