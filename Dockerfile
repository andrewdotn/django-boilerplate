FROM node:18-alpine AS frontend-builder

COPY frontend/package.json frontend/yarn.lock ./
RUN yarn

COPY frontend .
RUN node_modules/.bin/vite build


FROM python:3.10-slim AS python-builder

# build-essential is needed for uwsgi
RUN apt update && apt install -y build-essential && rm -rf /var/lib/apt/lists

RUN pip install pipenv

RUN mkdir /app
WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install


FROM python:3.10-slim AS python-run

RUN apt update && apt install -y \
    tini \
    media-types `# for uwsgi static serving` \
    sqlite3 `# for maintenance, init` \
    && rm -rf /var/lib/apt/lists

RUN mkdir /app
WORKDIR /app

COPY --from=python-builder /app /app

COPY . .

RUN mkdir frontend/static && mkdir frontend/static/dist
COPY --from=frontend-builder static/dist frontend/static/dist

ENV DJANGO_SETTINGS_MODULE=website.prod_settings

ENV PATH=/app/.venv/bin:${PATH}

RUN ./manage.py collectstatic

ENTRYPOINT ["tini", "--"]

CMD uwsgi --uwsgi-socket=0.0.0.0:8001 \
    --need-app --wsgi-file=website/wsgi.py \
    --check-static public --static-map=/media=media
