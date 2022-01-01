### Hexlet tests and linter status:
[![Actions Status](https://github.com/Serggi0/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/Serggi0/python-project-lvl3/actions)  *Hexlet tests and linter status*

[![lint & test GitHub action for develop branch](https://github.com/Serggi0/python-project-lvl3/actions/workflows/github_action_.yaml/badge.svg)](https://github.com/Serggi0/python-project-lvl3/actions/workflows/github_action_.yaml)  *GitHub action badge*

<!-- [! [Статус действий YourActionName] (https://github.com/ { userName } / { repoName } / workflows / { workflowName } /badge.svg)] (https://github.com/ { userName } / { repoName } / action) -->

[![Maintainability](https://api.codeclimate.com/v1/badges/f6ba19bc9e1493dbd1ce/maintainability)](https://codeclimate.com/github/Serggi0/python-project-lvl3/maintainability)  *CodeClimate Maintainability badge*

[![Test Coverage](https://api.codeclimate.com/v1/badges/f6ba19bc9e1493dbd1ce/test_coverage)](https://codeclimate.com/github/Serggi0/python-project-lvl3/test_coverage)  *CodeClimate test coverage badge*

This is third training project on [Hexlet.io](https://ru.hexlet.io) course.

Page-loader is a command-line utility that downloads pages from the Internet and saves them on your computer. Together with the page, it downloads all the resources (images, styles, and js), allowing you to open the page without the Internet.

#### Usage

```Python
usage: page-loader [-h] [-o OUTPUT] url

download the page from the web

positional arguments:
  url                   Add a download page

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Specify the directory to save the page
                        in(by default, in the program launch
                        directory)
```

#### Examples of working the programm
```Python
page-loader --output path/to/dir URL
```

<details>
<summary> Stages of project preparation</summary>

#### Asciinema step1:
```Python
poetry run page-loader
```
[![asciicast](https://asciinema.org/a/7hYK6eUqGKHmGHrlfnqbkn1Yx.svg)](https://asciinema.org/a/7hYK6eUqGKHmGHrlfnqbkn1Yx)

#### Asciinema step2:
```Python
poetry run page-loader -h
```
[![asciicast](https://asciinema.org/a/hyWuuPyuYEXmKA5WBaRkU84gC.svg)](https://asciinema.org/a/hyWuuPyuYEXmKA5WBaRkU84gC)

#### Asciinema step3:
```Python
tree
```
[![asciicast](https://asciinema.org/a/426188.svg)](https://asciinema.org/a/426188)

#### Asciinema step4:
```Python
cat myapp.log
```
[![asciicast](https://asciinema.org/a/mGcD16tlA3LBYh8D82OlO8B14.svg)](https://asciinema.org/a/mGcD16tlA3LBYh8D82OlO8B14)

#### Asciinema step5:
```Python
make page-loader
```
[![asciicast](https://asciinema.org/a/bV12dNP1YviNbKM0AAYmXf3i4.svg)](https://asciinema.org/a/bV12dNP1YviNbKM0AAYmXf3i4)

#### Asciinema step6:
```Python
make page-loader 
```
[![asciicast](https://asciinema.org/a/gajXHWvoFj7Z6uwUSH9T5T8RL.svg)](https://asciinema.org/a/gajXHWvoFj7Z6uwUSH9T5T8RL)
</details>