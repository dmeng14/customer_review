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

COPY ingester/ ${dir}/ingester/
COPY test/ ${dir}/test/
COPY run.sh ${dir}/

RUN chown -R ${USER}: ${dir}

# App setup
USER ${USER}

CMD ["./run.sh"]
