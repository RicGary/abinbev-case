FROM debian:11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instala Python, pip e outras dependências
RUN apt update && \
    apt install -y python3 python3-pip procps tini libjemalloc2 openjdk-11-jre-headless && \
    apt clean

WORKDIR /app

COPY dataproc/requirements.txt ./
RUN pip3 install -r requirements.txt

COPY dataproc/* /app
COPY openbrewery.py /app
COPY key.json /app
COPY dataproc/convert_json_delta.py /app/

ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

CMD ["python3", "convert_json_delta.py"]
