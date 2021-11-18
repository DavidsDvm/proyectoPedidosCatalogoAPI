FROM alpine:3.13.6

RUN apk add --no-cache python3-dev \
    && apk add py3-pip \
    && apk add postgresql-dev gcc \
    && apk add g++ \
    && pip3 install --upgrade pip 

WORKDIR /app

ENV PORT=$PORT

COPY . /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 --no-cache-dir install -r requirements.txt

RUN alembic upgrade head

EXPOSE $PORT

CMD uvicorn src.main:app --host 0.0.0.0 --port $PORT