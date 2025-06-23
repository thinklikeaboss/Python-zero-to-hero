# Python Zero to Hero
#### Author: Bocaletto Luca

> A hands-on, full-stack roadmap to mastering Python—starting from the basics all the way to web apps, CLI tools, packaging, and beyond.

**Author:** Luca Bocaletto  
**Repo:** https://github.com/bocaletto-luca/python-zero-to-hero  

---

## 📖 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Serving the HTML Lessons](#serving-the-html-lessons)  
   - [Running the Demo Scripts](#running-the-demo-scripts)  
5. [Chapters & Content](#chapters--content)  
6. [Contributing](#contributing)  
7. [License](#license)  
8. [Acknowledgments](#acknowledgments)  

---

## 🌟 Overview

**Python Zero to Hero** is your companion from day-one Python up to real-world applications.  
Each chapter ships with:

- A **self-contained HTML lesson** (`chapterXX.html`) styled with Bootstrap & Highlight.js.  
- A **runnable demo** script (`src/chapterXX.py`) illustrating every concept step-by-step.  
- **Exercises** at the end of the lesson to reinforce learning.

Whether you learn by reading, experimenting or building side projects, this repo has you covered.

---

## 🔧 Features

- **Foundations:** Syntax, data types, control flow, functions, modules, packages.  
- **Intermediate:** OOP, debugging, logging, testing, assertions.  
- **Advanced Topics:** Concurrency (threads, processes, asyncio), HTTP APIs, JSON/XML, data analysis (NumPy, pandas), decorators, context managers, type hints.  
- **Tooling:** Packaging & distribution (setuptools, wheels, PyPI), database access (sqlite3, SQLAlchemy Core & ORM, Alembic), profiling & optimization, web frameworks (Flask, FastAPI), CLI frameworks (argparse, Click, Typer).  
- **Full-stack approach:** From code examples to deployment commands.  

---

## 📂 Project Structure

```text
python-zero-to-hero/
├── chapter01.html      ← HTML lesson 1: Hello, variables & types
├── chapter02.html      ← HTML lesson 2: Control flow & loops
│   …
├── chapter22.html      ← HTML lesson 22: argparse, Click & Typer
├── README.md           ← This document
└── src/
    ├── chapter01.py    ← Demo script 1
    ├── chapter02.py    ← Demo script 2
    │   …
    └── chapter22.py    ← Demo script 22
```

- **Root folder**: All your static HTML lessons and the README.  
- **src/**: Python scripts that correspond to each chapter.  

---

## 🚀 Getting Started

### Prerequisites

- **Python** 3.8+  
- **Git** (for cloning)  
- (Optional) A modern browser  

### Installation

```bash
git clone https://github.com/bocaletto-luca/python-zero-to-hero.git
cd python-zero-to-hero
```

### Serving the HTML Lessons

For best results, serve files over HTTP:

```bash
# Quick HTTP server (Python 3.x)
python -m http.server 8000
```

Visit `http://localhost:8000/chapter01.html`, `chapter02.html`, … up to `chapter22.html`.

### Running the Demo Scripts

All demos live under `src/`. To execute:

```bash
python src/chapter14.py    # e.g., JSON, XML & HTTP Requests demo
python src/chapter20.py    # e.g., Database & ORM demo
```

Each script prints annotated outputs so you can follow along interactively.

---

## 📚 Chapters & Content

| Chapter | Topic                                                | HTML Lesson         | Demo Script        |
| ------- | ---------------------------------------------------- | ------------------- | ------------------ |
| 01      | Hello, Variables & Types                             | chapter01.html      | src/chapter01.py   |
| 02      | Control Flow & Loops                                 | chapter02.html      | src/chapter02.py   |
| 03      | Functions & Modules                                  | chapter03.html      | src/chapter03.py   |
| 04      | Data Structures: Lists, Tuples, Dicts, Sets          | chapter04.html      | src/chapter04.py   |
| 05      | File I/O & Exceptions                                | chapter05.html      | src/chapter05.py   |
| 06      | Object-Oriented Programming                          | chapter06.html      | src/chapter06.py   |
| 07      | Advanced OOP: Inheritance, Dunder Methods            | chapter07.html      | src/chapter07.py   |
| 08      | Functional Programming: Lambdas, Map/Filter, Comprehensions | chapter08.html      | src/chapter08.py   |
| 09      | Modules, Packages & Virtual Environments             | chapter09.html      | src/chapter09.py   |
| 10      | Packaging & Distribution Basics                      | chapter10.html      | src/chapter10.py   |
| 11      | Debugging, Logging & Testing                         | chapter11.html      | src/chapter11.py   |
| 12      | Concurrency & Parallelism                            | chapter12.html      | src/chapter12.py   |
| 13      | JSON, XML & HTTP Requests                            | chapter13.html      | src/chapter13.py   |
| 14      | Data Analysis with pandas & NumPy                    | chapter14.html      | src/chapter14.py   |
| 15      | Decorators & Context Managers                        | chapter15.html      | src/chapter15.py   |
| 16      | Type Hints & Static Typing                           | chapter16.html      | src/chapter16.py   |
| 17      | Packaging & PyPI Distribution                        | chapter17.html      | src/chapter17.py   |
| 18      | Profiling & Performance Optimization                  | chapter18.html      | src/chapter18.py   |
| 19      | Database Access (sqlite3) & SQLAlchemy Core & ORM    | chapter19.html      | src/chapter19.py   |
| 20      | Web Development: Flask & FastAPI                     | chapter20.html      | src/chapter20.py   |
| 21      | Building CLI Tools: argparse, Click & Typer          | chapter21.html      | src/chapter21.py   |
| 22      | (Future) Advanced Topics…                            | chapter22.html      | src/chapter22.py   |

> **Tip:** Jump to any chapter by opening the corresponding HTML or running its demo script.

---

## 🤝 Contributing

Contributions are more than welcome!  
1. Fork the repo.  
2. Create a feature branch: `git checkout -b feature/awesome-topic`.  
3. Commit your changes: `git commit -m "Add chapter XX: awesome topic"`.  
4. Push to your branch: `git push origin feature/awesome-topic`.  
5. Open a Pull Request.  

Please:

- Follow existing naming conventions (`chapterXX.html`, `src/chapterXX.py`).  
- Include code demos, HTML lesson, and exercises.  
- Update this README’s Table of Contents.

---

## 📄 License

This project is released under the **MIT License**.  
See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **Bootstrap** for responsive, modern layout  
- **Highlight.js** for code syntax highlighting  
- The vibrant Python community for inspiration and best practices  

---

Happy learning! 🚀  
— _Luca Bocaletto_  
