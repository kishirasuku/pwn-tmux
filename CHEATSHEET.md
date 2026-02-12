# pwn-tmux チートシート

## コンテナ起動

`start-pwn.bat` をダブルクリック、またはターミナルで:

```
.\start-pwn.bat
```

## template.py の使い方

```bash
# 1. テンプレートをコピー
cp /pwn/template.py /pwn/solve.py

# 2. solve.py の設定セクションを編集
#    BINARY, LIBC, HOST, PORT, context.arch を書き換える

# 3. 実行
python3 solve.py          # ローカル実行
python3 solve.py GDB      # gdb + tmux分割 (pwndbg表示)
python3 solve.py REMOTE    # リモート接続
```

## コンテナ内ツール一覧

| コマンド | 用途 |
|---|---|
| `checksec ./chall` | セキュリティ機構の確認 |
| `one_gadget ./libc.so.6` | ワンショットRCEガジェット検索 |
| `ROPgadget --binary ./chall` | ROPガジェット検索 |
| `ropper -f ./chall` | ROPチェイン自動生成 |
| `seccomp-tools dump ./chall` | seccompフィルタ解析 |
| `patchelf --set-interpreter ./ld.so ./chall` | ld差し替え |
| `patchelf --replace-needed libc.so.6 ./libc.so.6 ./chall` | libc差し替え |

## Ghidra (ヘッドレスデコンパイル)

```bash
analyzeHeadless /tmp/proj proj -import ./chall -postScript /opt/ghidra/Ghidra/Features/Decompiler/ghidra_scripts/ExportCFileScript.java
```

## libc-database

```bash
cd /opt/libc-database
./get ubuntu      # Ubuntu系libcをDL (初回のみ)
./find printf 0x??? read 0x???   # リークからlibc特定
./dump id         # オフセット取得
```

## gdb (pwndbg) よく使うコマンド

| コマンド | 用途 |
|---|---|
| `telescope $rsp 20` / `tb $rsp 20` | スタック表示 |
| `vis_heap_chunks` / `hc` | ヒープ可視化 |
| `heap` / `hp` | ヒープ情報 |
| `vmmap` | メモリマッピング |
| `search -s "flag"` | メモリ内文字列検索 |
| `cyclic 100` / `cyclic -l 0x6161616a` | オフセット特定 |

## tmux 操作

| キー | 操作 |
|---|---|
| `Ctrl+b |` | 縦分割 |
| `Ctrl+b -` | 横分割 |
| `Ctrl+b 矢印` | ペイン移動 |
| `Ctrl+b d` | デタッチ (コンテナは動き続ける) |
