FROM python:3.7-alpine3.7

# System setup
ENV dir /home/app

# System dependencies
RUN apk add --no-cache \
        musl \
        build-base \
        linux-headers \
        postgresql-dev \
        ca-certificates \
    && rm -rf /var/cache/apk/*

WORKDIR ${dir}

# App dependencies
COPY requirements.txt ${dir}/
RUN pip3 install -r requirements.txt

COPY api/ ${dir}/api/
COPY app.py ${dir}/app.py
COPY template/ ${dir}/template/
COPY test/ ${dir}/test/

EXPOSE 8000

CMD python3 app.py
