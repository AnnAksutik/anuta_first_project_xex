# defining new function 
import math


def equation_roots(a, b, c):
    """ returns the roots of a quadratic equation with known parameters a, b, c: a*x**2+b*x+c"""
    d = b ** 2 - 4 * a * c  # d-equation discriminant
    if d == 0:
        x1, x2 = -b / (2 * a), -b / (2 * a)
    elif d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        x1, x2 = min(x1, x2), max(x1, x2)
    else:
        x1 = None
        x2 = None
    return x1, x2


# calling the function
if __name__ == "__main__":
    # reading and cheking inputs
    while True:
        a, b, c = input(), input(), input()
        try:
            a, b, c = float(a), float(b), float(c)
            break
        except ValueError:
            print("Some inputs are not numbers.Please, try again")
    x1, x2 = equation_roots(a, b, c)
    print(x1, x2)
else:
    print('Variables are not integer')
