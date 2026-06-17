set nocompatible

syntax on
filetype plugin indent on

" Editing
set autoindent
set expandtab
set shiftwidth=4
set tabstop=4
set backspace=indent,eol,start
set autowrite
set textwidth=0
set nowrap

" UI
set number
set relativenumber
set cursorline
set hlsearch
set incsearch
set ignorecase
set smartcase
set belloff=all

" Colors
set termguicolors
hi Search ctermbg=DarkBlue ctermfg=White

" Insert-mode cursor shape
if exists('$TMUX')
    let &t_SI = "\ePtmux;\e\e[5 q\e\\"
    let &t_EI = "\ePtmux;\e\e[2 q\e\\"
else
    let &t_SI = "\e[5 q"
    let &t_EI = "\e[2 q"
endif

" Navigation
inoremap <C-h> <Left>
inoremap <C-j> <Down>
inoremap <C-k> <Up>
inoremap <C-l> <Right>

" Convenience
command! W write
command! Q quit

" Visualize tabs/trailing spaces
set list
set listchars=tab:»·,trail:·

" Performance
set lazyredraw
set ttyfast

" History
set history=1000