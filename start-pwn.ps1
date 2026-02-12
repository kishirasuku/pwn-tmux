$CONTAINER = "pwn-debug"
$IMAGE = "pwn-tmux:latest"
$MOUNT = "$PSScriptRoot\scripts"

$exists = docker inspect $CONTAINER 2>$null
if ($LASTEXITCODE -eq 0) {
    docker start $CONTAINER | Out-Null
    Write-Host "[*] Container started."
} else {
    docker run -d --name $CONTAINER --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v "${MOUNT}:/pwn" $IMAGE sleep infinity
    Write-Host "[*] Container created."
}

docker exec -it $CONTAINER bash -c "tmux attach 2>/dev/null || tmux new"
