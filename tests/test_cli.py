import subprocess
import sys
import json


def test_version_command():
    result = subprocess.run([sys.executable, '-m', 'genloop_cli', 'version'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'GenLoop version' in result.stdout


def test_generate_characters_command():
    result = subprocess.run([sys.executable, '-m', 'genloop_cli', 'generate', 'characters'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Generating characters...' in result.stdout


def test_generate_items_command():
    result = subprocess.run([sys.executable, '-m', 'genloop_cli', 'generate', 'items'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Generating items...' in result.stdout


def test_generate_environments_command():
    result = subprocess.run([sys.executable, '-m', 'genloop_cli', 'generate', 'environments'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Generating environments...' in result.stdout


def _create_workflow(tmp_path, valid=True):
    nodes = [{'type': 'GenLoopInputNode'}]
    if valid:
        nodes.append({'type': 'GenLoopOutputNode'})
    data = {'nodes': nodes if valid else []}
    wf = tmp_path / 'workflow.json'
    wf.write_text(json.dumps(data))
    return wf


def test_generate_characters_with_workflow(tmp_path):
    wf = _create_workflow(tmp_path, valid=True)
    result = subprocess.run([sys.executable, '-m', 'genloop_cli', 'generate', 'characters', '--workflow', str(wf)], capture_output=True, text=True)
    assert result.returncode == 0
    assert f'Loaded workflow from {wf}' in result.stdout


def test_generate_characters_invalid_workflow(tmp_path):
    wf = _create_workflow(tmp_path, valid=False)
    result = subprocess.run([sys.executable, '-m', 'genloop_cli', 'generate', 'characters', '--workflow', str(wf)], capture_output=True, text=True)
    assert result.returncode != 0
    assert 'Invalid workflow' in result.stderr


def test_generate_characters_with_override(tmp_path):
    wf = _create_workflow(tmp_path, valid=True)
    result = subprocess.run([
        sys.executable,
        '-m',
        'genloop_cli',
        'generate',
        'characters',
        '--workflow',
        str(wf),
        '--override',
        'foo=bar',
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Applied overrides: {'foo': 'bar'}" in result.stdout


def test_generate_characters_invalid_override(tmp_path):
    wf = _create_workflow(tmp_path, valid=True)
    result = subprocess.run([
        sys.executable,
        '-m',
        'genloop_cli',
        'generate',
        'characters',
        '--workflow',
        str(wf),
        '--override',
        'bad',
    ], capture_output=True, text=True)
    assert result.returncode != 0
    assert 'Invalid override' in result.stderr
