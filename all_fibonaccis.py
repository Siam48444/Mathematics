import matplotlib.pyplot as plt
import numpy as np

# Math fonts
plt.rcParams['font.family'] = 'KaTeX_Main'
plt.rcParams['mathtext.fontset'] = 'cm'



def main():
    n_vals = np.linspace(0, 4, 2000)

    real_vals = []
    imag_vals = []
    for n in n_vals:
        r, i = binet(n)
        real_vals.append(r)
        imag_vals.append(i)

    fig, ax = plt.subplots()     
    ax.plot(real_vals, imag_vals, marker="", linestyle="-", color="red")

    ax.set_title(r"Binet's Formula for Real $n$", fontsize=20)
    ax.set_xlabel(r"$\Re(F_n)$", fontsize=14)
    ax.set_ylabel(r"$\Im(F_n)$", fontsize=14)
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)

    ax.grid(True)
    plt.show()         



def fib(lim):
    if lim <= 0:
        return []

    f1, f2 = 1, 1 
    res = [f1, f2]
    for n in range(lim-2):
        res.append(res[-1] + res[-2])
    return res



def binet(n):
    phi = (1 + np.sqrt(5)) / 2

    re = (phi**n - phi**(-n)*np.cos(np.pi*n))/np.sqrt(5)
    im = -(phi**(-n)*np.sin(np.pi*n))/np.sqrt(5)

    return re, im






if __name__ == "__main__":
    main()