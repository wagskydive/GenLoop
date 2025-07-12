# Workflow Templates

The `workflows/` directory contains example ComfyUI workflows ready to use with the CLI.

## Character Workflow

`character.json` includes a basic setup with `GenLoopInputNode` and `GenLoopOutputCharacterNode`.

Use it with:

```bash
python -m genloop_cli generate characters --workflow workflows/character.json
```

## Item Workflow

`item.json` is similar but outputs items using `GenLoopOutputItemNode`.

## Environment Workflow

`environment.json` outputs environments using `GenLoopOutputEnvironmentNode`.
