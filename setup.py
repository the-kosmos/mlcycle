from setuptools import setup, find_packages

setup(
    name="your_package_name",
    version="0.1.0",
    author="Your Name",
    author_email="your@email.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy==2.3.3",
        "pandas==2.3.2",
        "requests==2.32.5",
        "PyYAML==6.0.2",
        "random_word==1.0.13",
    ],
    extras_require={
        "dev": [
            "pytest==8.4.2",
            "autopep8==2.3.2",
            "pycodestyle==2.14.0",
            "Pygments==2.19.2",
        ]
    },
)