# src/chapter22.py

"""
Chapter 22 – Building CLI Tools with argparse, Click & Typer
Author: Luca Bocaletto
Description:
    Demonstrate three styles of CLI creation:
      1) argparse (stdlib)
      2) Click
      3) Typer (built on Click + type hints)
    Each demo uses an in-process runner to show sample invocations.
"""

import sys
import argparse

import click
from click.testing import CliRunner as ClickRunner

import typer
from typer.testing import CliRunner as TyperRunner

# -----------------------------------------------------------------------------
# 1) argparse example
# -----------------------------------------------------------------------------
def argparse_main(argv=None):
    parser = argparse.ArgumentParser(description="Greet a user.")
    parser.add_argument("name", help="Name of the user")
    parser.add_argument("-t", "--times", type=int, default=1,
                        help="Number of greetings")
    args = parser.parse_args(argv or sys.argv[1:])
    for _ in range(args.times):
        print(f"Hello, {args.name}!")

def demo_argparse():
    print("== argparse Demo ==")
    # simulate: python chapter22.py Alice -t 2
    demo_argv = ["Alice", "-t", "2"]
    argparse_main(demo_argv)
    print()

# -----------------------------------------------------------------------------
# 2) Click example
# -----------------------------------------------------------------------------
@click.command()
@click.argument("name")
@click.option("--times", "-t", default=1, help="Number of greetings")
def click_cli(name, times):
    """Greet a user multiple times."""
    for _ in range(times):
        click.echo(f"Hello, {name}!")

def demo_click():
    print("== Click Demo ==")
    runner = ClickRunner()
    # simulate: click_cli("Bob", "--times", "3")
    result = runner.invoke(click_cli, ["Bob", "--times", "3"])
    print(result.output.strip())
    print()

# -----------------------------------------------------------------------------
# 3) Typer example
# -----------------------------------------------------------------------------
typer_app = typer.Typer()

@typer_app.command()
def greet(name: str, times: int = 1):
    """
    Greet a user multiple times.
    """
    for _ in range(times):
        typer.echo(f"Hello, {name}!")

def demo_typer():
    print("== Typer Demo ==")
    runner = TyperRunner(typer_app)
    # simulate: todo-cli greet Carol --times 2
    result = runner.invoke(["greet", "Carol", "--times", "2"])
    print(result.stdout.strip())
    print()

# -----------------------------------------------------------------------------
# Entry point
# -----------------------------------------------------------------------------
def main():
    print("\n=== Chapter 22: CLI Tools Demo ===\n")
    demo_argparse()
    demo_click()
    demo_typer()
    print("=== End of Chapter 22 ===\n")
    print("To run interactively:")
    print("  python chapter22.py Alice -t 2        # argparse")
    print("  python chapter22.py click --help       # Click CLI")
    print("  python chapter22.py greet --help       # Typer CLI\n")

if __name__ == "__main__":
    main()
