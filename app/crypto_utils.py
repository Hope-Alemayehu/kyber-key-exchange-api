import base64
from typing import Tuple
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Kyber-512 is the smallest and fastest variant
KEM_ALG = "Kyber512"


def ensure_oqs_available():
    """Ensure oqs module is available with required algorithms"""
    try:
        import oqs

        # Test if the required algorithm is available
        with oqs.KeyEncapsulation(KEM_ALG):
            pass
        logger.info("OQS initialized successfully with Kyber512")
        return True
    except Exception as e:
        logger.warning(f"Error initializing OQS: {e}")
        logger.warning("\nTo install the required dependencies on Windows:")
        logger.warning("1. Install Visual Studio Build Tools with C++ workload")
        logger.warning("2. Make sure Python development headers are installed")
        logger.warning("3. Run: pip install oqs-python")
        return False


# Check if oqs is available at module load time
OQS_AVAILABLE = ensure_oqs_available()

if not OQS_AVAILABLE:
    logger.warning(
        "OQS not available. Using simulated cryptography (NOT SECURE FOR PRODUCTION)"
    )
    logger.warning(
        "To enable real post-quantum cryptography, please install the required dependencies."
    )


def generate_keys() -> Tuple[str, str]:
    """
    Generate a new Kyber key pair

    Returns:
        tuple: (public_key_b64, private_key_b64) - Base64 encoded keys
    """
    try:
        if not OQS_AVAILABLE:
            # Fallback to simulated cryptography
            public_key = os.urandom(800)  # Simulated public key
            private_key = os.urandom(1632)  # Simulated private key
        else:
            import oqs

            logger.debug("Generating keypair...")
            with oqs.KeyEncapsulation(KEM_ALG) as kem:
                public_key = kem.generate_keypair()
                private_key = kem.export_secret_key()
                logger.debug(f"Public key length: {len(public_key)} bytes")
                logger.debug(f"Private key length: {len(private_key)} bytes")

        # Convert to base64 for easier handling in the API
        public_key_b64 = base64.b64encode(public_key).decode()
        private_key_b64 = base64.b64encode(private_key).decode()

        return public_key_b64, private_key_b64
    except Exception as e:
        logger.error(f"Key generation failed: {str(e)}")
        raise Exception(f"Key generation failed: {str(e)}")


def encapsulate_key(peer_public_key_b64: str) -> Tuple[str, str]:
    """
    Generate a shared secret and encapsulate it using the peer's public key

    Args:
        peer_public_key_b64 (str): Base64 encoded public key from peer

    Returns:
        tuple: (ciphertext_b64, shared_secret_b64) - Base64 encoded ciphertext and shared secret
    """
    try:
        # Decode the base64 public key
        peer_public_key = base64.b64decode(peer_public_key_b64)

        if not OQS_AVAILABLE:
            # Fallback to simulated cryptography
            ciphertext = os.urandom(768)  # Simulated ciphertext
            shared_secret = os.urandom(32)  # Simulated shared secret
        else:
            import oqs

            logger.debug("Encapsulating key...")
            with oqs.KeyEncapsulation(KEM_ALG) as kem:
                ciphertext, shared_secret = kem.encap_secret(peer_public_key)
                logger.debug(f"Ciphertext length: {len(ciphertext)} bytes")
                logger.debug(f"Shared secret length: {len(shared_secret)} bytes")

        # Convert to base64 for the API response
        ciphertext_b64 = base64.b64encode(ciphertext).decode()
        shared_secret_b64 = base64.b64encode(shared_secret).decode()

        return ciphertext_b64, shared_secret_b64
    except Exception as e:
        logger.error(f"Key encapsulation failed: {str(e)}")
        raise Exception(f"Key encapsulation failed: {str(e)}")


def decapsulate_key(private_key_b64: str, ciphertext_b64: str) -> str:
    """
    Decapsulate a shared secret using the private key

    Args:
        private_key_b64 (str): Base64 encoded private key
        ciphertext_b64 (str): Base64 encoded ciphertext

    Returns:
        str: Base64 encoded shared secret
    """
    try:
        # Decode the base64 inputs
        private_key = base64.b64decode(private_key_b64)
        ciphertext = base64.b64decode(ciphertext_b64)

        if not OQS_AVAILABLE:
            # Fallback to simulated cryptography
            return base64.b64encode(os.urandom(32)).decode()  # Simulated shared secret
        else:
            import oqs

            logger.debug("Decapsulating key...")
            with oqs.KeyEncapsulation(KEM_ALG, private_key) as kem:
                shared_secret = kem.decap_secret(ciphertext)
                logger.debug(
                    f"Decapsulated shared secret length: {len(shared_secret)} bytes"
                )
                return base64.b64encode(shared_secret).decode()
    except Exception as e:
        logger.error(f"Key decapsulation failed: {str(e)}")
        raise Exception(f"Key decapsulation failed: {str(e)}")
