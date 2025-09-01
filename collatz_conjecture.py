import matplotlib.pyplot as plt
import numpy as np

# Fonts
plt.rcParams['font.family'] = 'KaTeX_Main'
plt.rcParams['mathtext.fontset'] = 'cm'

title_fontsize = 20
label_fontsize = 14
ticks_fontsize = 12



def main():
    plot_sequence([17])



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

    line_color = "red" if len(numbers) == 1 else None
    fig, ax = plt.subplots()

    for num in numbers:
        y = collatz_sequence(num)
        x = [i for i in range(len(y))]
        ax.plot(x, y, marker="", linestyle="-", color=line_color)

    if len(numbers) == 1:
        ax.set_title(f"Collatz Sequence starting at {numbers[0]}", fontsize=title_fontsize)
        ax.set_xlabel(f"Iterations = {len(y)-1}", fontsize=label_fontsize)
        ax.set_ylabel(f"Values  (max = {max(y)})", fontsize=label_fontsize)
    else:
        ax.set_title(f"Collatz Sequence", fontsize=title_fontsize)
        ax.set_xlabel(f"Iterations", fontsize=label_fontsize)
        ax.set_ylabel(f"Values", fontsize=label_fontsize)

    ax.tick_params(axis="both", labelsize=ticks_fontsize)
    ax.grid(True, color="lightgray", linestyle="--", linewidth=0.7)
    fig.tight_layout()
    plt.show()












if __name__ == "__main__":
    main()