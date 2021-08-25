from src.app import *

def main():
    nums: list = generate_numbers(10)
    sum: int = add(nums)
    print(f"La suma es: {sum}")

if __name__ == '__main__':
    main()