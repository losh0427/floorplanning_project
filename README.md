# VLSI Floorplanning using Simulated Annealing

A concise and effective implementation of a floorplanning algorithm for VLSI chip design. This project finds an optimal placement for a set of circuit blocks to minimize the total chip area and wirelength, utilizing the simulated annealing optimization technique.

## Background

Floorplanning is a fundamental step in the physical design of integrated circuits (ICs). It involves arranging a set of rectangular modules (or blocks) on a chip layout to optimize certain metrics. The primary goals are:
1.  **Minimizing Area:** Placing the blocks as compactly as possible to reduce the overall silicon area, which directly impacts manufacturing cost.
2.  **Minimizing Wirelength:** Placing interconnected blocks closer to each other to reduce the total length of wires required, which improves performance and reduces power consumption.

This project employs a **slicing tree** representation to model the floorplan. A slicing tree is a binary tree where each internal node represents a vertical or horizontal cut, and each leaf node represents a block. This representation ensures that the resulting floorplan is always non-overlapping.

To find the optimal arrangement, we use **Simulated Annealing (SA)**, a probabilistic metaheuristic inspired by the annealing process in metallurgy. SA explores the solution space by iteratively making random changes (perturbations) to the slicing tree and accepting them based on a temperature-controlled probability. This allows the algorithm to escape local optima and find a globally optimal or near-optimal solution.

## Features

*   **Simulated Annealing Engine:** A robust optimizer to search for the best floorplan.
*   **Slicing Tree Representation:** Guarantees a non-overlapping placement of blocks.
*   **Cost Function:** Optimizes a weighted sum of chip area and total wirelength.
*   **File Parsing:** Reads standard academic benchmark files (`.blocks` and `.nets`).
*   **Result Visualization:** Generates an output file that can be used with a plotting tool to visualize the final floorplan.

## Getting Started

### Prerequisites

*   A C++ compiler (e.g., g++ 9.0 or later)
*   `make` build automation tool

### Compilation

Clone the repository and use the provided Makefile to compile the project:

```bash
git clone <your-repo-url>
cd floorplanning_project
make
```

If a Makefile is not available, you can compile the source files directly:

```bash
# Replace with your actual source file names
g++ -o floorplanner main.cpp parser.cpp floorplanner.cpp -O3 -std=c++17
```

### Usage

Run the executable with the input files and an output file path. The alpha parameter controls the trade-off between area and wirelength in the cost function (`cost = alpha * area + (1 - alpha) * wirelength`).

```bash
./floorplanner <alpha> <blocks_file> <nets_file> <output_file>
```

**Example:**

```bash
./floorplanner 0.5 input/apte.blocks input/apte.nets output/apte.out
```

This will run the floorplanner on the `apte` test case with equal weight for area and wirelength, and write the result to `output/apte.out`.