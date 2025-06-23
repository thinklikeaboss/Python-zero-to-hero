# src/chapter18.py

"""
Chapter 18 – Packaging & Distribution
Author: Luca Bocaletto
Description:
    Demonstrate reading your project's pyproject.toml metadata,
    inspecting installed distributions via importlib.metadata,
    and printing a simple project tree.
"""

import os
import sys

# tomllib is built-in in Python 3.11+; fall back to tomli if needed
try:
    import tomllib
except ImportError:
    import tomli as tomllib  # pip install tomli

from importlib import metadata

def demo_project_structure():
    print("== Project Structure ==")
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    for dirpath, dirnames, filenames in os.walk(root):
        level = dirpath.replace(root, "").count(os.sep)
        indent = "  " * level
        name = os.path.basename(dirpath) or root
        print(f"{indent}{name}/")
        for fname in sorted(filenames):
            print(f"{indent}  {fname}")
    print()

def demo_read_pyproject():
    print("== pyproject.toml Metadata ==")
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    pyproject_path = os.path.join(project_root, "pyproject.toml")
    try:
        with open(pyproject_path, "rb") as f:
            config = tomllib.load(f)
        proj = config.get("project", {})
        print("Name:       ", proj.get("name"))
        print("Version:    ", proj.get("version"))
        print("Description:", proj.get("description"))
        authors = proj.get("authors", [])
        if authors:
            print("Authors:    ",
                  ", ".join(a.get("name", "") for a in authors))
    except FileNotFoundError:
        print("No pyproject.toml found at", pyproject_path)
    except Exception as e:
        print("Error reading pyproject.toml:", e)
    print()

def demo_importlib_metadata():
    print("== Installed Distributions (first 5) ==")
    dists = list(metadata.distributions())[:5]
    for dist in dists:
        name = dist.metadata.get("Name", dist.metadata.get("Name".lower(), dist.name))
        print(f" - {name} {dist.version}")
    print("\n== Metadata for a Specific Package ==")
    pkg = "setuptools"
    try:
        ver = metadata.version(pkg)
        meta = metadata.metadata(pkg)
        print(f"{pkg} version: {ver}")
        print("Summary:", meta.get("Summary"))
        print("Home-page:", meta.get("Home-page"))
    except metadata.PackageNotFoundError:
        print(f"Package '{pkg}' not installed.")
    print()

def main():
    print("\n=== Chapter 18: Packaging & Distribution Demo ===\n")
    demo_project_structure()
    demo_read_pyproject()
    demo_importlib_metadata()
    print("=== End of Chapter 18 ===\n")

if __name__ == "__main__":
    main()
