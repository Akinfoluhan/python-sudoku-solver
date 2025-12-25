# Python Sudoku Solver

A command-line Sudoku solver built in Python that solves standard 9×9 puzzles using recursive backtracking with MRV (Minimum Remaining Values) pruning. Includes board validation, optional step-by-step visualization, and optional solve-time measurement.

---

## Features

- Solves 9×9 Sudoku puzzles using recursive backtracking
- Constraint checking across rows, columns, and 3×3 subgrids
- MRV heuristic to reduce backtracking (chooses the next empty cell with the fewest valid candidates)
- Validation to detect invalid starting boards
- Optional visualization of placements and backtracking steps
- Optional timing output in milliseconds

---

## Tech Stack

- Python
- NumPy
- argparse (CLI)

---

## Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/Akinfoluhan/python-sudoku-solver.git
cd python-sudoku-solver
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run normally

```bash
python solver.py
```

### Enable step-by-step visualization

```bash
python solver.py --visualize
```

### Control visualization speed (seconds)

```bash
python solver.py --visualize --delay 0.01
```

### Disable timing output

```bash
python solver.py --no-time
```

---

## Command-Line Options

- `--visualize` : prints each placement and backtrack step
- `--delay <float>` : delay between visualization steps (default: `0.03`)
- `--time` / `--no-time` : enable/disable timing output (default: timing on)

---

## Project Structure

```text
python-sudoku-solver/
├── solver.py
├── README.md
└── requirements.txt
```

---

## Algorithm Overview

1. Validate the starting board (no contradictions in row/col/subgrid).
2. Select an empty cell using MRV (fewest legal candidates).
3. Try numbers 1–9 that satisfy Sudoku constraints.
4. Recurse until solved; backtrack when a dead end is reached.

---

## Future Improvements

- Read puzzles from a text file or user input
- Add unit tests
- Add a puzzle generator
- Image-based input using OpenCV + overlay solution
