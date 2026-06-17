# ---- History ----
HISTSIZE=10000
SAVEHIST=10000

# ---- Prompt ----
PROMPT="%F{green}%n%f@%F{cyan}%m%f:%F{yellow}%~%f$ "

# ---- Auto-completion ----
autoload -Uz compinit && compinit

# ---- Alias ----
alias ls='ls -G'
alias ll='ls -alF'

# ---- Add current directory to PATH  ----
export PATH="$PATH:."
export PYTHONPATH="$HOME/projects${PYTHONPATH:+:$PYTHONPATH}"

# ---- History search with arrow keys ----
bindkey "^[[A" history-beginning-search-backward
bindkey "^[[B" history-beginning-search-forward

# ---- Custom ----
gacp() {
  git add -A &&
  git commit -m "${*:-wip}" &&
  git push
}

alias venv='source venv/bin/activate'
