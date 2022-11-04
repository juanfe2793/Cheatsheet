# Bash_profile

this is useful .bash_profile or .zshrc

```bash
# interactive shell commands

# pyenv
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"# interactive shell commands

# Kubeconfig
#export KUBECONFIG="${HOME}/.kube/config"
export KUBECONFIG="${KUBECONFIG}:${HOME}/.kube/config"
for f in $(ls $HOME/.kube/myconfigs); do export KUBECONFIG="${KUBECONFIG}:$HOME/.kube/myconfigs/$f" ; done

#Aliases
alias la='ls -lah'
alias gadd='git add .'
alias gmain='git checkout main'
alias gscmm='git commit -S -m '
alias grbs2='git rebase --interactive HEAD~2'
alias grbs3='git rebase --interactive HEAD~3'
alias ghard='git reset --hard HEAD'
alias gpull='git pull origin main'
alias kube-nodes='kube get nodes'
alias kube-pods='kube get pods -o wide'
alias kube='kubecolor'
alias kubectl='kubecolor'
alias eshell='exec $SHELL'
alias kube-ctx='kube config current-context'
autoload -U +X bashcompinit && bashcompinit
complete -o nospace -C /usr/local/bin/terraform terraform

```