FROM pwn-env:latest

# ============================================================
# パッケージ & 基本ツール
# ============================================================
RUN apt-get update && apt-get install -y \
    tmux \
    ruby ruby-dev \
    lib32z1 libc6-i386 libc6-dev-i386 \
    openjdk-21-jdk-headless \
    && rm -rf /var/lib/apt/lists/*

# ============================================================
# Ruby gems: one_gadget, seccomp-tools
# ============================================================
RUN gem install one_gadget seccomp-tools

# ============================================================
# Python tools: ROPgadget, ropper, keystone-engine
# ============================================================
RUN pip3 install --no-cache-dir --break-system-packages \
    ROPgadget \
    ropper \
    keystone-engine

# ============================================================
# libc-database
# ============================================================
RUN git clone https://github.com/niklasb/libc-database /opt/libc-database

# ============================================================
# Ghidra (headless)
# ============================================================
RUN wget -q -O /tmp/ghidra.zip https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.3.1_build/ghidra_11.3.1_PUBLIC_20250219.zip \
    && unzip -q /tmp/ghidra.zip -d /opt \
    && ln -s /opt/ghidra_* /opt/ghidra \
    && rm /tmp/ghidra.zip

ENV PATH="/opt/ghidra/support:${PATH}"

# ============================================================
# 設定ファイル
# ============================================================
# pwntools が tmux を使うように
RUN echo "import os\nos.environ['TERM'] = 'xterm-256color'" >> /etc/python3/sitecustomize.py

# gdbinit: pwndbg + エイリアス
RUN cat <<'EOF' > /root/.gdbinit
source /opt/pwndbg/gdbinit.py

# エイリアス
alias hp = heap
alias hc = vis_heap_chunks
alias tb = telescope
alias bs = backtrace
EOF

# tmux設定
RUN cat <<'EOF' > /root/.tmux.conf
set -g mouse on
set -g default-terminal "xterm-256color"
set -g history-limit 10000
bind | split-window -h
bind - split-window -v
EOF

WORKDIR /pwn
CMD ["bash"]
