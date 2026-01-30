# Assignment 6: Numerical Differentiation & Compressible Flow

## Overview
This assignment explores numerical differentiation techniques and their application to compressible flow analysis, particularly the Prandtl-Meyer expansion function critical for supersonic nozzle design.

## Topics Covered

### Numerical Differentiation Methods
- **Finite Difference Approximations**
  - Central difference (2nd order accuracy)
  - Forward difference (1st and 2nd order)
  - Backward difference
  - Step size selection and error analysis
  
- **Derivative Computation**
  - First derivatives (slopes, rates of change)
  - Second derivatives (curvature, acceleration)
  - Multiple evaluation points (M = 1 to 5)

- **Symbolic Differentiation**
  - Exact derivatives using SymPy
  - Comparison with finite difference approximations
  - Converting symbolic expressions to numerical functions

### Error Analysis
- Accuracy vs. step size (h)
- Truncation error in finite differences
- Round-off error considerations
- Optimal step size selection

## Key Python Libraries
- **NumPy**: Numerical computations
- **SymPy**: Symbolic mathematics
  - `diff()` - Symbolic differentiation
  - `lambdify()` - Convert symbolic to numerical functions
- **Matplotlib**: Visualization of derivatives and errors
- **aeromod**: Numerical method utilities

## Aerospace Applications

### Prandtl-Meyer Expansion Waves
- **Supersonic Flow Analysis**
  - Calculating expansion characteristics in supersonic nozzles
  - Mach number dependence of flow properties
  - Critical for supersonic aircraft and rocket nozzle design
  
- **Flow Property Variations**
  - Computing dν/dM (expansion function derivative)
  - Understanding how flow properties change with Mach number
  - Supersonic jet expansion characteristics

### General Applications
- Rate of change calculations in aerodynamic data
- Sensitivity analysis in design parameters
- Gradient-based optimization
- Trajectory analysis (velocity → acceleration)

## Files
- `AEEM_2058_MaxDittman_HW6.ipynb` - Jupyter notebook with differentiation methods
- `Assignment 6.pdf` - Problem specifications
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Implement finite difference approximations for derivatives
- Understand accuracy and order of different approximation schemes
- Apply numerical differentiation to compressible flow problems
- Analyze the Prandtl-Meyer expansion function
- Compare numerical and symbolic differentiation methods
- Select appropriate step sizes for accurate derivative computation
- Apply differentiation to supersonic aerodynamics problems
