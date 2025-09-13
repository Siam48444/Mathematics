import matplotlib.pyplot as plt



def main() -> None:
    # print(multiplicative_persistence(9999999))
    plot_multiplicative_persistence([10])



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

    x = [i for i in range(0, max(numbers)+1)]
    y = [multiplicative_persistence(j) for j in x]
    print(x)
    print(y)












if __name__ == "__main__":
    main()