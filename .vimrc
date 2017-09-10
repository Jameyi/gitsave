set nu
set tabstop=4
set shiftwidth=4
set autoindent
set softtabstop=4
set encoding=utf-8
set termencoding=utf-8
set formatoptions+=mM
set fencs=utf-8.gbk
let python_highlight_all=1
"Plugin 'scrooloose/syntastic'"
:inoremap ( ()<ESC>i
:inoremap ) <c-r>=ClosePair(')')<CR>
:inoremap { {<CR>}<ESC>o
:inoremap } <c-r>=ClosePair('}')<CR>
:inoremap [ []<ESC>i
:inoremap ] <c-r>=ClosePair(']')<CR>
:inoremap " ""<ESC>i
:inoremap ' ''<ESC>i
function! ClosePair(char)
	if getline('.')[col('.') - 1] == a:char
		return "\<Right>"
	else
		return a:char
	endif
endfunction
filetype plugin indent on
set completeopt=longest,menu
syntax on
autocmd BufNewFile *.py,*.cc,*.sh,*.java exec ":call SetTitle()"
func SetTitle()
	if &filetype == 'python'
		call setline(1,"\#! usr\/bin\/env python")
		call setline(2,"\#! coding:utf-8")
	endif
endfunction
