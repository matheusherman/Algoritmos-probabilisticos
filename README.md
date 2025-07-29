# SPUTINIK — Gaussian Distribution Sample Generator

This repository contains a Python script that generates a sample from a normal (Gaussian) distribution using a custom algorithm called `SPUTINIK`, based on a rational approximation of the inverse cumulative distribution function (CDF) of the normal distribution.

The script also visualizes the generated data through a histogram overlaid with the theoretical Gaussian curve.

## 📁 File

- `main.py` — Contains the SPUTINIK algorithm, data sampling logic, and plotting code.

## 🚀 How It Works

- The `SPUTINIK(m, s)` function generates a random number from a normal distribution with mean `m` and standard deviation `s`, using a rational approximation of the inverse normal CDF.
- The script:
  1. Generates 500 random values from a standard normal distribution.
  2. Calculates the Gaussian probability density function (PDF) over the sample range.
  3. Plots the histogram of the generated data and the Gaussian curve for visual comparison.

## 📦 Dependencies

Install the required libraries:

```
pip install numpy matplotlib
```

▶️ How to Run

Clone the repository and run the script:

```
python main.py
```

A graph will be displayed with the histogram and the Gaussian function.
📊 Expected Output

The output consists of:

    A histogram of the generated data (in green)

    A curve of the theoretical Gaussian function (in black)

This allows a visual comparison of the sample quality.
🧠 Notes

    The SPUTINIK function is inspired by algorithms such as Beasley-Springer-Moro for approximating the inverse of the standard normal distribution.

    It can be useful in simulations, data visualization, and teaching statistics or probability concepts.

Author: Matheus Herman
License: MIT
