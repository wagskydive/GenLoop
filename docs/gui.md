# GUI Application

The GenLoop GUI provides a visual interface for asset generation. It includes tabs for different asset types and tools.

Run the GUI using:

```bash
python -m genloop_gui
```

The window exposes six tabs:

- **Characters**
- **Items**
- **Environments**
- **Brainstorm**
- **Style Sheet**
- **Results**

The **Characters** tab supports character slot management with optional style
locking. Use **Add Slot** to create editable slot names and **Remove Slot** to
delete them. **Lock Style** assigns a style tag to the selected slot and the
mapping is saved in ``slots.json``. **Unlock Style** removes the association.
The **Generate** button runs the CLI character generation command and shows the
output in a text box for progress feedback.

The **Style Sheet** tab lets you manage a list of style tags stored in
``styles.json``. Add or remove styles and they will be saved automatically when
closing the GUI.

The **Results** tab shows a list of generated image files from the ``outputs``
directory. Use the refresh button to reload the list after running a generation
command.
