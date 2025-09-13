import matplotlib.pyplot as plt



def main() -> None:
    plot_multiplicative_persistence([i for i in range(1, 10000)])



def multiplicative_persistence(n):
    """Calculates the multiplicative persistence of a number."""

    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer.")

    persistence = 0

    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        
        n = product
        persistence += 1

    return persistence



def plot_multiplicative_persistence(numbers: list[int]) -> None:
    """Plots the persistences for given numbers."""

    y = [multiplicative_persistence(i) for i in numbers]

    plt.bar(numbers, y, color="black", zorder=7)
    plt.grid(False, color="lightgray", linestyle="--", linewidth=0.7, zorder=0)
    plt.show()












if __name__ == "__main__":
    main()