ARG IMAGE="python:3.13"
FROM --platform=amd64 mcr.microsoft.com/devcontainers/${IMAGE}
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends build-essential libssl-dev gdb cmake
