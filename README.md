# Page loader

[![Github Actions Status](https://github.com/altvec/python-project-lvl3/workflows/Python%20CI/badge.svg)](https://github.com/altvec/python-project-lvl3/actions)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Maintainability](https://api.codeclimate.com/v1/badges/48644f081f215379ebad/maintainability)](https://codeclimate.com/github/altvec/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/48644f081f215379ebad/test_coverage)](https://codeclimate.com/github/altvec/python-project-lvl3/test_coverage)

This is a CLI utility for downloading the specified webpage from the Internets.

## Installation

``` bash
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ altvec-page-loader
```

## Usage

``` bash
usage: page-loader [-h] [-o OUTPUT] [-l {INFO,DEBUG}] url

Page loader

positional arguments:
  url

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        set output directory
  -l {INFO,DEBUG}, --log-level {INFO,DEBUG}
                        set log level
```

## Downloading simple webpage

``` bash
page-loader --output . http://example.com
```

[![asciicast](https://asciinema.org/a/CNIZ4DO7kT0wNqTcm3QbMybTe.svg)](https://asciinema.org/a/CNIZ4DO7kT0wNqTcm3QbMybTe)

## Downloading webpage with local resources

``` bash
page-loader -o /tmp/ https://ru.hexlet.io/courses
```

[![asciicast](https://asciinema.org/a/Xk6o4tNfi5VQyLKtpqQzrbzhk.svg)](https://asciinema.org/a/Xk6o4tNfi5VQyLKtpqQzrbzhk)

## Downloadig webpage with local resources and DEBUG mode

``` bash
page-loader -o /tmp/ -l DEBUG https://ru.hexlet.io/courses
```

[![asciicast](https://asciinema.org/a/PvfKaog7eyr5dbiEifmdvwLz3.svg)](https://asciinema.org/a/PvfKaog7eyr5dbiEifmdvwLz3)
