import math


def max_error(n):
    return 0.5 * 10**-n


def approximation(f, a, b):
    return (b * f(a) - a * f(b)) / (f(a) - f(b))


def false_position(f, a, b, tol):
    # f: function , a : lower bound, b:upper bound, tol: tolerance level (max_error)
    if f(a) * f(b) >= 0:
        print("False Position Method doesn't exist")
        return None

    c = approximation(f, a, b)
    i = 0

    # Print headers for the table
    print(f"{'i':<4}{'a':<10}{'b':<10}{'c':<10}{'f(c)':<15}{'error':<15}")
    print(f"{i:<4}{a:<10.4f}{b:<10.4f}{c:<10.4f}{f(c):<15.4f}{'-':<15}")

    while True:
        if f(c) == 0:
            print(f"Exact root found: {c:.4f}")
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_new = approximation(f, a, b)
        error = abs(c_new - c)

        i += 1

        print(
            f"{i:<4}{a:<10.4f}{b:<10.4f}{c_new:<10.4f}{f(c_new):<15.4f}{error:<15.4f}"
        )

        if error < tol:
            print(
                f"Root found at c = {c_new:.4f} with error = {error:.4f} at {i}th iteration, which is less than the defined tolerance {tol:.4f}"
            )
            return c_new

        c = c_new


def get_function():

    func_str = input("Enter your function: ")

    # Function to replace function names
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


func = get_function()
a = float(input("Enter lower Bound(a): "))
b = float(input("Enter upper bound(b): "))
n = int(input("Enter the decimal place: "))
error = max_error(n)

root = false_position(func, a, b, error)
if root is not None:
    print(f"∴ The required approximated root: {root:.3f}")
