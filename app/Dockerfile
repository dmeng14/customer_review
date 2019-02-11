FROM python:3.6-slim

# System setup
ENV USER app
ENV APP_DIR=/home/app
ENV PYTHONPATH=$APP_DIR

RUN useradd -ms /bin/bash ${USER}

# System dependencies
RUN  apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  git \
  libffi-dev \
  unzip \
  default-libmysqlclient-dev \
  ca-certificates

WORKDIR $APP_DIR

# App dependencies
COPY requirements.txt $APP_DIR/
RUN pip3 install -r requirements.txt

COPY api/ $APP_DIR/api/
COPY app.py $APP_DIR/app.py
COPY swagger.yaml $APP_DIR/swagger.yaml
COPY test/ $APP_DIR/test/

CMD python3 app.py
