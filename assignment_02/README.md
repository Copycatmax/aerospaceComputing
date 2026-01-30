# Assignment 2: Linear System Solvers & Direct Methods

## Overview
This assignment explores direct methods for solving systems of linear equations Ax=b, comparing accuracy and computational efficiency of different approaches.

## Topics Covered

### Numerical Methods
- **Cramer's Rule**
  - Determinant-based solution method
  - Computationally expensive for large systems (O(n!))
  - Useful for theoretical understanding
  
- **Gaussian Elimination with Pivoting**
  - Row reduction with scaled partial pivoting
  - O(n³) complexity
  - Robust for general matrices
  
- **LU Decomposition**
  - Matrix factorization: A = LU
  - Efficient for multiple right-hand sides
  - Separate decomposition and solution phases

- **Matrix Inversion**
  - Computing A⁻¹ for matrix inverse
  - Residual error analysis

### Performance Analysis
- Solving systems of varying sizes (3×3 to 11×11)
- Comparing computational time and accuracy
- Residual error calculation: ||Ax - b||
- Benchmarking solver efficiency

## Key Python Libraries
- **NumPy**: Matrix operations and linear algebra (`np.linalg.det`, `np.dot`)
- **Pandas**: Data organization and results tabulation
- **Matplotlib**: Performance comparison plots
- **aeromod**: Custom module functions
  - `cramer()` - Cramer's rule implementation
  - `gaussPivot()` - Gaussian elimination with pivoting
  - `LUdecomp()` - LU decomposition with pivoting
  - `LUsolve()` - Forward/backward substitution

## Files
- `AEEM_2058_Max_Dittman_HW2.ipynb` - Jupyter notebook with solver implementations and comparisons
- `Assignment 2.pdf` - Problem specifications
- `README.md` - This file

## Aerospace Applications
- Structural analysis requiring solution of large linear systems
- Finite element analysis (FEA) mesh equations
- Load distribution calculations in aircraft structures
- Real-time computing requirements for flight control systems

## Learning Outcomes
Students will be able to:
- Implement multiple direct methods for solving linear systems
- Analyze computational complexity and efficiency trade-offs
- Understand when to use different solution methods
- Verify solution accuracy through residual error analysis
- Recognize the importance of pivoting for numerical stability
