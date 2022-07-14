FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /usr/src/code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# poetry export --no-interaction --no-ansi --without-hashes --format requirements.txt --dev --output ./fast_api/requirements.dev.txt
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.dev.txt .
RUN pip install -r requirements.dev.txt
# add app
COPY . .

# add entrypoint
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/code/entrypoint.sh

# run entrypoint
ENTRYPOINT ["/usr/src/code/entrypoint.sh"]

