# AI Tools Lab

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

A beginner-friendly Python project that combines a **Bubble Sort** implementation with a small set of handy **utility functions**. Built as a college project, the code is kept simple, well-commented, and easy to read, making it a good starting point for anyone learning algorithms and clean Python.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Running the Tests](#running-the-tests)
- [Contributors](#contributors)
- [Contributing](#contributing)
- [License](#license)

---

## Features

**Sorting**
- `bubble_sort(arr)`: sorts a list of numbers in ascending order using the Bubble Sort algorithm

**Utility functions**
- `is_palindrome(s)`: checks whether a string reads the same forwards and backwards (ignores case, spaces, and punctuation)
- `count_words(text)`: counts the number of words in a piece of text
- `celsius_to_fahrenheit(c)`: converts a temperature from Celsius to Fahrenheit

---

## Project Structure

```
ai-tools-lab/
├── sorting.py      # Bubble Sort implementation
├── utils.py        # Utility functions
├── README.md       # Project documentation
└── LICENSE         # MIT License
```

---

## Installation

**Requirements:** Python 3.8 or higher. No external libraries are needed.

1. **Clone the repository**

   ```bash
   git clone https://github.com/saanvisabikhi53-ctrl/ai-tools-lab.git
   ```

2. **Move into the project folder**

   ```bash
   cd ai-tools-lab
   ```

3. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

That's it. The modules are ready to import.

---

## Usage

### Bubble Sort

```python
from sorting import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(numbers))   # [11, 12, 22, 25, 34, 64, 90]
```

Bubble Sort works by repeatedly stepping through the list, comparing neighboring items, and swapping them if they are in the wrong order. After each pass, the largest unsorted value "bubbles up" to its correct position at the end of the list.

| Case    | Time Complexity |
|---------|-----------------|
| Best    | O(n) (with an early-exit check) |
| Average | O(n²)           |
| Worst   | O(n²)           |

### Utility functions

```python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

# Check for palindromes
print(is_palindrome("racecar"))                          # True
print(is_palindrome("A man, a plan, a canal: Panama"))   # True
print(is_palindrome("hello"))                            # False

# Count words
print(count_words("Hello world"))                        # 2
print(count_words("  Python   is   fun  "))              # 3

# Convert temperatures
print(celsius_to_fahrenheit(0))                          # 32.0
print(celsius_to_fahrenheit(100))                        # 212.0
print(celsius_to_fahrenheit(-40))                        # -40.0
```

---

## Running the Tests

`utils.py` includes a few quick checks that run when the file is executed directly:

```bash
python utils.py
```

---

## Contributors

| Name               | Role                |
|--------------------|---------------------|
| **Saanvi Sabikhi** | Author & Maintainer |

---

## Contributing

Contributions, suggestions, and bug reports are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Saanvi Sabikhi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```