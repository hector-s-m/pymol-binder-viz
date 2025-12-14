# 🧬 PyMOL Binder Viz
Visualization of protein structures in PyMOL with some functionalities useful for protein binders. To be used in the PyMOL CLI.

## 🚀 Quick Start
Download to home PyMOL directory, and first run:
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
### `interface` - Highlight atoms at an interface
```python
  interface
```
```python
  interface A, B+C # Specify multi-chain entities (e.g., A=antigen, B+C=Fab)
```
```python
  interface A, B, C # Three separate chains
```
Also possible to execute for conditionless focusing on interface
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
