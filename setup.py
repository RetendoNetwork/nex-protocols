from setuptools import setup, find_packages

setup(
    name="nex_protocols",
    version="1.0.0",
    author="Retendo Contributors",
    author_email="tonemail@example.com",
    description="NEX Protocols for Wii U & 3DS Consoles.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RetendoNetwork/nex_protocols",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "anynet ~= 1.1",
		    "pycryptodome"
    ],
)
