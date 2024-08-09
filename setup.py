from setuptools import setup, find_packages

setup(
    name="winzy-hello-world",
    description="Example winzy plugin",
    version="0.0.1",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires="winzy",
    entry_points={
        "winzy.plugins": ["hello = winzyhello.winzy_hello_world:hello_plugin"]
        },
    python_requires=">=3.9",
    author="Sukhbinder Singh",
    url="https://github.com/sukhbinder/xxxxxxx",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Database",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],

)

