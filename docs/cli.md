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

Future commands will include full asset generation functionality as described in `design.md`.
The `--workflow` option allows you to load a ComfyUI workflow JSON file.
