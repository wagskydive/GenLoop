# Development Roadmap

GenLoop will be developed in the following milestones derived from the design document. Each milestone contains a checklist of tasks to track progress.

## Milestone 1: Project Initialization
- [ ] Monorepo setup
- [ ] README and folder scaffold
- [ ] Installation docs

## Milestone 2: CLI Core
- [ ] `generate characters` command
- [ ] `generate items` command
- [ ] `generate environments` command
- [ ] Workflow loading from `.json`
- [ ] GenLoop node validation
- [ ] CLI argument overrides
- [ ] Run ComfyUI and watch for output
- [ ] Debug and override flags

## Milestone 3: Custom Nodes
- [ ] `GenLoopInputNode` with prompt and metadata handling
- [ ] Output nodes for characters, items and environments
- [ ] PNG saving and metadata logging
- [ ] Utility functions (slugifier, safe paths)

## Milestone 4: GUI Application
- [ ] Tabs for Characters, Items, Environments, Brainstorm and Style Sheet
- [ ] Results view
- [ ] Character slot management
- [ ] GUI to CLI bridge with progress feedback

## Milestone 5: Workflow Templates
- [ ] Default character workflow
- [ ] Default item workflow
- [ ] Default environment workflow
- [ ] Include GenLoop nodes in templates
- [ ] Publish under `/workflows`

## Milestone 6: Asset Metadata and Style Management
- [ ] Style sheet collection
- [ ] Slot memory for locked styles
- [ ] Asset logs in JSON

## Milestone 7: Packaging
- [ ] PyInstaller build for CLI
- [ ] GUI desktop packaging
- [ ] Bundle default workflows and templates

