Инструкция по запуску проекта:

   1. python3 -m venv .venv
   2. source .venv/bin/activate
   3. pip3 install -r req.txt
   4. alembic upgrade head
   5. uvicorn src.main:app

   ИЛИ

   1. ./start.sh

Сервер будет запущен на 127.0.0.1:8000