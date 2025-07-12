from __future__ import annotations

import os
import subprocess
from pathlib import Path
import shutil
import click
from typing import Sequence

__all__ = ["run_pyinstaller", "bundle_workflows"]


def run_pyinstaller(entry: str, name: str, dist: str = "dist") -> None:
    """Run PyInstaller to build ``entry`` as ``name`` into ``dist``.

    The ``GENLOOP_PYINSTALLER_CMD`` environment variable can override the
    command executed. Output is streamed through Click.
    """
    cmd = [
        "pyinstaller",
        "--onefile",
        "--distpath",
        dist,
        "--name",
        name,
        entry,
    ]
    env_cmd = os.environ.get("GENLOOP_PYINSTALLER_CMD")
    if env_cmd:
        click.echo(f"Running: {env_cmd}")
        process = subprocess.Popen(
            env_cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    else:
        click.echo(f"Running: {' '.join(cmd)}")
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
        except FileNotFoundError as e:
            raise click.ClickException("PyInstaller not found") from e
    assert process.stdout is not None
    for line in process.stdout:
        click.echo(line.rstrip())
    process.wait()
    if process.returncode != 0:
        raise click.ClickException(
            f"PyInstaller failed with code {process.returncode}"
        )


def bundle_workflows(dest: str) -> None:
    """Copy the ``workflows`` directory into ``dest``."""
    src = Path(__file__).resolve().parent.parent / "workflows"
    dest_path = Path(dest) / "workflows"
    dest_path.mkdir(parents=True, exist_ok=True)
    for wf in src.glob("*.json"):
        shutil.copy(wf, dest_path / wf.name)
    click.echo(f"Bundled workflows to {dest_path}")
