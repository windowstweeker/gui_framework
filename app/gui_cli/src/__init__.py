"""
Gui CLI
---------
Provides a simple cli gui to handle options/selections with color

"""

__version__ = "0.0.2"
__author__ = "Julian Feezell"
__license__ = "GNU GENERAL PUBLIC LICENSE Version 3"


from .main import HMI


__all__ = [HMI]


def main() -> None:
    print(f"{__doc__}"
          f"Package Management v{__version__}")
    return None


if __name__ == "__main__":
    main()
