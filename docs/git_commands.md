# Git commands

Useful git commands

```bash

# Add things to Git ignore
git rm -rf --cached .
git add .

# Clean all local branches except main

git branch | grep -v "main" | xargs git branch -D
```
