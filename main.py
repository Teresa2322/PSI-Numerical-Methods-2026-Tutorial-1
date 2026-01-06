# Hello World for PSI Numerical Methods 2026
import numpy as np
import matplotlib.pyplot as plt
 
print("Hello PSI 2026!")
print(np.exp(1.2))

x = np.linspace(0,2*np.pi,100)

plt.plot(x,np.sin(x), label = "sin(x)", color = 'green')
plt.plot(x,np.cos(x), label = "cos(x)", color = 'blue')
plt.legend()

plt.savefig("trig.png")

def myexp(x, N=10):
    """
    This function computes exp(x) via the Taylor Series using terms up to
    order N.
    """

    t = 1.0  # The value of the current term
    y = 1.0  # The value of exp(x) up to this point

    # We initialize with the 0th order term, so run the loop
    # for the remaining N terms.
    for i in range(1, N+1):
        t *= x/i  # Update the term: tn = x^n / n!
        y += t    # add tn to y

    # We're done!
    return y


if __name__ == "__main__":

    print("Hello, world!")

    print("e(1) with  5 terms is", myexp(1.0, 5))
    print("e(1) with 10 terms is", myexp(1.0, 10))
    print("e(1) with 20 terms is", myexp(1.0, 20))
    print("e(1) with 40 terms is", myexp(1.0, 40))
