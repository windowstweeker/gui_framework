from setuptools import find_packages, setup

with open("app/README.md", "r") as file:
    long_description = file.read()

with open("requirements.txt", "r") as file:
    required_packages = file.read()
    install_requires = []
    for package in required_packages.split("\n"):
        if package:
            install_requires.append(package)

setup(
    name="GUI_FRAMEWORK",
    version="0.0.2",
    description="Simple cli GUI",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/windowstweeker/gui_framework",
    author="Julian Feezell",
    author_email="<Author>@email.com",
    license="GNU General Public License v3 (GPLv3)",
    classifiers=[ # https://pypi.org/classifiers/
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    extras_require={
        "dev": ["twine>=4.0.2", "unittest>=0.0.1"],
    },
    python_requires=">=3.12",
)
