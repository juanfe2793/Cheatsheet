# Docker commands

some useful docker commands

```bash

# Run a container from ECR
docker container run -it 123456789.dkr.ecr.us-east-1.amazonaws.com/my/container:latest /bin/sh (or /bin/bash)

#Check dependencies

docker run --rm -v "$(pwd)":/opt/maven -w /opt/maven maven:3.8.4-jdk-8 mvn dependency:tree | grep log4

```