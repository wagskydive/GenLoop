import subprocess
import sys


def test_version_command():
    result = subprocess.run([sys.executable, '-m', 'genloop_cli', 'version'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'GenLoop version' in result.stdout
