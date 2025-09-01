import matplotlib.pyplot as plt
import numpy as np

# Custom fonts
plt.rcParams['font.family'] = 'KaTeX_Main'
plt.rcParams['mathtext.fontset'] = 'cm'



def main():
    print(collatz_sequence(10))



def collatz_sequence(n: int) -> list[int]:
    if n <=0 or not isinstance(n, int):
        print(f"Invalid number: n = {n}\n**Number must be positive integer.**")
        return []

    result = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        result.append(n)
    return result











if __name__ == "__main__":
    main()