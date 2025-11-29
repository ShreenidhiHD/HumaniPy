from setuptools import setup, find_packages

setup(
    name="HumaniPy",
    version="1.0.0",
    description="A package to simulate human-like behavior in automation tasks.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Shreenidhi HD",
    author_email="shreenidhihaagalagodu@gmail.com",
    url="https://github.com/ShreenidhiHD/HumaniPy/", 
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
        "pyautogui>=0.9.53",
        "undetected-chromedriver>=3.0.0",
        "fake-useragent>=0.1.11"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
