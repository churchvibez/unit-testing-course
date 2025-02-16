import math

def solve_quadratic(a: float, b: float, c: float):
    """Calculate the roots of a quadratic equation: ax^2 + bx + c = 0"""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        # one real root
        root = -b / (2 * a)
        return (root,)
    else:
        # complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

if __name__ == "__main__":
    # Quick manual tests
    print(solve_quadratic(1, -3, 2))   # Should print: (2.0, 1.0)
    print(solve_quadratic(1, 2, 1))    # Should print: (-1.0,)
    print(solve_quadratic(1, 1, 1))    # Should print complex roots
