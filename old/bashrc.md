
```bash
HISTCONTROL=ignoreboth:erasedups

alias ll='ls -l'
alias ltr='ls -ltr'

alias p='python3'
alias e='einstein'
alias n='nano'
alias h='history'
alias pl='prolog'
alias cdo='cd "/mnt/c/Users/Jake/OneDrive - Dublin City University"'
alias cdg='cd "/mnt/i/My Drive"'
alias cdu='cd "/mnt/c/Users/Jake"'
alias dcu='docker compose up -d'
alias dcd='docker compose down'
alias dcp='docker compose pull'
alias dps='docker ps'
alias dl='docker logs'
alias dprune='docker system prune -a'
alias dus='du | sort -n'
alias docker-compose='docker compose'
alias ducks='du -cks * | sort -rn | head'
alias serv='cd ~/services'
alias cupdate='sudo apt update && sudo apt full-upgrade -y'

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```