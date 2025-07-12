# Tickets

## Ticket 1 - Create Development Roadmap
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Read the `design.md` document and create `planning.md` with a development roadmap that contains milestones and a logical order in which the development will take place. It contains checkmarks to keep track of the overall progress. It is a document that goes into full detail about the roadmap.

## Ticket 2 - Project Setup
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Read the design document about the tools that will be used and install the software and dependencies and add them to `requirements.txt`and create a boiler plate project, 


## Ticket 2 - Update Agents Instructions
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Review the design document and expand `AGENTS.md` with detailed project guidelines and iterative workflow instructions.
## Ticket 3 - Generate Characters Command
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement the `generate characters` command in the CLI. For now it should simply output a message indicating that character generation has been triggered.

## Ticket 4 - Generate Items Command
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement the `generate items` command in the CLI. It should output a message indicating that item generation has been triggered.

## Ticket 5 - Generate Environments Command
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement the `generate environments` command in the CLI. It should output a message indicating that environment generation has been triggered.

## Ticket 6 - Workflow Loading
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Add `--workflow` option to generation commands. Load JSON workflow file and validate required nodes (`GenLoopInputNode` and `GenLoopOutput*Node`).

## Ticket 7 - CLI Argument Overrides
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Add `--override key=value` option to generation commands. Parsed overrides should be applied to the loaded workflow data.

## Ticket 8 - CLI Debug Flag
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Add `--debug` option to generation commands to print loaded workflow data and overrides.

## Ticket 9 - ComfyUI Execution Stub
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a placeholder function to invoke ComfyUI using a workflow path. For now it should just print the command that would be run.


## Ticket 10 - Run ComfyUI Execution
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Replace the placeholder ComfyUI function with actual subprocess execution. Stream output and allow overriding the command via the `GENLOOP_COMFYUI_CMD` environment variable.

## Ticket 11 - Slugifier Utility
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Add a `slugify` helper in `genloop_nodes.utils` to create filesystem-safe slugs.

## Ticket 12 - GenLoopInputNode Skeleton
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a minimal `GenLoopInputNode` with prompt formatting and metadata output.

## Ticket 13 - Safe Path Utility
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a `safe_path` helper in `genloop_nodes.utils` to sanitise file paths.

## Ticket 14 - GenLoopOutput Nodes
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Add basic output node classes capable of saving PNG and JSON metadata using `safe_path`.



## Ticket 15 - GUI Skeleton
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a basic PySide6 GUI application with tabs for Characters, Items, Environments, Brainstorm, Style Sheet and Results. Provide a module entry point to launch the GUI.
## Ticket 16 - GUI Results View
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a results view in the GUI that lists generated files from the output directory.

## Ticket 17 - Default Character Workflow
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Provide a default character workflow JSON under `workflows/` containing GenLoopInputNode and GenLoopOutputCharacterNode.

## Ticket 18 - Default Item Workflow
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Provide a default item workflow JSON under `workflows/` containing GenLoopInputNode and GenLoopOutputItemNode.

## Ticket 19 - Default Environment Workflow
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Provide a default environment workflow JSON under `workflows/` containing GenLoopInputNode and GenLoopOutputEnvironmentNode.


## Ticket 20 - Character Slot Management
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement character slot management UI in the GUI character tab. Users should be able to add and remove slots which are displayed as editable fields.

## Ticket 21 - GUI to CLI Bridge
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Connect the GUI with the CLI to trigger character generation from the Characters tab. Show command output in a text area for progress feedback.

## Ticket 22 - Style Sheet Collection
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a `StyleSheet` manager to load and save style tags in a JSON file. Provide GUI integration to display and edit the list.

## Ticket 23 - Slot Memory for Locked Styles
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
## Ticket 24 - Asset Logger
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Create an `AssetLogger` to append metadata to `asset_log.json` whenever an output node saves an asset.

## Ticket 25 - CLI Packaging
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a `package` command in the CLI that uses PyInstaller to build a standalone executable. The command should allow overriding the PyInstaller command via the `GENLOOP_PYINSTALLER_CMD` environment variable and bundle the default workflows into the output directory.

## Ticket 26 - GUI Packaging
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Extend the `package` command to support packaging the GUI application using PyInstaller with the same environment variable override.

## Ticket 27 - Bundle Workflows
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement a helper that copies the contents of the `workflows` directory into a specified destination so packaged applications include the templates.

## Ticket 28 - Code Cleanup
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Address flake8 warnings, remove unused imports, and tidy files.
