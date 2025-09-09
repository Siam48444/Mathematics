def main():
    lim = 5
    for i in range(1, lim):
        for j in range(i+1, lim+1):
            print(P(i, j))



def P(a: int, b: int) -> tuple[int, int, int]:
    return (abs(a**2 - b**2), 2*a*b, a**2 + b**2)










if __name__ == "__main__":
    main()