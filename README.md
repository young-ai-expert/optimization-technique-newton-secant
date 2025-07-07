

# Secant and Newton Methods in Python

This project implements two numerical optimization/root-finding techniques — **Newton's Method** and the **Secant Method** — using Python and `sympy`.

## 📌 Overview

- **Newton's Method** uses derivatives to iteratively find critical points (minima/maxima) or roots of a function.
- **Secant Method** approximates derivatives using two initial guesses and doesn't require symbolic differentiation.

## 🚀 Features

- Symbolic differentiation with `sympy` (for Newton's method).
- User input for function, initial guesses, and error tolerance.
- Iterative convergence with stopping criteria.


## 📂 Files

- `newton_method.py` – Implements Newton's method for optimization or root-finding.
- `secant_method.py` – Implements the Secant method for root-finding.


## ✅ How to Run

Make sure you have Python and `sympy` installed.

```bash
pip install sympy
python newton_method.py
python secant_method.py
