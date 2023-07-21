#!/bin/bash

docker build --build-arg FILENAME=foo --build-arg PORT=8080 -t foo -f Dockerfile .
docker build --build-arg FILENAME=sidecar --build-arg PORT=5000 -t sidecar -f Dockerfile .
