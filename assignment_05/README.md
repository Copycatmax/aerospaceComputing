# Assignment 5: Numerical Integration

## Overview
This assignment covers numerical integration techniques for computing definite integrals, essential for aerodynamic force calculations, moments, and geometric properties in aerospace engineering.

## Topics Covered

### Numerical Integration Methods
- **Gauss Quadrature**
  - Fixed-point quadrature rules
  - Varying number of integration nodes (2, 4, 8, etc.)
  - Optimal node placement for polynomial accuracy
  
- **Adaptive Integration**
  - Automatic error control with scipy.integrate.quad
  - Adaptive subdivision for complex integrands
  - Comparison with fixed-point methods
  
- **Multi-Dimensional Integration**
  - Double integrals using dblquad
  - Integration over 2D regions
  - Area and volume calculations

### Accuracy Analysis
- Comparing quadrature node counts
- Error analysis vs. analytical solutions
- Convergence behavior with increasing nodes

## Key Python Libraries
- **SciPy.integrate**: 
  - `quad()` - Adaptive integration
  - `fixed_quad()` - Gaussian quadrature with specified nodes
  - `dblquad()` - Double integration
- **NumPy**: Mathematical functions and array operations
- **Matplotlib**: Result visualization
- **aeromod**: Integration utilities

## Aerospace Applications

### Aerodynamic Force Calculations
- Integrating pressure distributions over wing surfaces
- Computing lift, drag, and moment coefficients
- Surface integral calculations for complex geometries

### Geometric Properties
- Center of gravity calculations
- Moments of inertia for structural components
- Volume and surface area computations

### Propulsion Systems
- Fuel volume calculations
- Thrust integration over nozzle exit plane
- Mass flow rate computations

## Files
- `AEEM_2058_MaxDittman_HW5-1.ipynb` - Jupyter notebook with integration implementations
- `Assignment 5.pdf` - Problem specifications
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Apply Gaussian quadrature to compute definite integrals
- Select appropriate quadrature order for desired accuracy
- Use adaptive integration for complex integrands
- Compute multi-dimensional integrals
- Understand trade-offs between fixed and adaptive methods
- Apply numerical integration to aerospace engineering calculations
- Verify integration accuracy through error analysis
