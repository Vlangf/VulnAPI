FROM python:3.12.8-slim

RUN apt-get update && apt-get install -y supervisor && apt-get clean

WORKDIR /app
RUN pip install uv

COPY pyproject.toml /app/pyproject.toml
RUN uv pip install --no-cache-dir -r /app/pyproject.toml --system

COPY . /app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
