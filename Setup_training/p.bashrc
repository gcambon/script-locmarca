# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

color_prompt=yes
if [ "$color_prompt" = yes ]; then
    #PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]|\[\033[01;34m\]$(pwd)\[\033[00m\]\$ '
else
    #PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
    PS1='${debian_chroot:+($debian_chroot)}\u@\h|$(pwd)\$ '
fi

############
# prompt taking into account git
# orig ps1 is <\w>\u<\h> :
if [ -f ~/.bash_git ]; then
  source ~/.bash_git
  #export PS1='<\w>\u<\h>$(__git_ps1 "(%s)") : '
  #export PS1='<\w>\u<\h>$(__git_ps1 "(%s)") : '
  ##export PS1=$PS1'$(__git_ps1 "(%s)") : '
  export PS1=$PS1'$(__git_ps1 "[%s]") '
fi

# User specific aliases and functions
alias vi='vim'
alias fd='find . -name \!*'
alias ping='ping -s \!*'
alias tx='textedit \!* &'
alias h='history'
#alias mv='mv -i'
alias rm='rm -i'
alias lm='ls -rtl'
#alias cp='cp -i'
alias cleandir='rm -f *~* *#* *Thumbs.db*'

alias omp4='export OMP_NUM_THREADS=4'
alias omp2='export OMP_NUM_THREADS=2'
alias omp8='export OMP_NUM_THREADS=8'

#Modules
# module load gcc/7.1.0  
# # for netcdf, netcdf-fortran, mpich compiled with gcc/7.1.0
# module load wrf/4.4.2

module load mamba/psf2026
export COMMONDATA="/data/gcambon/COMMONDATA/"

alias squ='squeue -u $USER --long'
#alias getonei='salloc --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=32G --time=02:00:00 --partition=kura'
alias getonei='salloc --nodes=1 --ntasks=4 --cpus-per-task=1 --mem=32G --time=02:00:00 --partition=kura'
alias mbp='mamba activate psf2026'

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/python/mamba3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/python/mamba3/etc/profile.d/conda.sh" ]; then
        . "/opt/python/mamba3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/python/mamba3/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/opt/python/mamba3/etc/profile.d/mamba.sh" ]; then
    . "/opt/python/mamba3/etc/profile.d/mamba.sh"
fi