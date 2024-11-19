# 0x07. Rotate 2D Matrix

## Algorithm
- **Python**
- **Weight:** 1

## Project Timeline
- **Start:** Nov 18, 2024, 4:00 AM
- **End:** Nov 22, 2024, 4:00 AM
- **Checker Release:** Nov 19, 2024, 4:00 AM
- **Auto Review:** At the deadline

## Objective
Implement an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This project requires understanding matrix manipulation and in-place operations in Python.

## Key Concepts

### Matrix Representation in Python
- Represent 2D matrices using lists of lists.
- Access and modify elements in a 2D matrix.

### In-place Operations
- Perform operations without creating a copy of the data structure.
- Minimize space complexity by modifying the matrix in place.

### Matrix Transposition
- Understand transposing a matrix (swap rows and columns).
- Implement matrix transposition as a step in rotation.

### Reversing Rows in a Matrix
- Reverse the order of rows as part of the rotation process.

### Nested Loops
- Use nested loops to iterate through 2D data structures.
- Modify elements within nested loops for rotation.

## Resources

### Python Official Documentation
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### GeeksforGeeks Articles
- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

By understanding these concepts and utilizing the resources, you can approach the problem methodically: first transpose the matrix and then reverse each row to achieve a 90-degree clockwise rotation.

## Additional Resources
- Mock Technical Interview

## Requirements

### General
- Editors: `vi`, `vim`, `emacs`
- Files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
- Files should end with a new line
- First line: `#!/usr/bin/python3`
- A `README.md` file is mandatory
- Code should use `pycodestyle` style (version 2.8.0)
- No module imports allowed
- All modules and functions must be documented
- Files must be executable

## Tasks

### 0. Rotate 2D Matrix
**Mandatory**

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

- **Prototype:** `def rotate_2d_matrix(matrix):`
- **Note:** Do not return anything. The matrix must be edited in-place.
- **Assumption:** The matrix will have 2 dimensions and will not be empty.

#### Example
```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
