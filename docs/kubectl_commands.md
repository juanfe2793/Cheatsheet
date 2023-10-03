# Kubectl Commands

useful kubectl commands

## Verbose

Add --v=4 to verbose a Kubectl command

## Config Context

```bash
# Detailed current context
kubectl config view --minify

# Name of current context
kubectl config current-context

# List available context
kubectl config get-contexts

# Which context to use
kubectl config use-context cluster

# Obtain config from eks cluster
aws eks --region us-east-1 update-kubeconfig --name cluster --alias cluster

```

## Pods

```bash

# describe where the pods are running
kubectl get pods -o wide -n kube-system 

#Get pods running in a specific node
kubectl get pods -n kube-system -o wide --field-selector spec.nodeName=<nodeid> 

# Interactive shell
kubectl exec --stdin --tty <pod-name> -n kube-system -- /bin/sh 
kubectl exec --stdin --tty <pod-name> -n kube-system -- /bin/bash 

# Copy files from a pod
kubectl cp <some-namespace>/<some-pod>:/tmp/foo /tmp/bar
```

## Nodes

```bash
# Get tainted nodes.
kubectl get nodes -o jsonpath="{range .items[*]}{.metadata.name} {.spec.taints[?(@.effect=='NoSchedule')].effect}{\"\n\"}{end}"

#Filter by Label. The -L filters by label key and displays the label values at each node.
kubectl get nodes -L eks.amazonaws.com/capacityType 

```

## Secrets

```bash
#Decode a secret
kubectl get secret my-secret-key -n my-namespace -o jsonpath='{.data.secret-username}' | base64 --decode

# List all Secrets currently in use by a pod
kubectl get pods -o json | jq '.items[].spec.containers[].env[]?.valueFrom.secretKeyRef.name' | grep -v null | sort | uniq


```

## Events

```bash

# List Events sorted by timestamp
kubectl get events --sort-by=.metadata.creationTimestamp 
kubectl get events --sort-by=".lastTimestamp"

```

## Service Accounts

```shell

# Enumerate permissions for a given service account
kubectl -n my-namespace auth can-i --list --as system:serviceaccount:my-namespace:my-service-account

```
