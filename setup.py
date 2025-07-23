#!/usr/bin/env python3
"""
Setup script for Bible Gateway Downloader - True Async Edition
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#"):
                    requirements.append(line)
    return requirements

setup(
    name="bygod",
    version="2.0.0",
    author="Bible Gateway Downloader Team",
    author_email="your-email@example.com",
    description="A comprehensive, truly asynchronous tool for downloading Bible translations from BibleGateway.com",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/bible-gateway-downloads",
    py_modules=["bible_downloader"],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Religion",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=[
        "aiohttp>=3.8.0",
        "beautifulsoup4>=4.11.0",
        "colorlog>=6.7.0",
        "pyyaml>=6.0",
        "lxml>=4.9.0",
    ],
    extras_require={
        "dev": [
            "black>=22.0.0",
            "isort>=5.10.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bygod=bible_downloader:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "bible",
        "download",
        "biblegateway",
        "async",
        "scripture",
        "religion",
        "json",
        "csv",
        "xml",
        "yaml",
    ],
    project_urls={
        "Bug Reports": "https://github.com/your-username/bible-gateway-downloads/issues",
        "Source": "https://github.com/your-username/bible-gateway-downloads",
        "Documentation": "https://github.com/your-username/bible-gateway-downloads#readme",
    },
)
