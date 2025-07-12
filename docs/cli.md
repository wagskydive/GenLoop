# CLI Usage

GenLoop ships with a simple command line interface. It currently supports a `version` command and placeholder commands for generating character, item and environment assets.

```bash
python -m genloop_cli version
```

To trigger character generation:

```bash
python -m genloop_cli generate characters [--workflow path/to/workflow.json]
```

To trigger item generation:

```bash
python -m genloop_cli generate items [--workflow path/to/workflow.json]
```

To trigger environment generation:

```bash
python -m genloop_cli generate environments [--workflow path/to/workflow.json]
```

Overrides can be supplied with `--override key=value`. Multiple overrides are
allowed and will update the loaded workflow data:

```bash
python -m genloop_cli generate characters --workflow wf.json \
    --override prompt="A hero" --override style=anime
```

Future commands will include full asset generation functionality as described in `design.md`.
The `--workflow` option allows you to load a ComfyUI workflow JSON file.
When a workflow is provided, GenLoop will launch ComfyUI to execute it. The
``GENLOOP_COMFYUI_CMD`` environment variable can be used to override the command
that is run. This is useful for testing or if ComfyUI is installed in a custom
location.

For troubleshooting you can pass `--debug` to print the loaded workflow and any applied overrides:

```bash
python -m genloop_cli generate characters --workflow wf.json --debug
```
