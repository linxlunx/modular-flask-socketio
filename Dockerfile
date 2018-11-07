FROM python:3.6-alpine as base

FROM base as builder

# install gcc to compile greenlet and musl-dev for limit.h header
RUN apk update && apk add gcc musl-dev

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

ADD . /opt/app
WORKDIR /opt/app

CMD ["python", "run.py"]
