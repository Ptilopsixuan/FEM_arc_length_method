import numpy as np
import matplotlib.pyplot as plt
from autograd import grad

def Y(x):
    y = x**3
    return y

def K(x):
    k = 3*x**2
    # k = 1-1/x**2
    return k

def arc(start_x, s, y_max, steps):
    xs = [start_x]
    las = [0]
    for i in range(steps):
        x = xs[i]
        la = las[i]
        k = K(x)

        dx = y_max/k
        dL = s/(dx**2 + 1)**0.5
        dx = dL*y_max/k
        la += dL
        x += dx

        R = la*y_max-Y(x)
        iter = 0

        while abs(R) > 1e-7:
            iter += 1
            if i != 0 and iter == 1:
                if np.dot(np.array([xs[i]-xs[i-1], las[i]-las[i-1]]), np.array([dx, dL])) < 0:
                    dL = -dL
                    dx = -dx
                    la += 2* dL
                    x += 2*dx

            print(f"Step {i+1}; iteration {iter}")
            k = K(x)

            Kr = R/k
            Kf = y_max/k
            a = y_max**2+Kf**2
            b = 2*((la-las[i])*y_max**2+Kf*(Kr+x-xs[i]))
            c = Kr*(Kr+2*(x-xs[i]))
            roots = np.roots([a, b, c])
            dL = roots[np.argmin(abs(roots))]

            la += dL
            R = la*y_max - Y(x)
            dx = R*y_max/k
            x += dx
            R = la*y_max - Y(x)

        xs.append(x)
        las.append(la)

    return xs, las

if __name__ == "__main__":
   y_max = 5
   s = 0.01
   start_x = 0.01
   steps = 20
   x, la = arc(start_x, s, y_max, steps)
   plt.plot(x, [l*y_max for l in la])
   plt.show()

