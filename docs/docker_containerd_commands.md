# Docker commands

some useful docker commands

```bash

# Run a container from ECR
docker container run -it 123456789.dkr.ecr.us-east-1.amazonaws.com/my/container:latest /bin/sh (or /bin/bash)

#Check dependencies

docker run --rm -v "$(pwd)":/opt/maven -w /opt/maven maven:3.8.4-jdk-8 mvn dependency:tree | grep log4

```

# Containerd Commands

```shell

# Get the container id of the pod. Example:
kubectl get pod my-pod-0 -n my-namespace -o jsonpath="{.status.containerStatuses[].containerID}" | sed 's/.*\/\///'
8e1f2e5907087b5fd55d98849fef640ca73a5ca04db2e9fc0b7d1497ff87aed9

# SSH as root in a containerd pod
sudo runc --root /run/containerd/runc/k8s.io/ exec -t -u 0 8e1f2e5907087b5fd55d98849fef640ca73a5ca04db2e9fc0b7d1497ff87aed9 sh
```
