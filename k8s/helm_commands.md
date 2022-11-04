# Helm commands

some useful helm commands

```bash

# Show the status of a helm release
helm status 

# List all the Helm releases
helm list --all

# Fast rollback one release (like HEAD~1)

helm rollback <release-name> 0

# Push chart to S3 bucket

HELM_S3_MODE=3 helm s3 push $chart $repo 
HELM_S3_MODE=3 helm s3 push grafana adyton

# Pull chart

helm pull <repo>/<chart> Example: (helm pull grafana/grafana)

# Watch the manifest will be deployed to cluster.

helm template <name> <chart>

```