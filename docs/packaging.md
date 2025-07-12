# Packaging

GenLoop can be bundled as a standalone executable using PyInstaller. A new CLI command is provided:

```bash
python -m genloop_cli package --target cli
```

This generates a binary under the ``dist/`` directory. The `GENLOOP_PYINSTALLER_CMD` environment variable can be used to override the PyInstaller command, which is useful during testing.

The packaging process also copies the contents of the ``workflows`` folder into the output directory so packaged applications include the example templates.

To package the GUI application run:

```bash
python -m genloop_cli package --target gui
```

PyInstaller must be installed. See ``requirements.txt``.
