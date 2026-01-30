# Assignment 1: Root Finding & Polynomial Analysis

## Overview
This assignment focuses on numerical methods for finding roots of equations and zeros of polynomials, with applications to supersonic aerodynamics and propulsion systems.

## Topics Covered

### Numerical Methods
- **Root Finding Algorithms**
  - Bisection method for bracketed roots
  - Newton-Raphson method with derivative information
  - Root search techniques for initial bracketing
  
- **Polynomial Operations**
  - Finding roots of polynomial equations
  - Polynomial deflation after root extraction
  - Complex root handling

### Aerospace Applications
- **Supersonic Shock Wave Analysis**
  - Solving θ-β-M (deflection-shock angle-Mach) relations for oblique shocks
  - Implicit nonlinear equation solving for shock-expansion theory
  - Critical for supersonic aircraft design and analysis
  
- **Rocket Propulsion**
  - Calculating rocket velocity as a function of fuel burn rate
  - Nonlinear dynamics of propulsion systems

## Key Python Libraries
- **NumPy**: Array operations and mathematical functions
- **Matplotlib**: Visualization of results and convergence behavior
- **aeromod**: Custom module functions
  - `bisection()` - Bisection root finding
  - `newtonRaphson()` - Newton-Raphson method
  - `rootsearch()` - Initial bracket search
  - `polyRoots()` - Polynomial root finder using Laguerre's method
  - `deflPoly()` - Polynomial deflation

## Files
- `AEEM_2058_MaxDittman_HW1.ipynb` - Jupyter notebook with implementations and visualizations
- `Assignment 1.pdf` - Problem specifications and requirements
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Implement and apply root finding methods to aerospace engineering problems
- Solve implicit nonlinear equations arising in supersonic flow analysis
- Find and verify polynomial roots using multiple methods
- Understand the importance of proper bracketing for convergence
