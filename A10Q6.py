
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    iterations = []
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Function has the same sign at both ends of the interval.")
        return None

    for i in range(max_iter):
        m = (a + b) / 2
        fm = f(m)
        iterations.append(m)

        if abs(fm) < tol or abs(b - a) / 2 < tol:
            print(f"Root found at x = {m:.6f} with f(m) = {fm:.6e} after {i+1} iterations")
            break

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
    else:
        print("Max iterations reached without converging to desired tolerance.")

    return np.array(iterations)

a = 0.0
b = 3.0

updates = bisection_method(f, a, b)

x = np.linspace(a - 1, b + 1, 400)
y = f(x)

plt.plot(x, y, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

if updates is not None:
    plt.plot(updates, f(updates), 'ro-', label='Bisection Updates')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method for Root Finding')
plt.legend()
plt.grid(True)
plt.show()
#plt.savefig("bisection_plot.png")
#print("Plot saved as 'bisection_plot.png'")