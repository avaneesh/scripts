#!/bin/bash

# $1 is device name
# _TMUX_CURR_WINDOW is set by ptmux
tmux select-window -t $_TMUX_CURR_WINDOW
tmux send-keys 'pltelnet '$1 'C-m'
tmux split-window -p 80
tmux send-keys 'ptelnet '$1 'C-m'

