FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir loguru

RUN mkdir -p /var/log

ENV PATH="/app/venv/bin:$PATH"

CMD ["python", "app.py"]
