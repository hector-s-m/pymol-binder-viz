# 🧬 PyMOL Binder Viz
Visualization of protein structures in PyMOL with some functionalities useful for protein binders. To be used in the PyMOL CLI.

Coloring and aesthetics based on my personal taste 😬

## 🚀 Quick Start
Download to home PyMOL directory, and always first run:
```python
  run polish.py
```
This applies preliminary publication-quality settings.

## 🎨 Commands
### `binder` - Highlight Binder and interacting residues
```python
  binder A # Single chain binder (e.g., miniproteins, scFvs, nanobodies)
```
  or
```python
  binder B+C # Multi-chain binder (e.g., Fabs or multimeric binders)
```
### `interface` - Highlight interface atoms
Conditionless highlighting of all interfaces:
```python
  interface
```
Syntax for more complex interfaces:
```python
  interface A, B+C, D+E, F
```
Conditionless focusing on interface:
```python
  zoom_interface
```
### `color_by_plddt` - pLDDT or B-factor Viz
Color with variable radius putty. Similar to preset--> b-factor putty but only applying putty on low pLDDT loops.
```python
  color_by_plddt # For predicted structures
```
  or
```python
  color_by_b # For experimental structures
```

### `clean` - Reset View
To reset standard cartoon
```python
  clean
```
