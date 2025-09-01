import matplotlib.pyplot as plt
import numpy as np

# Fonts
plt.rcParams['font.family'] = 'KaTeX_Main'
plt.rcParams['mathtext.fontset'] = 'cm'

title_fontsize = 20
label_fontsize = 14
ticks_fontsize = 12



def main():
    plot_sequence([27])



def collatz_sequence(n: int) -> list[int]:
    if n <=0 or not isinstance(n, int):
        print(f"Invalid number. Must be positive integer.")
        return []

    result = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        result.append(n)
    return result



def plot_sequence(numbers: list[int]) -> None:
    if any(n <= 0 or not isinstance(n, int) for n in numbers):
        print("Invalid input list. Must contain positive integers.")
        return

    for num in numbers:
        y = collatz_sequence(num)
        x = [i for i in range(len(y))]
        plt.plot(x, y, marker="", linestyle="-")

    if len(numbers) == 1:
        plt.title(f"Collatz Sequence starting at {numbers[0]}", fontsize=title_fontsize)
        plt.xlabel(f"Number of steps = {len(y)-1}", fontsize=label_fontsize)
        plt.ylabel(f"Values", fontsize=label_fontsize)
    else:
        plt.title(f"Collatz Sequence", fontsize=title_fontsize)
        plt.xlabel(f"Number of steps", fontsize=label_fontsize)
        plt.ylabel(f"Values", fontsize=label_fontsize)

    plt.tick_params(axis="both", labelsize=ticks_fontsize)
    plt.grid(False)
    plt.show()












if __name__ == "__main__":
    main()