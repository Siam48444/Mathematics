import matplotlib.pyplot as plt
import numpy as np

# Fonts
plt.rcParams['font.family'] = 'KaTeX_Main'
plt.rcParams['mathtext.fontset'] = 'cm'

title_fontsize = 20
label_fontsize = 14
ticks_fontsize = 12



total_stopping_cache = {1: 0}



def main():
    plot_total_stopping_time([i for i in range(1, 10000+1)])
    # print(collatz_total_stopping_time(27))



def collatz_sequence(n: int) -> list[int]:
    if not isinstance(n, int) or n <= 0:
        print(f"Invalid number. Must be positive integer.")
        return []

    result = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        result.append(n)
    return result



def collatz_total_stopping_time(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        print(f"Invalid number. Must be positive integer.")
        return

    if n in total_stopping_cache:
        return total_stopping_cache[n]

    original = n
    count = 0

    while n not in total_stopping_cache:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1

    result = count + total_stopping_cache[n]
    total_stopping_cache[original] = result
    return result
    
    
    
def plot_sequence(numbers: list[int]) -> None:
    if any(n <= 0 or not isinstance(n, int) for n in numbers):
        print("Invalid input list. Must contain positive integers.")
        return

    line_color = "#000000" if len(numbers) == 1 else None

    for num in numbers:
        y = collatz_sequence(num)
        x = [i for i in range(len(y))]
        plt.plot(x, y, marker="", linestyle="-", color=line_color, zorder=3)

    if len(numbers) == 1:
        plt.title(f"Collatz Sequence starting at {numbers[0]}", fontsize=title_fontsize)
        plt.xlabel(f"Iteration = {len(y)-1}", fontsize=label_fontsize)
        plt.ylabel(f"Value  (max = {max(y)})", fontsize=label_fontsize)
    else:
        plt.title(f"Collatz Sequence", fontsize=title_fontsize)
        plt.xlabel(f"Iteration", fontsize=label_fontsize)
        plt.ylabel(f"Value", fontsize=label_fontsize)

    plt.tick_params(axis="both", labelsize=ticks_fontsize)
    plt.grid(True, color="lightgray", linestyle="--", linewidth=0.7, zorder=0)

    plt.show()



def plot_total_stopping_time(numbers: list[int], is_bar: bool=False) -> None:
    if any(not isinstance(n, int) or n <= 0 for n in numbers):
        print("Invalid input list. Must contain positive integers.")
        return

    for num in numbers:
        x = num
        y = collatz_total_stopping_time(num)
        if is_bar:
            plt.bar(x, y, color="#000000", zorder=3)
        else:
            plt.plot(x, y, marker="o", markersize=5, linestyle="", color="#000000")

    plt.title("Collatz Stopping Times", fontsize=title_fontsize)
    plt.xlabel("Starting Number", fontsize=label_fontsize)
    plt.ylabel("Stopping Time", fontsize=label_fontsize)
    plt.tick_params(axis="both", labelsize=ticks_fontsize)
    plt.grid(True, color="lightgray", linestyle="--", linewidth=0.7, zorder=0)

    plt.show()











if __name__ == "__main__":
    main()