# SparseRegression

[![PyPI version](https://badge.fury.io/py/sparseregression.svg)](https://badge.fury.io/py/sparseregression)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE.md)
[![Downloads](https://pepy.tech/badge/sparseregression)](https://pepy.tech/project/sparseregression)

A Python package for sparse linear regression using mixed-integer optimization. Given a feature matrix and a sparsity budget `k`, it finds the best subset of at most `k` features that minimises the sum of squared residuals.

## Installation

```bash
pip install sparseregression
```

> **Note:** The solver [IPOPT](https://coin-or.github.io/Ipopt/) must be installed separately and its executable path passed at runtime.

## Quick Start

```python
import sklearn.datasets as sd
import sparseregression.linear as sl

# Load example data
data = sd.load_boston()
X, y = data.data, data.target

# Fit sparse regression with at most 10 non-zero coefficients
results, coefficients = sl.sparse_linear_regression(
    X, y, k=10, executable="~/Ipopt/ipopt"
)

print(coefficients)
```

## API Reference

#### `sparseregression.linear.sparse_linear_regression`

```python
sparse_linear_regression(X, y, k, engine='ipopt', executable='~', verbose=False)
```

Solves the sparse linear regression problem via mixed-integer programming:

$$\min_{\beta,\, z} \sum_i \left(y_i - X_i \cdot \beta\right)^2 \quad \text{s.t.} \quad \sum_j z_j \leq k,\; -Mz_j \leq \beta_j \leq Mz_j,\; z_j \in \{0,1\}$$

| Parameter    | Type      | Description                                              |
|--------------|-----------|----------------------------------------------------------|
| `X`          | `ndarray` | Feature matrix of shape `(n, p)`                        |
| `y`          | `ndarray` | Target vector of length `n`                             |
| `k`          | `int`     | Maximum number of non-zero coefficients                 |
| `engine`     | `str`     | Optimisation solver name (default: `'ipopt'`)           |
| `executable` | `str`     | Path to solver executable (default: `'~'`)              |
| `verbose`    | `bool`    | Print solver output (default: `False`)                  |

**Returns:** `(results, coefficients)` — solver result object and a list of regression coefficients.

## License

Distributed under the [MIT License](./LICENSE.md).
