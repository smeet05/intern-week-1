# Day 2 – Python Data Handling & CSV Analysis

## Overview

Day 2 focused on working with Python data structures, processing data, and performing basic CSV analysis.

## Topics Covered

* Lists and dictionaries
* String manipulation
* `split()` and `map()`
* Reading and processing CSV files
* Basic data analysis
* Loops and conditional statements
* Functions
* Calculating simple statistics from data

## Exercises

### 01 – List/Data Processing

Worked with lists and performed basic operations on their elements.

### 02 – Dictionary/Data Processing

Used dictionaries to store and process key-value data.

### 03 – String Processing

Practiced manipulating and analyzing strings using Python.

### 04 – Data Conversion

Used `split()` and `map()` to convert user input into usable Python data types.

### 05 – CSV Analysis

Read data from a CSV file and performed basic analysis on the dataset.

## Key Python Concepts Learned

### `split()`

`split()` separates a string into multiple parts.

Example:

```python
numbers = input().split()
```

If the input is:

```text
10 20 30 40
```

Python converts it into:

```python
["10", "20", "30", "40"]
```

### `map()`

`map()` applies a function to every element of an iterable.

Example:

```python
numbers = list(map(int, input().split()))
```

This converts:

```text
10 20 30
```

into:

```python
[10, 20, 30]
```

## CSV Analysis

CSV stands for **Comma-Separated Values**.

CSV files are commonly used to store tabular data such as:

* Student records
* Sales data
* Employee information
* Transaction records
* Datasets used for analysis and machine learning

In this exercise, Python was used to read the CSV data and extract useful information from it.

## Learning Outcome

By completing Day 2, I practiced handling structured data in Python and learned how Python can be used to process and analyze real-world datasets stored in CSV format.
