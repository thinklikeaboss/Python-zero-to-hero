# src/chapter8.py

"""
Chapter 8 – File I/O
Author: Luca Bocaletto
Description: Demonstrate Python's file input/output:
             reading/writing text, CSV, and binary files
             using context managers.
"""

import csv
import os

def demo_read_text():
    print("== Reading Text File ==")
    # Prepare a sample text file
    sample = "sample.txt"
    with open(sample, "w", encoding="utf-8") as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    # Read entire content
    with open(sample, "r", encoding="utf-8") as f:
        content = f.read()
        print("Full content:\n", content, sep="")
    # Read lines
    with open(sample, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("Lines list:", lines)
    # Iterate line by line
    print("Iterate lines:")
    with open(sample, "r", encoding="utf-8") as f:
        for line in f:
            print("›", line.strip())
    print()

def demo_write_text():
    print("== Writing Text File ==")
    out = "output.txt"
    lines = ["Header\n", "First data line\n", "Second data line\n"]
    with open(out, "w", encoding="utf-8") as f:
        f.write("=== OUTPUT ===\n")
        f.writelines(lines)
    print(f"Written {len(lines)+1} lines to '{out}'.\n")

def demo_csv():
    print("== CSV File Handling ==")
    csv_file = "demo.csv"
    rows = [
        ["ID", "Name", "Score"],
        [1, "Alice", 85],
        [2, "Bob", 92],
        [3, "Charlie", 78],
    ]
    # Write CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to '{csv_file}'.")
    # Read CSV
    print("Read back:")
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    print()

def demo_binary():
    print("== Binary File I/O ==")
    src = "binary.dat"
    dst = "binary_copy.dat"
    # Create a binary file with bytes 0–127
    data = bytes(range(128))
    with open(src, "wb") as f:
        f.write(data)
    size = os.path.getsize(src)
    print(f"Created '{src}' ({size} bytes).")
    # Copy in chunks
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while chunk := fin.read(32):
            fout.write(chunk)
    copy_size = os.path.getsize(dst)
    print(f"Copied to '{dst}' ({copy_size} bytes).")
    print()

def main():
    print("\n=== Chapter 8: File I/O Demo ===\n")
    demo_read_text()
    demo_write_text()
    demo_csv()
    demo_binary()
    print("=== End of Chapter 8 ===\n")

if __name__ == "__main__":
    main()
