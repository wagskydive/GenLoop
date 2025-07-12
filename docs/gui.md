# GUI Application

The GenLoop GUI provides a visual interface for asset generation. It currently offers a basic window with tabs for different asset types and tools.

Run the GUI using:

```bash
python -m genloop_gui
```

The initial version exposes six tabs:

- **Characters**
- **Items**
- **Environments**
- **Brainstorm**
- **Style Sheet**
- **Results**

The **Results** tab shows a list of generated image files from the
``outputs`` directory. Use the refresh button to reload the list after
running a generation command.

Future versions will connect the GUI to the CLI to launch generation workflows and display progress.
