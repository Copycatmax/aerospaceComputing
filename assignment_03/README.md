# Assignment 3: Iterative Methods for Linear Systems

## Overview
This assignment focuses on iterative methods for solving large sparse systems of linear equations, particularly well-suited for problems where direct methods become computationally expensive.

## Topics Covered

### Numerical Methods
- **Gauss-Seidel Iteration**
  - Iterative refinement with relaxation parameter ω
  - Automatic computation of optimal relaxation factor
  - Convergence criteria based on solution change (tolerance 1e-12)
  - Particularly efficient for sparse matrices
  
- **Conjugate Gradient Method**
  - Krylov subspace iteration for symmetric positive definite systems
  - Faster convergence than Gauss-Seidel for many problems
  - Custom matrix-vector multiplication for sparse representations
  - Ideal for very large systems

### Performance Comparison
- Iterative vs. direct solver efficiency
- Convergence rate analysis
- Number of iterations to achieve tolerance
- Computational cost per iteration

## Key Python Libraries
- **NumPy**: Vector operations and array manipulation
- **Pandas**: Results organization and tabulation
- **Matplotlib**: Convergence behavior visualization
- **aeromod**: Custom module functions
  - `gaussSeidel()` - Gauss-Seidel with automatic relaxation
  - `conjGrad()` - Conjugate gradient solver

## Aerospace Applications

### Heat Transfer in Composite Structures
- Solving steady-state temperature distribution problems
- 2D heat conduction with boundary conditions
- Temperature field analysis in aircraft components
- Large sparse systems from finite difference discretization

### Finite Element Analysis
- Structural analysis of aerospace components
- Large-scale mesh equations (thousands to millions of unknowns)
- Memory-efficient sparse matrix operations

## Files
- `AEEM_2058_MaxDittman_HW3-2.ipynb` - Jupyter notebook with iterative solver implementations
- `Assignment 3.pdf` - Problem specifications
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Implement and apply iterative methods for large sparse systems
- Understand the advantages of iterative vs. direct methods
- Compute and optimize relaxation parameters for faster convergence
- Design custom matrix-vector multiplication for sparse representations
- Apply iterative methods to heat transfer and structural problems
- Analyze convergence behavior and stopping criteria
