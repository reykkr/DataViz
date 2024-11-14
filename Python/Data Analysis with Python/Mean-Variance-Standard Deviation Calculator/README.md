# Mean-Variance-Standard Deviation Calculator

## Overview
The **Mean-Variance-Standard Deviation Calculator** project involves implementing a Python function that computes statistical measures (mean, variance, standard deviation, min, max, and sum) for a given list of numbers. The input list is reshaped into a 3x3 matrix, and various calculations are performed along different axes as well as the flattened matrix.

## Purpose
The purpose of this project is to:

- Implement fundamental statistical calculations using **NumPy**.
- Learn how to manipulate and reshape arrays using **NumPy**.
- Gain hands-on experience with mathematical operations along multiple axes of an array.

## Key Skills Demonstrated
1. **NumPy Array Manipulation**
   - Used **NumPy** to reshape a list of numbers into a 3x3 matrix.

2. **Statistical Calculations**
   - Calculated mean, variance, standard deviation, max, min, and sum along rows, columns, and the entire matrix.

3. **Error Handling**
   - Implemented error handling to ensure the input list contains exactly nine numbers.

## Tools Used
- **Python**: Main programming language for data manipulation and statistical calculations.
- **NumPy**: Used for array manipulation and performing mathematical calculations.

## Project Components
1. **Matrix Reshaping**
   - Converted the input list of nine numbers into a 3x3 **NumPy** matrix.

2. **Statistical Measure Calculations**
   - Calculated statistical metrics (mean, variance, standard deviation, max, min, and sum) along both axes (rows and columns) and for the entire matrix.

3. **Function Implementation**
   - Implemented the `calculate(numbers)` function that returns a dictionary containing the computed values.

## Getting Started
To run the project:

1. Ensure you have **Python** installed along with **NumPy**.
2. Run the script `mean_var_std.py` and call the `calculate(numbers)` function with a list of nine numbers to obtain the statistical calculations.
#
## Example Usage
```python

from mean_var_std import calculate

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])) 
```

## Notes
This project demonstrates the use of NumPy for statistical analysis on a small dataset, highlighting array manipulation, mathematical operations, and data aggregation techniques.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.