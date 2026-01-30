# Assignment 7: Numerical Integration Applications

## Overview
This assignment extends numerical integration techniques with focus on comparing fixed-point and adaptive quadrature methods, and applying double integration to compute areas and volumes.

## Topics Covered

### Integration Techniques
- **Fixed Quadrature Methods**
  - 2-node Gaussian quadrature
  - 4-node Gaussian quadrature
  - Predetermined integration points and weights
  - Efficiency for smooth integrands
  
- **Adaptive Quadrature**
  - Automatic error estimation and control
  - Dynamic subdivision of integration interval
  - Best for integrands with varying smoothness
  
- **Double Integration**
  - Computing integrals over 2D regions
  - Nested integration for area calculations
  - Volume computations under surfaces

### Method Comparison
- Accuracy vs. number of nodes
- Computational efficiency analysis
- When to use fixed vs. adaptive methods
- Error tolerance achievement

## Key Python Libraries
- **SciPy.integrate**:
  - `fixed_quad()` - Fixed Gaussian quadrature
  - `quad()` - Adaptive integration with automatic error control
  - `dblquad()` - Double integration for 2D problems
- **NumPy**: Mathematical operations
- **Matplotlib**: Results visualization and comparison plots

## Aerospace Applications

### Aerodynamic Surface Integrals
- Computing forces from pressure distributions
- Integrating shear stress over surfaces
- Calculating total lift and drag from local loads

### Structural Analysis
- Stress distribution integration
- Computing resultant forces and moments
- Cross-sectional property calculations

### Volume Calculations
- Fuel tank volume computations
- Payload bay capacity analysis
- Geometric property determination

## Files
- `AEEM_2058_MaxDittman_HW7.ipynb` - Jupyter notebook with integration applications
- `Assignment 7.pdf` - Problem specifications
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Compare fixed and adaptive integration methods
- Select appropriate quadrature rules for different problems
- Implement double integration for 2D regions
- Analyze accuracy vs. computational cost trade-offs
- Apply integration methods to practical aerospace calculations
- Understand when adaptive methods are necessary
- Compute areas, volumes, and other integral quantities
