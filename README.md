<a href="https://codeclimate.com/github/Nikita-Illarionov/python-project-lvl3/maintainability"><img src="https://api.codeclimate.com/v1/badges/3f2999a606af6dbeef98/maintainability" /></a>

<a href="https://codeclimate.com/github/Nikita-Illarionov/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/3f2999a606af6dbeef98/test_coverage" /></a>

<a href="https://github.com/Nikita-Illarionov/python-project-lvl3/actions"><img src="https://github.com/Nikita-Illarionov/python-project-lvl3/workflows/Travis_CI/badge.svg" /></a>

### Hexlet tests and linter status:
![Actions Status](https://github.com/Nikita-Illarionov/python-project-lvl3/workflows/hexlet-check/badge.svg)

page-loader - утилита, которая скачивает страницу из сети и кладет ее в указанную директорию (по умолчанию в директорию запуска программы).
~~~
$ page-loader --output=/var/tmp https://hexlet.io/courses
$ open /var/tmp/hexlet-io-courses.html
~~~

Инструкция по установке и использованию:
 - Установите виртуальное окружение, в котором будет утилита
~~~
python -m venv test_venv
~~~
 - Обновите pip (рекомендуется); убедитесь, что библиотека requests имеет версию >= 2.25.0
 - Скачайте пакет
~~~
test_venv/bin/pip install -i https://test.pypi.org/simple/ nikita-illarionov-hexlet-code
~~~
 - Утилита page-loader имеет необязательный параметр -o (--output) - директория, в которую будет помощен html файл (по умолчанию это директория, из которой запускается программа). Обязательный параметр - адрес сайта.
~~~
$ page-loader https://hexlet.io
~~~
 - после установки в указанной директории (либо в текущей, если она не была указана) будет файл с расширением html, который и будет являться сохраненной страницей.

Видео-пример установки и использования утилиты page-loader:

https://asciinema.org/a/PFMtEefhrrANCCTg0hifKkAF8

Пример использования утилиты:

https://asciinema.org/a/ggUvqUqcWX4qGlwfDEaslaS28

Пример использования утилиты с предупреждениями и исключениями:

https://asciinema.org/a/Mm2026Xq8935nfOEtVUxEDUAL
