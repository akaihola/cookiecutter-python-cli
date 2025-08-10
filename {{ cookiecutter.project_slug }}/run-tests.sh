#!/usr/bin/env bash

set -v

errors=0

if ! git diff --quiet pyproject.toml; then
    uv pip install -e '.' || errors=$?
fi

uv run {{ cookiecutter.project_slug }} --help || errors=$?
uv run {{ cookiecutter.project_slug }} --show-config || errors=$?

exit $errors
