# GenLoop

GenLoop is a modular asset generation system built to work with ComfyUI. It provides a command line interface and optional GUI for generating game assets such as characters, items, and environments.

This repository is organised as a monorepo containing packages for the CLI, GUI, and custom ComfyUI nodes. Each component is under active development according to the roadmap in `planning.md`.

## Repository Structure

- `genloop_cli/` – command line interface package
- `genloop_gui/` – optional GUI package with tabs for Characters, Items, Environments, Brainstorm, Style Sheet and a Results view listing generated files
- `genloop_nodes/` – custom ComfyUI nodes
- `workflows/` – default workflow templates (see [docs/workflows.md](docs/workflows.md))
- `docs/` – documentation
- `docs/style_sheet.md` – information on managing style tags
- `tests/` – unit tests

See [docs/nodes.md](docs/nodes.md) for details on node utilities such as
`GenLoopInputNode` and the output node classes that save generated assets.
For details on the optional graphical interface see [docs/gui.md](docs/gui.md).

## Installation

See [docs/installation.md](docs/installation.md) for setup instructions.

For details on the command line interface, read [docs/cli.md](docs/cli.md). You can try the placeholder generation commands:

```bash
python -m genloop_cli generate characters [--workflow path/to/workflow.json]
python -m genloop_cli generate items [--workflow path/to/workflow.json]
python -m genloop_cli generate environments [--workflow path/to/workflow.json]
python -m genloop_cli generate characters --workflow wf.json \
    --override prompt="A hero" --override style=anime
python -m genloop_cli generate characters --workflow wf.json --debug
```
Supplying a workflow will run ComfyUI. Set ``GENLOOP_COMFYUI_CMD`` to override
the command if ComfyUI is installed elsewhere or for testing purposes.

To launch the GUI run:

```bash
python -m genloop_gui
```

Within the **Characters** tab you can manage character slots by adding or
removing editable slot names. Styles can be locked to a slot and are persisted
in ``slots.json``. Use the **Generate** button to run the CLI. See
[docs/gui.md](docs/gui.md) for details. The **Style Sheet** tab manages style
tags stored in ``styles.json``. Output nodes also append metadata entries to
``asset_log.json``.

## Packaging

See [docs/packaging.md](docs/packaging.md) for instructions on building standalone executables using PyInstaller. A `package` CLI command is available to build both the CLI and GUI applications.
