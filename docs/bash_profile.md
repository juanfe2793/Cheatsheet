# Bash_profile

this is useful .bash_profile or .zshrc

```bash
# interactive shell commands 

# pyenv 
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"# interactive shell commands 

# Kubeconfig
export KUBECONFIG="${KUBECONFIG}:${HOME}/.kube/config"
for f in $(ls $HOME/.kube/clusters); do export KUBECONFIG="${KUBECONFIG}:$HOME/.kube/clusters/$f" ; done

# Krew 
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"

# pyenv 
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

#owl

#alias python=/usr/local/opt/python@3.9
export PATH="/usr/local/opt/python@3.9/bin:$PATH"
export PATH="$(brew --prefix python@3)/bin:$PATH"
export OWL="/Users/jgomezmanzanares/code/owl"
eval "$("$OWL/bin/owl" init -)"
function aws-login() {  eval $( $OWL/bin/owl aws-login $@ ) ; };

# Go env PATH

export PATH="/Users/${USER}/go/bin:$PATH"


#Aliases
alias la='ls -lah'

# Git aliases
alias gadd='git add .'
alias gmain='git checkout main'
alias gscmm='git commit -S -m '
alias grbs2='git rebase --interactive HEAD~2'
alias grbs3='git rebase --interactive HEAD~3'
alias ghard='git reset --hard HEAD'
alias gpull='git pull origin main'
alias gclean='git branch | grep -v "main" | xargs git branch -D'

# Kubectl aliases
alias kube-nodes='k get nodes'
alias kube-pods='k get pods -o wide'
alias k='kubecolor'
alias kubectl='kubecolor'
alias eshell='exec $SHELL'
alias kctx='kubectx'

autoload -U +X bashcompinit && bashcompinit
complete -o nospace -C /usr/local/bin/terraform terraform

```
