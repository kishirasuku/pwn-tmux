# pwn-tmux

Docker-based CTF/PWN development environment with pwntools + pwndbg + tmux integration.

## Features

- **pwntools** with `gdb.debug()` + tmux split-pane debugging
- **pwndbg** for rich GDB visualization (heap, stack, registers)
- **one_gadget** / **ROPgadget** / **ropper** for ROP chain building
- **seccomp-tools** for sandbox analysis
- **Ghidra** (headless) for automated decompilation
- **libc-database** for libc identification from leaked addresses
- **keystone-engine** for in-script assembly
- 32-bit binary support (libc6-i386, gcc-multilib)

## Quick Start

### 1. Build

```bash
docker build -t pwn-tmux docker/
```

### 2. Launch

**Windows:**
Double-click `start-pwn.cmd`, or run:

```powershell
.\start-pwn.ps1
```

**Manual:**

```bash
docker run -d --name pwn-debug \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    -v ./scripts:/pwn \
    pwn-tmux sleep infinity

docker exec -it pwn-debug bash -c "tmux attach 2>/dev/null || tmux new"
```

### 3. Start hacking

```bash
cp /pwn/template.py /pwn/solve.py
# Edit solve.py with your exploit
python3 solve.py GDB    # launches gdb+pwndbg in a tmux split
```

## Usage

```bash
python3 solve.py          # local execution
python3 solve.py GDB      # gdb.debug() + tmux split-pane
python3 solve.py REMOTE   # connect to remote target
```

## Installed Tools

| Tool | Usage |
|------|-------|
| `checksec ./chall` | Check binary protections |
| `one_gadget ./libc.so.6` | Find one-shot RCE gadgets |
| `ROPgadget --binary ./chall` | Search ROP gadgets |
| `ropper -f ./chall` | Auto-generate ROP chains |
| `seccomp-tools dump ./chall` | Analyze seccomp filters |
| `patchelf --set-interpreter ./ld.so ./chall` | Swap ld/libc for local testing |

See [CHEATSHEET.md](CHEATSHEET.md) for the full reference.

## Directory Structure

```
pwn-tmux/
├── README.md
├── CHEATSHEET.md           # quick reference
├── start-pwn.cmd           # Windows launcher
├── start-pwn.ps1           # PowerShell launcher script
├── docker/
│   └── Dockerfile          # image definition
└── scripts/
    ├── template.py         # exploit template
    └── test_exploit.py     # smoke test
```

## Container Lifecycle

```bash
docker stop pwn-debug      # stop (preserves state)
docker start pwn-debug      # resume
docker rm -f pwn-debug      # destroy
```
