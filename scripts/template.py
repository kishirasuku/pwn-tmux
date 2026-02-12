#!/usr/bin/env python3
from pwn import *
import sys

# ============================================================
# 設定
# ============================================================
BINARY = './chall'
LIBC   = ''  # e.g. './libc.so.6'
HOST   = ''
PORT   = 0

context.arch    = 'amd64'
context.os      = 'linux'
context.log_level = 'debug'
context.terminal  = ['tmux', 'splitw', '-h']

elf  = ELF(BINARY)
libc = ELF(LIBC) if LIBC else None

# ============================================================
# 接続
# ============================================================
def conn():
    if args.REMOTE:
        return remote(HOST, PORT)
    elif args.GDB:
        return gdb.debug(['stdbuf', '-o0', BINARY], gdbscript=GDB_SCRIPT)
    else:
        return process(['stdbuf', '-o0', BINARY])

GDB_SCRIPT = '''
# ブレークポイントをここに追加
# b *main
# b *0x401234
c
'''

# ============================================================
# exploit
# ============================================================
def exploit():
    p = conn()

    # --- ここにexploitを書く ---

    p.interactive()

if __name__ == '__main__':
    exploit()
