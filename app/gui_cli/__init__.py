"""
MyPackage
---------
A brief description of what this package does.

"""

__version__ = "0.0.2"
__author__ = "<Author>"
__license__ = "GNU GENERAL PUBLIC LICENSE Version 3"


from .src import HMI


__all__ = [HMI]


def main() -> None:
    print(f"{__doc__}Package Management v{__version__}")
    return None


if __name__ == "__main__":
    main()
