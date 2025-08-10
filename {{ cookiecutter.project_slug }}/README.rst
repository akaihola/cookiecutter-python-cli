{{ cookiecutter.project_slug }}
====

{{ cookiecutter.project_slug }} is a command line tool that ...

Features
--------

- ...

Installation
------------

To install {{ cookiecutter.project_slug }}, you need to have Python 3.11 or higher.
You can install the package using e.g. ``pip``, ``uv`` or ``pipx``::

    pip install {{ cookiecutter.project_slug }}
    uv pip install {{ cookiecutter.project_slug }}
    uv tool install {{ cookiecutter.project_slug }}
    pipx install {{ cookiecutter.project_slug }}

Then simply run::

    {{ cookiecutter.project_slug }} --help

Or, you can skip installing and just run it using ``uvx``::

    uvx {{ cookiecutter.project_slug }} --help


Development
-----------

To contribute to the development of {{ cookiecutter.project_slug }}, follow these steps:

1. Clone the repository::

    git clone git@gihub.com:akaihola/{{ cookiecutter.project_slug }}
    cd {{ cookiecutter.project_slug }}

2. Create a virtualenv and install the dependencies::

    uv sync

3. Make your changes and run the tests::

    bash run-tests.sh

License
-------

This project is licensed under the MIT License.
