import matplotlib.pyplot as plt
import numpy as np

# Fonts
plt.rcParams['font.family'] = 'KaTeX_Main'
plt.rcParams['mathtext.fontset'] = 'cm'

title_fontsize = 20
label_fontsize = 14
ticks_fontsize = 12

fig, ax = plt.subplots()
ax.tick_params(axis="both", labelsize=ticks_fontsize)
ax.grid(True, color="lightgray", linestyle="--", linewidth=0.7)



def main():
    # plot_sequence([703])
    # print(max_in_range(1, 1000))
    plot_stopping_time([i for i in range(1, 1000+1)])



def collatz_sequence(n: int) -> list[int]:
    if not isinstance(n, int) or n <= 0:
        print(f"Invalid number. Must be positive integer.")
        return []

    result = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        result.append(n)
    return result



def collatz_stopping_time(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        print(f"Invalid number. Must be positive integer.")
        return

    stops = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        stops += 1
    return stops



def max_in_range(start: int, end: int) -> tuple[int, int]:
    if not isinstance(start, int) or not isinstance(end, int) or start <= 0 or end <= 0:
        print(f"Invalid number. Must be positive integer.")
        return

    max_val = 0
    num = 2
    for i in range(start, end+1):
        seq = collatz_sequence(i)
        if max(seq) > max_val:
            max_val = max(seq)
            num = i
    return (num, max_val)



def plot_sequence(numbers: list[int]) -> None:
    if any(n <= 0 or not isinstance(n, int) for n in numbers):
        print("Invalid input list. Must contain positive integers.")
        return

    line_color = "red" if len(numbers) == 1 else None

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

    plt.show()



def plot_stopping_time(numbers: list[int]) -> None:
    if any(not isinstance(n, int) or n <= 0 for n in numbers):
        print("Invalid input list. Must contain positive integers.")
        return

    for num in numbers:
        x = num
        y = collatz_stopping_time(num)
        ax.plot(x, y, marker="o", markersize=5, linestyle="", color="red")

    ax.set_title("Collatz Stopping Times", fontsize=title_fontsize)
    ax.set_xlabel("Starting Number", fontsize=label_fontsize)
    ax.set_ylabel("Stopping Time", fontsize=label_fontsize)

    plt.show()











if __name__ == "__main__":
    main()