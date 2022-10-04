FROM python:3.10-slim

RUN set -ex; \
    apt-get update; \
    apt-get upgrade -y; \
    apt-get install -y --no-install-recommends \
        curl wget \
        vim joe \
        less \
        procps htop \
        net-tools \
        dnsutils \
        iproute2 \
        tcpdump \
        unzip libarchive-tools \
        build-essential \
        libcairo2 \
        libpq-dev \
        libffi-dev \
        postgresql-client \
        libxml2-dev libxmlsec1-dev libxmlsec1-openssl pkg-config \
        default-libmysqlclient-dev; \
    pip install --upgrade pip; \
    # apt-get purge -y --auto-remove build-essential linux-libc-dev libc-dev libxml2-dev libxmlsec1-dev pkg-config; \
    rm -rf /var/lib/apt/lists/*

# Install dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN curl -qsL https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    | tar -C /usr/local/bin -xzvvf -

CMD ["/bin/bash"]

# Make dev_appserver executable and installation of dependencies
COPY requirements.txt ./
RUN pip install -U pip && \
    pip install -r requirements.txt

ADD auth/ /app
RUN ./app/manage.py collectstatic --noinput

WORKDIR /app

