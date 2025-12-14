# 🧬 PyMOL Binder Viz
Visualization of protein structures in PyMOL with some functionalities useful for protein binders. To be used in the PyMOL CLI.

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
  interface A, B+C,D+E, F # Three separate chains
```
Conditionless focusing on interface:
```python
  zoom_interface
```
### `color_by_plddt` - pLDDT or B-factor Viz
```python
  color_by_plddt
  or
  color_by_b
```

### `clean` - Reset View
To reset standard cartoon
```python
  clean
```
