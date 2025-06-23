# src/chapter15.py

"""
Chapter 15 – Data Analysis with pandas & NumPy
Author: Luca Bocaletto
Description:
    Demonstrate NumPy arrays, pandas Series/DataFrame operations,
    indexing & selection, aggregation & group-by, handling missing data,
    and basic plotting with matplotlib.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def demo_numpy():
    print("== NumPy Arrays Demo ==")
    arr = np.array([1, 2, 3, 4])
    mat = np.arange(9).reshape(3, 3)
    print("1D array:", arr)
    print("2D array:\n", mat)
    print("arr + 10 →", arr + 10)
    print("mean:", arr.mean(), "sum:", arr.sum())
    print()

def demo_pandas():
    print("== pandas Series & DataFrame Demo ==")
    # Series
    s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print("Series:\n", s)
    # DataFrame
    df = pd.DataFrame({
        'col1': [1, 2, 3, 2, 1],
        'col2': ['x', 'y', 'x', 'y', 'x']
    })
    print("\nDataFrame:\n", df)
    print()

def demo_selection():
    print("== Indexing & Selection Demo ==")
    df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': ['x', 'y', 'z']
    })
    print("loc[0, 'col1'] →", df.loc[0, 'col1'])
    print("iloc[0:2, 0:2]:\n", df.iloc[0:2, 0:2])
    print("boolean mask (col1 > 1):\n", df[df['col1'] > 1])
    print()

def demo_groupby():
    print("== Aggregation & GroupBy Demo ==")
    df = pd.DataFrame({
        'group': ['A', 'A', 'B', 'B', 'A'],
        'value': [5, 3, 4, 2, 1]
    })
    print("Mean:", df['value'].mean(), "Sum:", df['value'].sum())
    grouped = df.groupby('group')['value'].agg(['mean', 'count'])
    print("GroupBy result:\n", grouped)
    print()

def demo_missing_apply():
    print("== Missing Data & apply() Demo ==")
    df = pd.DataFrame({
        'col1': [1, np.nan, 3, np.nan, 5]
    })
    print("Original:\n", df)
    df['col1'] = df['col1'].fillna(0)
    df['col2'] = df['col1'].apply(lambda x: x**2)
    print("\nFilled & squared:\n", df)
    print()

def demo_plotting():
    print("== Plotting Demo ==")
    df = pd.DataFrame({
        'col1': [1, 3, 2, 4],
        'col2': ['A', 'B', 'A', 'B']
    })
    # Line plot
    df['col1'].plot(title='col1 over index')
    plt.show()
    # Bar plot
    df.groupby('col2')['col1'].sum().plot(kind='bar', title='sum by col2')
    plt.show()
    print()

def main():
    print("\n=== Chapter 15: Data Analysis Demo ===\n")
    demo_numpy()
    demo_pandas()
    demo_selection()
    demo_groupby()
    demo_missing_apply()
    demo_plotting()
    print("=== End of Chapter 15 ===\n")

if __name__ == "__main__":
    main()
