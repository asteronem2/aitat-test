#!/bin/bash

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r req.txt -q

alembic upgrade head

uvicorn src.main:app
