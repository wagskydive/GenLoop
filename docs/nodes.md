# GenLoop Nodes Utilities

GenLoop provides helper functions for building custom ComfyUI nodes.

## `slugify`

```
from genloop_nodes import slugify
```

Returns a filesystem-safe slug by lowering the text and replacing any
non-alphanumeric characters with underscores.

## `GenLoopInputNode`

A minimal implementation returning a formatted prompt and metadata:

```python
from genloop_nodes import GenLoopInputNode
node = GenLoopInputNode(prompt="hello", style_tag="cute")
info = node.prepare()
```
