# 🧬 PyMOL Binder Viz
Visualization of protein structures in PyMOL with some functionalities useful for protein binders.

## 🚀 Quick Start

Download to home PyMOL directory, and run:
```python
  run polish.py

```
This applies publication settings: soft shadows, smooth rendering, no shine, 60% surface transparency.

## 🎨 Commands

### `binder` - Highlight Binder and interacting residues

binder A # Single chain binder (e.g., miniproteins, scFvs, nanobodies)
binder B+C # Multi-chain binder (e.g., Fabs or multimeric binders)

### `interface` - Highlight atoms at an interface
interface # Auto-detect all chains
interface A, B+C # Specify clustered entities (e.g., A=antigen, B+C=Fab)
interface A, B, C # Three separate chains

## 💡 Typical Workflow

fetch 7abc
run polish.py
binder B # Highlight binder B
ray 2400, 2400 # High-res render
png figure.png

text

## 📝 Pro Tips

- Reset everything: re-run `polish.py`
- Adjust view after commands with `zoom` and `orient`
- For ultra-quality: `ray 4800, 4800`

## 📄 License

MIT - Use freely! ✨
