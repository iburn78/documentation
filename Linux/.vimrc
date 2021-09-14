set nocompatible              " be iMproved, required
filetype off                  " required
syntax on
set autoindent
set autowrite
set shiftwidth=4
set hlsearch
set incsearch
set textwidth=70
set cursorline
"set number
set tabstop=4
set expandtab
"set ignorecase
set backup
set backupdir=~/.vimbackup
set directory=~/.vimbackup
set writebackup
"insert mode mapping - it may not work well though, especially left mapping
inoremap <C-h> <left>        
inoremap <C-j> <down>
inoremap <C-k> <up>
inoremap <C-l> <right>
inoremap <C-v> <BS>
inoremap <C-b> <Del>

autocmd InsertEnter * highlight CursorLine guifg=white guibg=darkblue ctermfg=white ctermbg=darkblue
autocmd InsertLeave * highlight CursorLine guifg=white guibg=black ctermfg=white ctermbg=black
set textwidth=300
set backspace=indent,eol,start
set belloff=all

hi Search ctermbg=DarkBlue
hi Search ctermfg=White
