import os
import subprocess

STEAMCMD_PATH = "/opt/steamcmd"
STEAMCMD_EXE = f"{STEAMCMD_PATH}/steamcmd.sh"

# Install steamcmd.
if not os.path.exists(STEAMCMD_EXE):
    subprocess.call(f"mkdir -p {STEAMCMD_PATH}", shell=True)
    subprocess.call(
        f"wget -qO- 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar zxf - -C {STEAMCMD_PATH}",
        shell=True,
    )

# Install/update the server.
if os.environ["SKIP_INSTALL"] in ["", "false"]:
    steamcmd = [STEAMCMD_EXE]
    steamcmd.extend(["+force_install_dir", "/opt/ArmaReforgerServer"])
    if os.environ.get("STEAM_USER"):
        steamcmd.extend(
            ["+login", os.environ["STEAM_USER"], os.environ["STEAM_PASSWORD"]]
        )
    else:
        steamcmd.extend(["+login", "anonymous"])
    steamcmd.extend(["+app_update", "1874900"])
    if os.environ.get("STEAM_BRANCH"):
        steamcmd.extend(["-beta", os.environ["STEAM_BRANCH"]])
    if os.environ.get("STEAM_BRANCH_PASSWORD"):
        steamcmd.extend(["-betapassword", os.environ["STEAM_BRANCH_PASSWORD"]])
    steamcmd.extend(["validate", "+quit"])
    subprocess.call(steamcmd)

# Launch server.
launch = " ".join(
    [
        os.environ["ARMA_BINARY"],
        "-backendlog",
        "-nothrow",
        f"-config {os.environ['ARMA_CONFIG']}",
        f"-maxFPS {os.environ['ARMA_MAX_FPS']}",
        f"-profile {os.environ['ARMA_PROFILE']}",
        os.environ["ARMA_PARAMS"],
    ]
)

print(launch, flush=True)
subprocess.call(launch, shell=True)
