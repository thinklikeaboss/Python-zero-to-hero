# Python Zero to Hero

> A comprehensive, hands-on guide to mastering Python—from the basics to advanced topics—complete with HTML lessons and runnable demo scripts.

**Author:** Luca Bocaletto  
**Repository:** https://github.com/bocaletto-luca/python-zero-to-hero

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Running the HTML Lessons](#running-the-html-lessons)  
   - [Running the Demo Scripts](#running-the-demo-scripts)  
5. [Usage Examples](#usage-examples)  
6. [Contributing](#contributing)  
7. [License](#license)  
8. [Acknowledgments](#acknowledgments)  

---

## Overview

Python Zero to Hero is designed as both a **learning resource** and a **reference**. Each chapter delivers:

- A self-contained **HTML lesson** with code snippets and exercises.  
- A **Python demo script** (`chapterXX.py`) that you can execute to see concepts in action.  

Start at Chapter 1 to build solid fundamentals, and progress through advanced topics such as web development, data analysis, packaging, and more.

---

## Features

- **Chapters 1–10:** Core language constructs (variables, control flow, functions, OOP)  
- **Chapters 11–15:** Debugging, testing, concurrency, web APIs, data analysis  
- **Chapters 16–20:** Decorators, context managers, typing, packaging, databases  
- **Chapters 21–22:** Building web apps/APIs with Flask & FastAPI; CLI tools with argparse, Click & Typer  
- **HTML lessons** with syntax highlighting and Bootstrap styling  
- **Runnable demo scripts** under `src/` for hands-on experimentation  
- **Exercises** at the end of each chapter to reinforce learning  

---

## Project Structure

```text
python-zero-to-hero/
├── CHAPTER_INDEX.html       ← Homepage linking all chapters
├── chapter01.html           ← Lesson HTML
├── chapter02.html
│   …
├── chapter22.html
├── README.md                ← You are here
└── src/
    ├── chapter01.py         ← Demo scripts
    ├── chapter02.py
    │   …
    └── chapter22.py
```

- **Root** contains all `chapterXX.html` files and the index.  
- **src/** holds Python scripts matching each chapter.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- (Optional) A static-file server to serve HTML lessons  
- Internet connection for external CSS/JS (Bootstrap, Highlight.js)

### Installation

```bash
# Clone the repo
git clone https://github.com/bocaletto-luca/python-zero-to-hero.git
cd python-zero-to-hero
```

### Running the HTML Lessons

You can simply open any `chapterXX.html` in your browser. For best results (to avoid CORS issues), run a local server:

```bash
# Python 3:
python -m http.server 8000
# Then visit http://localhost:8000/chapter01.html
```

### Running the Demo Scripts

Each chapter has a corresponding Python file under `src/`. To run:

```bash
# Example: run Chapter 14 demo
python src/chapter14.py
```

They’ll print step-by-step demos of core concepts, so you can experiment and modify as you learn.

---

## Usage Examples

- **Debugging and Testing (Ch 12):**  
  `python src/chapter12.py` shows how to use `pdb`, `logging` and `unittest`.  

- **Async I/O (Ch 13):**  
  `python src/chapter13.py` demonstrates threading, multiprocessing, futures, and `asyncio`.  

- **Web APIs (Ch 14):**  
  `python src/chapter14.py` sends GET/POST requests to httpbin.org.  

- **Data Analysis (Ch 15):**  
  `python src/chapter15.py` walks through NumPy and pandas operations, plus plotting.  

- **Packaging (Ch 18):**  
  `python src/chapter18.py` reads your `pyproject.toml` and inspects distributions.  

- **Web Apps (Ch 21):**  
  `python src/chapter21.py` runs embedded test-clients for Flask and FastAPI.

---

## Contributing

Contributions, issues and feature requests are welcome! To get started:

1. Fork the repository.  
2. Create a new branch: `git checkout -b feature/YourFeature`.  
3. Commit your changes: `git commit -m 'Add some feature'`.  
4. Push to the branch: `git push origin feature/YourFeature`.  
5. Open a Pull Request on GitHub.

Please ensure code demos remain in `src/` and lessons stay in `chapterXX.html` format. Add exercises for new chapters and update the README accordingly.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute as you see fit.

---

## Acknowledgments

- [Bootstrap](https://getbootstrap.com) for responsive layout  
- [Highlight.js](https://highlightjs.org) for code syntax highlighting  
- Inspiration from thousands of open-source Python tutorials and guides  

---

Happy coding and thanks for checking out **Python Zero to Hero**! 🚀
