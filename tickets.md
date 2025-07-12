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

