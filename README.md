# GenLoop

GenLoop is a modular asset generation system built to work with ComfyUI. It provides a command line interface and optional GUI for generating game assets such as characters, items, and environments.

This repository is organised as a monorepo containing packages for the CLI, GUI, and custom ComfyUI nodes. Each component is under active development according to the roadmap in `planning.md`.

## Repository Structure

- `genloop_cli/` – command line interface package
- `genloop_gui/` – optional GUI package
- `genloop_nodes/` – custom ComfyUI nodes
- `workflows/` – default workflow templates
- `docs/` – documentation
- `tests/` – unit tests

See [docs/nodes.md](docs/nodes.md) for details on node utilities such as
`GenLoopInputNode` and the output node classes that save generated assets.

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
