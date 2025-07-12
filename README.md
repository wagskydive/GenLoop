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

## Installation

See [docs/installation.md](docs/installation.md) for setup instructions.

For details on the command line interface, read [docs/cli.md](docs/cli.md). You can try the placeholder generation command:

```bash
python -m genloop_cli generate characters
```
