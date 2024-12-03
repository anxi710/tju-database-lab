#!/bin/bash

# 创建一个新的 tmux 会话，命名为 'dev-session'
tmux new-session -d -s dev-session

# 在第一个窗口中运行前端代码
tmux send-keys -t dev-session 'cd ./takeout/front_end ; npm run serve' C-m

# 分割窗口，创建第二个窗口
tmux split-window -v
tmux send-keys 'mysql -u root -p' C-m

tmux select-pane -U

# 再次分割窗口，创建第三个窗口
tmux split-window -h
tmux send-keys 'cd ./takeout/back_end ; conda activate takeout' C-m
tmux send-keys 'python run.py' C-m

# 选择第二个窗口
tmux select-pane -t 2

# 附加到会话
tmux attach-session -t dev-session
