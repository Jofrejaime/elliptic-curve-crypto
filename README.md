# Elliptic Curve Cryptography Project

This project implements elliptic curve cryptography (ECC) using both manual methods and libraries such as `sympy` and `ecdsa`. It includes key generation, signing, and verification processes, along with utility functions for mathematical operations.

## Project Structure

```
elliptic-curve-crypto
├── src
│   ├── manual
│   │   ├── elliptic_curve.py       # Manual implementation of elliptic curves
│   │   └── keygen.py               # Key generation for ECC
│   ├── sympy_impl
│   │   └── sympy_elliptic_curve.py # ECC operations using sympy
│   ├── ecdsa_impl
│   │   └── ecdsa_example.py        # ECDSA signing and verification
│   ├── utils
│   │   └── math_utils.py           # Utility functions for math operations
│   └── __init__.py                 # Marks src as a package
├── tests
│   ├── test_manual.py              # Unit tests for manual implementation
│   ├── test_sympy_impl.py          # Unit tests for sympy implementation
│   └── test_ecdsa_impl.py          # Unit tests for ECDSA implementation
├── requirements.txt                 # Required Python packages
├── .gitignore                       # Files to ignore in version control
└── README.md                        # Project documentation
```

## Installation

To set up the project, clone the repository and install the required packages:

```bash
git clone <repository-url>
cd elliptic-curve-crypto
pip install -r requirements.txt
```

## Usage

### Manual Implementation

You can use the manual implementation of elliptic curves by importing the `EllipticCurve` class from `src/manual/elliptic_curve.py`. The `KeyGenerator` class in `keygen.py` can be used to generate keys.

### Sympy Implementation

For operations using the `sympy` library, import the `SympyEllipticCurve` class from `src/sympy_impl/sympy_elliptic_curve.py`.

### ECDSA Implementation

The `ECDSAExample` class in `src/ecdsa_impl/ecdsa_example.py` demonstrates how to generate keys, sign messages, and verify signatures using the `ecdsa` library.

## Features

- **Point Addition and Doubling**: Implemented for elliptic curves.
- **Scalar Multiplication**: Efficiently computed using the double-and-add algorithm.
- **Key Generation**: Securely generates private and public keys.
- **ECDSA**: Implements signing and verification of messages.
- **Utility Functions**: Provides essential mathematical operations.

## Testing

Unit tests are provided for each implementation. You can run the tests using:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.