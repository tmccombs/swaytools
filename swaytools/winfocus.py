import os
import subprocess
import shutil

from .ipc import I3Ipc


def get_command():
    "Try to get a dmenu command to run"
    return (
        os.environ.get("DMENU_CMD") or shutil.which("bemenu") or shutil.which("dmenu")
    )


def main():
    cmd = get_command()
    with I3Ipc() as i3:
        tree = i3.get_tree()
        options = "\n".join(f'{c["id"]}: {c["name"]}' for c in tree.views())
        res = subprocess.run(
            cmd, shell=True, check=True, text=True, capture_output=True, input=options
        )
        cid = res.stdout.split(":", 2)[0]
        i3.command(f'[con_id="{cid}"] focus')
