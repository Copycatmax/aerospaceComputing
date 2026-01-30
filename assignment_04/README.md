# Assignment 4: Deep Neural Networks with PyTorch

## Overview
This assignment introduces machine learning and deep neural networks for function approximation and surrogate modeling, essential skills for modern aerospace engineering applications.

## Topics Covered

### Neural Network Fundamentals
- **Feed-Forward Network Architecture**
  - Input layer → Hidden layers → Output layer
  - Network topology design and selection
  - Activation functions
  
- **Training and Optimization**
  - Backpropagation algorithm
  - Gradient descent optimization
  - Learning rate selection and tuning
  - Momentum for faster convergence
  
- **Hyperparameter Tuning**
  - Network architecture experimentation: [1, 22, 12, 12, 1] to [1, 88, 1]
  - Training/validation split ratios (70%/30% vs 90%/10%)
  - Number of training epochs
  - Learning rate optimization
  - Overfitting analysis and prevention

### Model Validation
- Training vs. validation error tracking
- Continued training for improved convergence
- Performance metrics and loss functions

## Key Python Libraries
- **PyTorch**: Deep learning framework (via custom Assignment class)
- **NumPy**: Data preprocessing and array operations
- **Matplotlib**: Training progress and loss visualization
- **Scikit-learn concepts**: Model validation and metrics

## Aerospace Applications

### Surrogate Modeling
- Replacing expensive computational fluid dynamics (CFD) simulations
- Real-time aerodynamic coefficient prediction
- Fast optimization with neural network surrogates

### Flight Dynamics
- Learning complex relationships in flight test data
- Predicting aircraft response to control inputs
- System identification from experimental data

### Design Optimization
- Approximating objective functions in multi-dimensional design spaces
- Rapid design space exploration
- Trade study automation

## Files
- `AEEM_2058_MaxDittman_HW4.ipynb` - Main assignment notebook with PyTorch implementations
- `dnn_assignment.ipynb` - Additional deep neural network exercises
- `Assignment 4.pdf` - Problem specifications
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Design and implement feed-forward neural networks
- Train networks using backpropagation and gradient descent
- Tune hyperparameters for optimal performance
- Recognize and mitigate overfitting
- Apply neural networks to function approximation problems
- Understand when neural networks are appropriate for aerospace applications
- Evaluate model performance on validation data
