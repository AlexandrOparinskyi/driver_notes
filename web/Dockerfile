FROM python:3.12-slim

WORKDIR app/

COPY web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY web/ ./web/
COPY bot/ ./bot/
COPY database/ ./database/
COPY config.py .

CMD uvicorn web.connect:app --host "0.0.0.0" --port 8000 --proxy-headers