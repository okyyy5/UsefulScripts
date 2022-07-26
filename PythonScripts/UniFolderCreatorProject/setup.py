import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="UniFolderCreator",
    version="0.0.1",
    author="Oktay Turdu & Brook Jeynes",
    author_email="",
    description=("A tool to create a folder structure for a university"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "UniFOlderCreator": "https://github.com/okyyy5/UsefulScripts",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "udirc = UniFolderCreator.cli:app",
        ]
    }
)