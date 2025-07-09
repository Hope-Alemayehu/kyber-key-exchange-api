# Kyber Key Exchange API

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready backend API implementing Post-Quantum Cryptography (PQC) key exchange using the Kyber algorithm. Built with FastAPI, this project provides secure session management and cryptographic operations.

## Features

- Quantum-resistant key exchange using Kyber algorithm
- Session-based key management
- Fallback to simulated cryptography when OQS is not available
- Comprehensive error handling and logging
- Interactive API documentation with Swagger UI

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Windows/Linux/macOS

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kyber-key-exchange-api.git
   cd kyber-key-exchange-api
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Unix or MacOS:
   # source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Optional: Enable Real PQC (Recommended for Production)

For real post-quantum cryptography, install the Open Quantum Safe library:

1. **Windows**:
   - Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with C++ workload
   - Install [CMake](https://cmake.org/download/)
   - Add CMake to your system PATH

2. **Install OQS Python bindings**:
   ```bash
   pip install git+https://github.com/open-quantum-safe/liboqs-python.git
   ```

## Running the API

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:
- Interactive documentation: http://127.0.0.1:8000/docs
- Alternative documentation: http://127.0.0.1:8000/redoc

## API Endpoints

### `POST /generate-keypair`
Generate a new keypair and session.

**Response**:
```json
{
  "session_id": "unique-session-id",
  "public_key": "base64-encoded-public-key",
  "private_key": "base64-encoded-private-key"
}
```

### `POST /exchange`
Perform key exchange using session data.

**Request Body**:
```json
{
  "session_id": "your-session-id",
  "peer_public_key": "base64-encoded-peer-public-key"
}
```

**Response**:
```json
{
  "ciphertext": "base64-encoded-ciphertext",
  "shared_secret": "base64-encoded-shared-secret"
}
```

### `POST /decapsulate`
Decapsulate a shared secret using a private key.

**Request Body**:
```json
{
  "session_id": "your-session-id",
  "ciphertext": "base64-encoded-ciphertext"
}
```

**Response**:
```json
{
  "shared_secret": "base64-encoded-shared-secret"
}
```

### `GET /health`
Check API health status.

**Response**:
```json
{
  "status": "healthy"
}
```

## Project Structure

```
kyber-key-exchange-api/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI application and endpoints
│   ├── crypto_utils.py     # Cryptographic operations with OQS fallback
│   └── session_store.py    # In-memory session management
├── tests/                  # Test files
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
└── README.md               # This file
```

## Development

### Running Tests
```bash
pip install -r requirements-dev.txt
pytest
```

### Code Style
This project uses:
- Black for code formatting
- Flake8 for linting
- isort for import sorting

Run code style checks:
```bash
black .
flake8
isort .
```

## Deployment

For production deployment, consider using:
- Gunicorn with Uvicorn workers
- Environment variables for configuration
- Proper logging and monitoring
- HTTPS with valid certificates

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Open Quantum Safe](https://openquantumsafe.org/)
- [Kyber Algorithm](https://pq-crystals.org/kyber/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)