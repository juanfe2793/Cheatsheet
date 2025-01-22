# Carvel Commands

Useful commands for tools associated with carvel, like imgpkg

### imgpkg


```bash
# Local dev
imgpkg push -f bundle -b kind-registry.local:5000/internal/cluster-issuer:0.0.1
curl kind-registry.local:5000/v2/_catalog
curl -s kind-registry.local:5000/v2/internal/cluster-issuer/tags/list | jq .

# Pushing to ECR

export IMGPKG_ENABLE_IAAS_AUTH=false
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 12345678910.dkr.ecr.us-east-1.amazonaws.com
imgpkg push -f bundle -b --registry 433117149852.dkr.ecr.us-east-1.amazonaws.com

# Pulling from ECR

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 12345678910.dkr.ecr.us-east-1.amazonaws.com
imgpkg pull -i 12345678910.dkr.ecr.us-east-1.amazonaws.com/internal/bundle-name:v0.0.1-test -o tmp

```

### kapp

```bash
kctrl app kick -a app-name -n kapp-controller
```
