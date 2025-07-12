# 🧠 GenLoop: Design & Development Roadmap

A modular asset-generation system powered by ComfyUI and LLM prompt integration. Part of the **CodeLoop Suite**, GenLoop acts as the asset creation layer alongside DevLoop (code) and QA Loop (testing).

---

## 📘 System Overview

**GenLoop** is a developer-focused asset generator that interfaces with ComfyUI to produce 2D game-ready content through:

- Smart prompt input
- Workflow validation
- Custom ComfyUI nodes
- Batch generation
- File output management

---

## 🔧 Architecture Summary

### Core Components:
- `genloop-cli`: Headless tool to trigger ComfyUI workflows via prompt + config
- `genloop-gui`: Optional PySide6/Electron interface to visually manage assets
- `genloop-nodes`: Custom ComfyUI input/output nodes with batch logic
- `workflows/`: Plug-and-play generation graphs with node compatibility

---

## 🧩 Custom Node System

### 1. `GenLoopInputNode`

**Inputs:**
- prompt (STRING)
- style_tag (STRING)
- asset_type (STRING)
- variant_count (INT)
- output_path (STRING)
- check_existing (BOOL)

**Outputs:**
- formatted_prompt (STRING)
- metadata (JSON)
- current_prompt (STRING)

**Behavior:**
- Generates variant list if needed
- Checks for existing output before triggering
- Handles slot-based metadata
- Prepares prompt + metadata for output node

---

### 2. `GenLoopOutputNode` Variants

- `GenLoopOutputCharacterNode`
- `GenLoopOutputItemNode`
- `GenLoopOutputEnvironmentNode`

**Inputs:**
- image (IMAGE)
- prompt_metadata (JSON)
- resolution (INT, INT)
- slot_reference (STRING)
- file_prefix (STRING)

**Behavior:**
- Auto-generates structured filenames
- Writes PNGs and optional `.json` metadata
- Can save sprite sheets, icons, or tilesets depending on type
- Export logs per asset generated

---

### 🔎 Workflow Validation Rules

- Must contain:
  - `GenLoopInputNode`
  - At least one valid `GenLoopOutput*Node`
- If invalid:
  - CLI fails with error
  - GUI disables “Generate” with helpful feedback

---

## 🧠 Design Features

- Modular tabbed UI (Characters / Items / Environments)
- Drag-and-drop style sheet panel
- Character Slot system
- Design Page: try ideas before committing
- Batch generation with override & debug mode
- Prompt metadata preservation
- Smart output folder/file system

---

## 🚀 Roadmap: Development Milestones

---

### 🧱 Milestone 1: Project Initialization

- [ ] Monorepo setup
- [ ] README, folder scaffold
- [ ] Install docs

---

### 🧩 Milestone 2: CLI Core

#### CLI Commands
- [ ] `generate characters`
- [ ] `generate items`
- [ ] `generate environments`

#### Workflow Handling
- [ ] Load workflow `.json`
- [ ] Validate GenLoop nodes
- [ ] Override node values with CLI args

#### Execution
- [ ] Run ComfyUI
- [ ] Watch for output
- [ ] Implement `--debug`, `--override`

---

### 🧩 Milestone 3: Custom Nodes

#### GenLoopInputNode
- [ ] Accept prompt, style, type, etc.
- [ ] Output metadata
- [ ] Internal prompt formatter

#### GenLoopOutput*Node
- [ ] Character node
- [ ] Item node
- [ ] Environment node
- [ ] Save PNGs
- [ ] Log metadata

#### Node Utilities
- [ ] Slugifier
- [ ] File-safe path builder

---

### 🧱 Milestone 4: GUI App

#### Core Tabs
- [ ] Characters
- [ ] Items
- [ ] Environments
- [ ] Brainstorm
- [ ] Style Sheet
- [ ] Results

#### Character Page
- [ ] Character slots
- [ ] Lock style
- [ ] Preview generation

#### Integration
- [ ] GUI → CLI bridge
- [ ] Progress & error UI

---

### 🧱 Milestone 5: Workflow Templates

- [ ] Default character workflow
- [ ] Default item workflow
- [ ] Default environment workflow
- [ ] All workflows must include GenLoop nodes
- [ ] Published in `/workflows` folder

---

### 🧱 Milestone 6: Asset Metadata & Style

- [ ] Style sheet collection
- [ ] Slot memory for locked styles
- [ ] Asset logs (.json)

---

### 🧱 Milestone 7: Packaging

- [ ] PyInstaller build for CLI
- [ ] GUI desktop app build
- [ ] Bundle default templates & workflows

---

## 🔚 Summary

GenLoop is a full-stack, developer-friendly system that allows flexible asset generation using ComfyUI, powered by custom prompt inputs, batch control, and smart output routing. Its design is modular, expandable, and deeply integrated with real dev pipelines.

