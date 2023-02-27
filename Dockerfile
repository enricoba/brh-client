# get python image
FROM python:3.11-buster

# create directory for src
RUN mkdir -p /var/brh-client
WORKDIR /var/brh-client

# copy data
COPY . /var/brh-client/

# install requirements
RUN addgroup --gid 1000 brhclient \
    && adduser --system --uid 1000 --ingroup brhclient --no-create-home --disabled-login brhclient \
    && chown -R brhclient:brhclient /var/brh-client \
    && wget -qO - https://packages.confluent.io/deb/7.3/archive.key | apt-key add - \
    && apt update \
    && apt install software-properties-common -y \
    && add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/7.3 stable main" \
    && add-apt-repository "deb https://packages.confluent.io/clients/deb buster main" \
    && apt update && apt upgrade -y \
    && apt install librdkafka-dev bash -y \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# activate user
USER brhclient

# entrypoint
ENTRYPOINT ["/var/brh-client/docker-entrypoint.sh"]