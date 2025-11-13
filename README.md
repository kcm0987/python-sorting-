
# python-sorting

A collection of classic sorting algorithm implementations in Python, intended for learning, comparison, and benchmarking.

![output](https://github.com/kcm0987/python-sorting-/blob/95769cfe28f0986039d3a01305cb4bdd4b64dfba/Screenshot%202025-11-13%20220956.png)


Badges
- Build / CI: (add your CI badge)
- License: MIT (or your chosen license)
- Python: (add supported Python versions badge)

## Table of contents
- [Overview](#overview)
- [Features](#features)
- [Algorithms included](#algorithms-included)
- [Installation](#installation)
- [Usage](#usage)
  - [As a library](#as-a-library)
  - [Command-line](#command-line)
- [Examples](#examples)
- [Complexity](#complexity)
- [Benchmarks](#benchmarks)
- [Project structure](#project-structure)
- [Contributing](#contributing)
- [Testing](#testing)
- [License](#license)
- [Author](#author)

## Overview
This repository provides straightforward, well-documented Python implementations of common sorting algorithms. It is useful for students, educators, and developers who want to study algorithm behavior, compare performance, or use a specific implementation.

## Features
- Clear, idiomatic Python implementations
- In-place and out-of-place variants where appropriate
- Unit tests and simple benchmarking tools
- Sorted/unsorted input examples
- Documentation and complexity notes for each algorithm

## Algorithms included
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort (Lomuto/Hoare variants)
- Heap Sort

## Installation
Clone the repository:
git clone https://github.com/kcm0987/python-sorting-.git
cd python-sorting-

Optionally create a virtual environment:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Install dev dependencies (if provided):
pip install -r requirements.txt

## Usage

### As a library
Import the algorithm you want and call it:

python
from sorting import quick_sort, merge_sort

arr = [5, 3, 8, 1, 2]
sorted_arr = quick_sort(arr)        # if implementation returns new list
# or for in-place sorts:
# quick_sort(arr, 0, len(arr) - 1)
print(sorted_arr)

(Adjust the import path to match your package layout — e.g., from python_sorting import quick_sort.)

### Command-line
If you include a CLI runner (scripts/run_sort.py), you can run:
python -m scripts.run_sort --algorithm quick_sort --input "5 3 8 1 2"

A simple CLI implementation might accept:
- --algorithm: name of algorithm
- --size: size of random array to generate
- --seed: random seed
- --benchmark: run multiple iterations for timing

## Examples

Sorting a list with merge sort:

python
from sorting.merge_sort import merge_sort
data = [9, 4, 6, 2, 7]
print("Before:", data)
print("After: ", merge_sort(data))

Benchmark example (simple):

python
import timeit
from sorting import quick_sort
setup = "from sorting import quick_sort; import random; arr = random.sample(range(10000), 1000)"
stmt = "quick_sort(arr.copy())"
print(timeit.timeit(stmt, setup=setup, number=50))

## Complexity

Algorithm | Worst-case | Average | Best-case | Space
--- | ---: | ---: | ---: | ---:
Bubble Sort | O(n^2) | O(n^2) | O(n) | O(1)
Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1)
Insertion Sort | O(n^2) | O(n^2) | O(n) | O(1)
Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n)
Quick Sort | O(n^2) | O(n log n) | O(n log n) | O(log n) (avg)
Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1)



## Benchmarks
To run the included benchmarks:
- Ensure dependencies are installed (e.g., numpy if used)
- Run: python -m benchmarks.run_all
- Results are printed and optionally saved to a CSV for plotting

Tips:
- Benchmark on representative input sizes
- Test on random, sorted, and reverse-sorted inputs to see behavior differences
- Use timeit or perf_counter for more accurate timing

## Project structure
A recommended layout (adjust to your repo):
.
├── sorting/                # package code
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── ...
├── scripts/
│   └── run_sort.py         # CLI runner
├── benchmarks/
│   └── run_all.py
├── tests/
│   └── test_sorting.py
├── requirements.txt
└── README.md

## Contributing
Contributions are welcome!
- Fork the repository
- Create a feature branch: git checkout -b feature/my-algo
- Add tests for new algorithms / edge cases
- Run tests and linters
- Submit a pull request with a clear description and rationale

Guidelines:
- Follow PEP 8
- Keep implementations readable and documented
- Include complexity notes and any trade-offs

## Testing
Use pytest:
pip install -r requirements-dev.txt
pytest

Add tests in the tests/ directory. Test edge cases:
- empty list
- single-element list
- list with duplicates
- already sorted list
- reverse-sorted list

## License
This project is licensed under the MIT License — see the LICENSE.md file for details. (Change if you prefer another license.)

## Author
kcm0987 — feel free to open issues or pull requests.


