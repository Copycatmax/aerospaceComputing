# Assignment 9: Fast Fourier Transform & Signal Processing

## Overview
This assignment introduces frequency domain analysis using Fast Fourier Transforms (FFT), an essential tool for vibration analysis, flutter detection, and structural health monitoring in aerospace systems.

## Topics Covered

### Signal Processing Fundamentals
- **Fast Fourier Transform (FFT)**
  - Converting time-domain signals to frequency domain
  - Efficient O(n log n) algorithm
  - Discrete Fourier Transform implementation
  
- **Frequency Domain Analysis**
  - Computing frequency spectra
  - Identifying dominant frequencies in signals
  - Amplitude vs. frequency visualization
  
- **Signal Decomposition**
  - Breaking down composite signals into components
  - Sinusoidal function analysis: f(x) = 4sin(3πx/9) - 4sin(2πx/7)
  - Extracting individual frequency contributions

### FFT Applications
- Frequency spectrum computation
- Peak frequency identification
- Signal filtering concepts
- Spectral analysis of periodic phenomena

## Key Python Libraries
- **NumPy.fft**:
  - `fft()` - Fast Fourier Transform computation
  - `fftfreq()` - Frequency bin calculation
- **NumPy**: Signal generation and array operations
- **Matplotlib**: Frequency spectrum visualization
- **CSV**: Data input/output

## Aerospace Applications

### Vibration Analysis
- **Wing Flutter Detection**
  - Identifying dangerous oscillation frequencies
  - Monitoring structural vibrations in flight
  - Preventing catastrophic structural failures
  
- **Engine Monitoring**
  - Detecting abnormal vibration frequencies
  - Predictive maintenance through frequency anomaly detection
  - Bearing and rotor imbalance identification

### Structural Health Monitoring
- Analyzing dynamic response of aircraft structures
- Detecting damage through frequency shifts
- Modal analysis for natural frequency determination

### Acoustic Analysis
- Engine noise signature characterization
- Acoustic fatigue assessment
- Sound source identification

## Files
- `AEEM_2058_MaxDittman_HW9.ipynb` - Jupyter notebook with FFT implementations
- `Assignment 9.pdf` - Problem specifications
- `README.md` - This file

## Learning Outcomes
Students will be able to:
- Implement Fast Fourier Transform for signal analysis
- Transform signals between time and frequency domains
- Identify dominant frequencies in composite signals
- Visualize and interpret frequency spectra
- Apply FFT to vibration and flutter analysis problems
- Understand the importance of frequency analysis in aerospace
- Recognize frequency anomalies indicating structural issues
