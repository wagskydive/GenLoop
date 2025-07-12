# GenLoop Nodes Utilities

GenLoop provides helper functions for building custom ComfyUI nodes.

## `slugify`

```
from genloop_nodes import slugify
```

Returns a filesystem-safe slug by lowering the text and replacing any
non-alphanumeric characters with underscores.

## `safe_path`

```
from genloop_nodes import safe_path
```

Sanitises a path by replacing problematic characters. Useful when building
file paths for generated assets.

## `GenLoopInputNode`

A minimal implementation returning a formatted prompt and metadata:

```python
from genloop_nodes import GenLoopInputNode
node = GenLoopInputNode(prompt="hello", style_tag="cute")
info = node.prepare()
```

## `GenLoopOutput*Node`

Output nodes save images and metadata to disk. Example usage:

```python
from genloop_nodes import GenLoopOutputCharacterNode
node = GenLoopOutputCharacterNode(output_dir="out")
node.save(b"img", {"prompt": "hi"}, name="hero")
```
