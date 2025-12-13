# 🧬 PyMOL Binder Viz
Visualization of protein structures in PyMOL with some functionalities useful for protein binders.

## 🚀 Quick Start

run polish.py

text

This applies publication settings: soft shadows, smooth rendering, no shine, 60% surface transparency.

## 🎨 Commands

### `binder` - Highlight Your Designed Binder

binder A # Single chain binder
binder B+C # Multi-chain binder

text

**What it does:**
- 🟠 Binder → **salmon**
- 🔵 Target → **teal**  
- Shows sticks within 4Å of interface
- Elements colored (N=blue, O=red, S=yellow)

### `interface` - Analyze Protein Interfaces

interface # Auto-detect all chains
interface A, B+C # Specify entities
interface A, B, C # Three separate chains

text

**What it does:**
- 🌈 Colors each entity differently
- Shows interface residues (within 4Å)
- ⚡ Displays hydrogen bonds (dashed lines)

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
