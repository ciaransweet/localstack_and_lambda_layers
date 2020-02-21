#!/bin/bash

echo "Build Layer and extract zip of dependencies"
docker run --name cogeo -w /var/task --volume $PWD/:/local -itd remotepixel/amazonlinux:gdal3.0-py3.7-cogeo bash
docker exec -it cogeo bash '/local/create-layer.sh'
docker cp cogeo:/tmp/package.zip package.zip
docker stop cogeo
docker rm cogeo

echo "Unzip Layer and move all items up one directory"
mkdir deps \
&& cd deps \
&& unzip -qq ../package.zip \
&& mv bin/* . && rm -rf bin \
&& mv lib/* . && rm -rf lib \
&& mv python/* . && rm -rf python \
&& mv share/* . && rm -rf share \
&& rm ../package.zip

echo "Copy in Lambda code and zip up new 'uber' Lambda"
cp ../lambda.py . \
&& zip -r9q lambda.zip . \
&& mv lambda.zip ../lambda.zip \
&& cd .. \
&& rm -rf deps
