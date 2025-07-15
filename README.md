# Kyber Key Exchange API

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A backend API implementing Post-Quantum Cryptography (PQC) key exchange using the Kyber algorithm. Built with FastAPI, this project provides secure session management and cryptographic operations.

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

## Quick Start

1. **Start the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the interactive API documentation**:
   - Open your browser and go to: http://127.0.0.1:8000/docs
   - This will show you all available endpoints with the ability to test them directly

3. **Example API Request**:
   ```bash
   # Generate a new key pair
   curl -X 'POST' \
     'http://127.0.0.1:8000/api/keys/generate' \
     -H 'accept: application/json' \
     -d ''
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

**Example Request**:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/generate-keypair' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

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

**Example Request**:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/exchange' \
  -H 'Content-Type: application/json' \
  -d '{
    "session_id": "your-session-id",
    "peer_public_key": "base64-encoded-peer-public-key"
  }'
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

**Example Request**:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/decapsulate' \
  -H 'Content-Type: application/json' \
  -d '{
    "session_id": "your-session-id",
    "ciphertext": "base64-encoded-ciphertext"
  }'
```

**Response**:
```json
{
  "shared_secret": "base64-encoded-shared-secret"
}
```

### `GET /health`
Check API health status.

**Example Request**:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/health' \
  -H 'accept: application/json'
```

**Response**:
```json
{
  "status": "healthy"
}
```

## Project Structure

```
kyber-key-exchange-api/
├── app/                          # Main application package
│   ├── __init__.py             # Package initialization
│   ├── main.py                 # FastAPI application and endpoints
│   ├── crypto_utils.py         # Cryptographic operations using OQS
│   └── session_store.py        # Session management with TTL support
├── .gitignore                  # Git ignore file
├── README.md                   # This file
├── requirements.txt            # Production dependencies
└── requirements-dev.txt        # Development dependencies
```

### Key Components

- **`app/main.py`**:
  - FastAPI application setup and configuration
  - API route definitions
  - Request/response models
  - Error handling middleware

- **`app/crypto_utils.py`**:
  - Implements Kyber key exchange using OQS
  - Handles key generation, encapsulation, and decapsulation
  - Provides fallback to simulated cryptography when OQS is not available
  - Includes comprehensive error handling and logging

- **`app/session_store.py`**:
  - Manages user sessions with TTL (Time To Live)
  - Thread-safe session operations
  - Automatic session cleanup

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