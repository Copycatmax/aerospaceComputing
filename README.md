# Aerospace Computing

This repository contains coursework for an undergraduate aerospace engineering computing course that develops numerical analysis and programming skills for aerospace problem-solving.

## Course Overview

This course further develops the computing skills of undergraduate aerospace engineering students that were initially taught in the ENED sequence courses and reintroduces them as tools for successful problem solving. The course introduces the basic principles of numerical analysis needed for all aspects of aerospace engineering problem solving. The techniques and skills developed are directly applicable to aerodynamics, dynamics and controls, propulsion, structures, and systems engineering. Students will reexamine the basic Python programming skills, develop stronger programming skills and strategies, and learn how to find available solutions to engineering problems developed by the Python community as they develop their personal computing technique module.

## Learning Objectives

Upon successful completion of this course, students will be able to:

1. Utilize Python to code numerical methods and plot results
2. Solve systems of linear equations using direct methods
3. Solve systems of linear equations by iterative methods
4. Interpolate data and develop curve fits; employ neural networks
5. Find the roots of equations and the zeros of polynomials and solve systems of nonlinear equations
6. Perform numerical differentiation
7. Perform numerical integration
8. Solve ODEs with Euler and Runge-Kutta methods
9. Utilize fast Fourier transforms (FFTs)
10. Compute eigenvalues
11. Utilize probability-based tools from existing Python modules

## Repository Architecture

### Core Module
- **`aeromod.py`** - Custom Python module containing numerical methods implementations including:
  - Linear system solvers (Gaussian elimination, LU decomposition, Cramer's rule)
  - Iterative solvers (Gauss-Seidel, conjugate gradient)
  - Root finding methods (bisection, Newton-Raphson)
  - Polynomial operations (evaluation, deflation, root finding)
  - Interpolation methods (Newton polynomials, rational interpolation, cubic splines)
  - Matrix operations (row/column swapping, decomposition utilities)

### Assignment Structure

The repository is organized into 10 assignment directories, each containing:
- Jupyter notebook(s) with code implementations and visualizations
- PDF assignment specification
- README.md with detailed description of methods and applications

#### Assignment Topics

- **`assignment_01/`** - Root Finding & Polynomial Analysis
  - Supersonic shock wave analysis (θ-β-M relations)
  - Bisection and Newton-Raphson methods
  - Polynomial root finding and deflation

- **`assignment_02/`** - Linear System Solvers
  - Direct methods: Cramer's rule, Gaussian elimination, LU decomposition
  - Computational efficiency comparison
  - Matrix inversion and residual error analysis

- **`assignment_03/`** - Iterative Methods for Linear Systems
  - Gauss-Seidel iteration with relaxation
  - Conjugate gradient method for sparse systems
  - Heat transfer applications in composite structures

- **`assignment_04/`** - Deep Neural Networks with PyTorch
  - Feed-forward network architecture design
  - Backpropagation and hyperparameter tuning
  - Function approximation and surrogate modeling

- **`assignment_05/`** - Numerical Integration
  - Gauss quadrature methods
  - Adaptive integration techniques
  - Multi-dimensional integration applications

- **`assignment_06/`** - Numerical Differentiation
  - Finite difference approximations (central, forward, backward)
  - Prandtl-Meyer expansion function analysis
  - Compressible flow applications

- **`assignment_07/`** - Integration Applications
  - Fixed-point vs adaptive quadrature
  - Double integration for areas and volumes
  - Aerodynamic surface integral calculations

- **`assignment_08/`** - Interpolation & Heat Transfer
  - 2D interpolation with RectBivariateSpline
  - Steady-state heat conduction problems
  - Temperature field visualization

- **`assignment_09/`** - Fast Fourier Transform & Signal Processing
  - FFT implementation and frequency domain analysis
  - Vibration and flutter detection
  - Acoustic signature analysis

- **`assignment_10/`** - Eigenvalue Problems
  - Eigenvalue and eigenvector computation
  - Structural dynamics and natural frequencies
  - Stability analysis for aerospace systems

## Key Technologies

- **Python 3** - Primary programming language
- **NumPy** - Numerical computing and linear algebra
- **SciPy** - Scientific computing (integration, interpolation, FFT)
- **Matplotlib** - Data visualization and plotting
- **SymPy** - Symbolic mathematics
- **PyTorch** - Deep learning framework
- **Pandas** - Data organization and analysis
- **Jupyter** - Interactive computing environment

## Applications to Aerospace Engineering

The numerical methods in this course are directly applicable to:
- **Aerodynamics**: Shock wave analysis, supersonic flow, pressure integration
- **Structures**: Heat transfer, stress analysis, natural frequencies, flutter
- **Dynamics & Controls**: Stability analysis, eigenvalue problems, system response
- **Propulsion**: Rocket performance, nozzle design, expansion waves
- **Systems Engineering**: Optimization, surrogate modeling, signal processing