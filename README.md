# Kyber Key Exchange API Demo

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A demonstration backend API implementing a Post-Quantum Cryptography (PQC) key exchange service inspired by the NIST finalist CRYSTALS-Kyber algorithm. Built with FastAPI, this project showcases secure session management and cryptographic operations in a production-ready API service.

## Overview

This API demonstrates a secure key exchange mechanism that could be used in quantum-resistant cryptographic systems. The service provides:

- Generation of public-private keypairs per session
- Secure key exchange simulation
- Health status monitoring
- Session-based security model

## Important Note: Simulated Cryptography

**This is a simulation** of quantum-resistant cryptographic operations. The implementation uses secure random byte generation to demonstrate the API flow without actual lattice-based PQC algorithms.

### Key Simulation Details:
- Key generation and encapsulation are simulated using cryptographically secure random bytes
- The architecture is designed for easy integration with real PQC libraries
- Code structure follows best practices for production deployment

## Project Structure

```
kyber-key-exchange-api/
├── app/
│   ├── main.py             # FastAPI application and endpoints
│   ├── crypto_utils.py     # Simulated cryptographic operations
│   └── session_store.py    # In-memory session management
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kyber-key-exchange-api.git
   cd kyber-key-exchange-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

Start the development server:
```bash
uvicorn app.main:app --reload
```

Access the interactive API documentation at:
```
http://127.0.0.1:8000/docs
```

## API Endpoints

- `POST /generate-keypair`: Generate a new keypair and session
- `POST /exchange`: Perform key exchange using session data
- `GET /health`: Check API health status

## Future Enhancements

- [ ] Integrate with Open Quantum Safe (liboqs) for real PQC operations
- [ ] Add persistent session storage
- [ ] Implement authentication and rate limiting
- [ ] Dockerize the application
- [ ] Set up CI/CD pipeline
- [ ] Add comprehensive test suite

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [CRYSTALS-Kyber](https://pq-crystals.org/kyber/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Acknowledgments

- NIST for standardizing post-quantum cryptographic algorithms
- The Open Quantum Safe project for their work on PQC implementations
- The FastAPI community for an amazing web framework