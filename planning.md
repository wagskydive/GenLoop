# Development Roadmap

GenLoop will be developed in the following milestones derived from the design document. Each milestone contains a checklist of tasks to track progress.

## Milestone 1: Project Initialization
- [x] Monorepo setup
- [x] README and folder scaffold
- [x] Installation docs

## Milestone 2: CLI Core
- [x] `generate characters` command
- [x] `generate items` command
- [x] `generate environments` command
 - [x] Workflow loading from `.json`
 - [x] GenLoop node validation
 - [x] CLI argument overrides
- [x] Run ComfyUI and watch for output
 - [x] Debug and override flags

## Milestone 3: Custom Nodes
- [x] `GenLoopInputNode` with prompt and metadata handling
- [x] Output nodes for characters, items and environments
- [x] PNG saving and metadata logging
- [x] Utility functions (slugifier, safe paths)

## Milestone 4: GUI Application
- [x] Tabs for Characters, Items, Environments, Brainstorm and Style Sheet
- [x] Results view
- [x] Character slot management
- [x] GUI to CLI bridge with progress feedback

## Milestone 5: Workflow Templates
- [x] Default character workflow
- [x] Default item workflow
- [x] Default environment workflow
- [x] Include GenLoop nodes in templates
- [x] Publish under `/workflows`

## Milestone 6: Asset Metadata and Style Management
- [x] Style sheet collection
- [ ] Slot memory for locked styles
- [ ] Asset logs in JSON

## Milestone 7: Packaging
- [ ] PyInstaller build for CLI
- [ ] GUI desktop packaging
- [ ] Bundle default workflows and templates

