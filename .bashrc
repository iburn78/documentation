# ---- Interactive shells only ----
case $- in
    *i*) ;;
      *) return ;;
esac

# ---- History ----
HISTSIZE=10000
HISTFILESIZE=10000
shopt -s histappend

# ---- Prompt ----
PS1='\[\e[32m\]\u\[\e[0m\]@\[\e[36m\]\h\[\e[0m\]:\[\e[33m\]\w\[\e[0m\]\$ '

# ---- Auto-completion ----
if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
fi

# ---- Alias ----
alias ls='ls --color=auto'
alias ll='ls -alF'

# ---- Add current directory to PATH ----
export PATH="$PATH:."
export PYTHONPATH="$HOME/projects${PYTHONPATH:+:$PYTHONPATH}"

# ---- History search with arrow keys ----
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

# ---- Custom ----
gacp() {
    git add -A &&
    git commit -m "${*:-wip}" &&
    git push
}

alias venv='source venv/bin/activate'