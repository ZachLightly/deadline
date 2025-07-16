import sys


def print_python_executable():
    print(f"Python executable location: {sys.executable}")


def main():
    print("Hello from backend!")
    print_python_executable()


if __name__ == "__main__":
    main()
