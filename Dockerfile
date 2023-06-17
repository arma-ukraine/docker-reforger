FROM debian:bullseye-slim

LABEL maintainer="ACE Team - https://github.com/acemod"
LABEL org.opencontainers.image.source=https://github.com/acemod/docker-reforger

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
    && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    python3 \
    lib32stdc++6 \
    lib32gcc-s1 \
    wget \
    ca-certificates \
    libcurl4 \
    net-tools \
    libssl1.1 \
    wamerican \
    && \
    apt-get remove --purge -y \
    && \
    apt-get clean autoclean \
    && \
    apt-get autoremove -y \
    && \
    rm -rf /var/lib/apt/lists/* 

ENV STEAM_USER=""
ENV STEAM_PASSWORD=""
ENV STEAM_BRANCH="public"
ENV STEAM_BRANCH_PASSWORD=""

ENV ARMA_CONFIG=""
ENV ARMA_PROFILE=/opt/ArmaReforgerServer/profile
ENV ARMA_BINARY="./ArmaReforgerServer"
ENV ARMA_PARAMS=""
ENV ARMA_MAX_FPS=120

ENV SKIP_INSTALL=false

WORKDIR /opt/ArmaReforgerServer
VOLUME /opt/ArmaReforgerServer

EXPOSE 2001/udp
EXPOSE 17777/udp

STOPSIGNAL SIGINT

COPY *.py /

CMD ["python3","/launch.py"]
