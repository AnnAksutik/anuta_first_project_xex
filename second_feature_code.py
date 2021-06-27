# defining new function 
import math


def equation_roots(ratio_1, ratio_2, ratio_3):
    """ returns the roots of a quadratic equation with known parameters a, b, c: a*x**2+b*x+c"""
    d = ratio_2 ** 2 - 4 * ratio_1 * ratio_3  # d-equation discriminant
    if d == 0:
        root_1, root_2 = round(-ratio_2 / (2 * ratio_1), 2), round(-ratio_2 / (2 * ratio_1), 2)
    elif d > 0:
        root_1 = round((-ratio_2 - math.sqrt(d)) / (2 * ratio_1), 2)
        root_2 = round((-ratio_2 + math.sqrt(d)) / (2 * ratio_1), 2)
        root_1, root_2 = min(root_1, root_2), max(root_1, root_2)
    else:
        root_1 = None
        root_2 = None
    return root_1, root_2


# calling the function
if __name__ == "__main__":
    # reading and checking inputs
    while True:
        print("Hello, here we are to find existing roots of he quadratic equation")
        print("Please, enter 3 numbers equal to your 3 coefficients, each in a new line")
        a, b, c = input(), input(), input()
        try:
            a, b, c = float(a), float(b), float(c)
            break
        except ValueError:
            print("Some inputs are not numbers.Please, try again")
    x1, x2 = equation_roots(a, b, c)
    print("The answer is", x1, x2)
else:
    print("Variables are not integer")
