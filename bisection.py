import math


def max_error(n):
    return 0.5 * 10**-n


def approx_root(a, b):
    return (a + b) / 2


def bisection_method(f, a, b, tol):

    if f(a) * f(b) >= 0:
        print("Bisection method doesn't exist in the given interval.")
        return None

    c = approx_root(a, b)
    i = 0

    print(f"{'i':<4}{'a':<10}{'b':<10}{'c':<10}{'f(c)':<15}{'error':<15}")
    print(f"{i:<4}{a:<10.4f}{b:<10.4f}{c:<10.4f}{f(c):<15.4f}{'-':<15}")

    while True:
        if f(c) == 0:
            print(f"Exact root found: {c:.4f}")
            return c

        # update bounds
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c1 = approx_root(a, b)
        error = abs(c1 - c)

        i += 1

        print(f"{i:<4}{a:<10.4f}{b:<10.4f}{c1:<10.4f}{f(c1):<15.4f}{error:<15.4f}")

        if error <= tol:
            print(
                f"Root found at c = {c1:.4f} with error = {error:.4f} at {i}th iteration, which is less than or equal to the defined tolerance {tol:.4f}"
            )
            return c1

        c = c1


def get_function():

    func_str = input("Enter your function: ")

    # Function to replace function names for math expressions
    def replace_functions(expr):
        return (
            expr.replace("sin(", "math.sin(")
            .replace("cos(", "math.cos(")
            .replace("tan(", "math.tan(")
            .replace("exp(", "math.exp(")
            .replace("log(", "math.log(")
            .replace("sqrt(", "math.sqrt(")
            .replace("^", "**")
        )

    def func(x):

        func_eval = replace_functions(func_str)

        return eval(func_eval)

    return func


# Input for the bisection method
func = get_function()
a = float(input("Enter lower bound (a): "))
b = float(input("Enter upper bound (b): "))
n = int(input("Enter the decimal place: "))
tol = max_error(n)

root = bisection_method(func, a, b, tol)

if root is not None:
    print(f"∴ The required approximated root: {root:.{n}f}")
