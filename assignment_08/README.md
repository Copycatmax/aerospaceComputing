# Assignment 8: Interpolation & Heat Transfer

## Overview
This assignment combines 2D interpolation techniques with solving steady-state heat transfer problems, demonstrating how numerical methods integrate to solve complex aerospace engineering challenges.

## Topics Covered

### Interpolation Methods
- **2D Interpolation**
  - RectBivariateSpline for smooth surface fitting
  - Interpolating scattered data to regular grids
  - Generating continuous surfaces from discrete points
  
- **Sparse System Solutions**
  - Conjugate gradient method for large sparse matrices
  - Efficient memory usage for structured problems
  - Custom matrix-vector multiplication

### Heat Transfer Analysis
- **Steady-State Conduction**
  - Solving 2D Laplace equation (∇²T = 0)
  - Finite difference discretization
  - Boundary condition implementation
  
- **Temperature Field Visualization**
  - 2D contour plots of temperature distribution
  - Gradient analysis (heat flux directions)
  - Interpolation for smooth visualization

## Key Python Libraries
- **SciPy.interpolate**:
  - `RectBivariateSpline()` - Bivariate spline interpolation
- **NumPy**: Array operations and linear algebra
- **Matplotlib**: Temperature field visualization and contour plots
- **aeromod**:
  - `conjGrad()` - Conjugate gradient solver for sparse systems

## Aerospace Applications

### Thermal Analysis
- **Hypersonic Flow Regions**
  - Temperature distribution in high-speed flight
  - Heat transfer in aerodynamic heating zones
  - Leading edge and stagnation point analysis
  
- **Spacecraft Thermal Management**
  - Temperature control in orbital environments
  - Radiator and heat sink design
  - Thermal protection system analysis

### Structural Components
- Heat distribution in composite materials
- Thermal stress analysis
- Temperature-dependent material properties

## Problem Details
- Solving 9×9 temperature field systems
- Multiple boundary conditions (fixed temperatures)
- Visualizing results through interpolation

## Files
- `AEEM_2058_MaxDittman_HW8.ipynb` - Jupyter notebook with interpolation and heat transfer
- `Assignment 8.pdf` - Problem specifications
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Implement 2D interpolation for surface generation
- Solve steady-state heat conduction problems
- Apply conjugate gradient to sparse linear systems
- Visualize 2D temperature fields with contour plots
- Understand heat transfer in aerospace structures
- Connect numerical methods (linear solvers + interpolation)
- Analyze thermal behavior of aerospace components
