from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kyber-key-exchange-api",
    version="0.1.0",
    author="Hope Alemayehu",
    author_email="hopesp444@gmail.com",
    description="A production-ready API for Kyber post-quantum key exchange",
    long_description="backend API implementing Post-Quantum Cryptography (PQC) key exchange using the Kyber algorithm",
    long_description_content_type="text/markdown",
    url="https://github.com/Hope-Alemayehu/kyber-key-exchange-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "oqs>=0.10.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "requests>=2.28.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
            "mkdocs>=1.4.0",
            "mkdocs-material>=9.0.0",
        ],
    },
)
