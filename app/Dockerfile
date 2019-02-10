FROM python:3.6-slim

# System setup
ENV USER app
ENV dir /home/app

RUN useradd -ms /bin/bash ${USER}

# System dependencies
RUN  apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  git \
  libffi-dev \
  unzip \
  default-libmysqlclient-dev \
  ca-certificates

WORKDIR ${dir}

# App dependencies
COPY requirements.txt ${dir}/
RUN pip3 install -r requirements.txt

COPY api/ ${dir}/api/
COPY app.py ${dir}/app.py
COPY swagger.yaml ${dir}/swagger.yaml
COPY test/ ${dir}/test/

CMD python3 app.py
