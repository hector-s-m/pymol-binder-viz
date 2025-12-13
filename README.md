# 🧬 PyMOL Binder Viz
Visualization of protein structures in PyMOL with some functionalities useful for protein binders.

## 🚀 Quick Start

Download to home PyMOL directory, and first run:
```python
  run polish.py

```
This applies publication settings: soft shadows, smooth rendering, no shine, 60% surface transparency.

## 🎨 Commands

### `binder` - Highlight Binder and interacting residues

```python
  binder A # Single chain binder (e.g., miniproteins, scFvs, nanobodies)
  or
  binder B+C # Multi-chain binder (e.g., Fabs or multimeric binders)
```

### `interface` - Highlight atoms at an interface
interface # Auto-detect all chains
interface A, B+C # Specify clustered entities (e.g., A=antigen, B+C=Fab)
interface A, B, C # Three separate chains

```python
  interface # Auto-detect all chains
  interface A, B+C # Specify clustered entities (e.g., A=antigen, B+C=Fab)
  interface A, B, C # Three separate chains
```
