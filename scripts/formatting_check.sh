#!/bin/bash
set -Eeuo pipefail
cd "$(dirname "$(readlink -f "$0")")"/..

PYTHON_EXECUTABLE=python3

$PYTHON_EXECUTABLE -m black . && $PYTHON_EXECUTABLE -m isort .

git_output="$(git status --porcelain)"

if [[ -n "${git_output}" ]]; then
  echo "Exiting with non-zero status, because repo is not clean:"
  echo
  git status -s
  exit 1
else
  echo "No changes to the repo were made, exiting with 0"
fi
