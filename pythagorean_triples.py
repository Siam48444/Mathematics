import math



def main() -> None:
    primitive_triples(5)



# In both functions, argument 'lim' is the maximum value for 'a' and 'b' to generate triples.

def pythagorean_triples(lim: int) -> None:
    """Prints all Pythagorean triples up to limit."""
    for i in range(1, lim):
        for j in range(i+1, lim+1):
            print(abs(i**2 - j**2), 2*i*j, i**2 + j**2)



def primitive_triples(lim: int) -> None:
    """Prints only primitive Pythagorean triples up to limit."""
    for i in range(1, lim):
        for j in range(i+1, lim+1):
            if math.gcd(i, j) == 1 and (i % 2 == 0 or j % 2 == 0):
                print(abs(i**2 - j**2), 2*i*j, i**2 + j**2)










if __name__ == "__main__":
    main()