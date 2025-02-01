from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def integral_mc(func: Callable, a: float, b: float, n: int) -> float:
    x_random = np.random.uniform(a, b, n)
    y_random = np.random.uniform(0, max(func(np.linspace(a, b, 1000))), n)

    under_curve = y_random < func(x_random)
    return ((b - a) * max(func(np.linspace(a, b, 1000))) * np.sum(under_curve) / n, x_random, y_random)


def draw_plot(f, x_random, y_random, a, b):
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

    ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.3)
    plt.grid()
    plt.show()


def main():
    def f(x):
        return (x - 1) ** 2 + 2

    a = 0
    b = 3
    n = 1000

    mc_result, x_random, y_random = integral_mc(f, a, b, n)

    draw_plot(f, x_random, y_random, a, b)

    result, error = spi.quad(f, a, b)

    print("Monte carlo: ", mc_result)
    print("spipy: ", result)


if __name__ == "__main__":
    main()
