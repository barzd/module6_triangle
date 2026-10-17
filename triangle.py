import math


def is_valid_triangle(a, b, c):
    """
    Check if the given sides can form a valid triangle.

    return bool True if the sides can form a valid triangle, False otherwise.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)


def is_right_triangle(a, b, c):
    """Return whether the valid triangle has a right angle."""
    if not is_valid_triangle(a, b, c):
        return False

    first, second, longest = sorted((a, b, c))
    return math.isclose(first**2 + second**2, longest**2, rel_tol=1e-9)


def classify_triangle(a, b, c):
    """
    Classify the triangle based on the lengths of its sides.

    return str The type of triangle: 'equilateral', 'isosceles', or 'scalene'.
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        classification = "equilateral"
    elif a == b or b == c or a == c:
        classification = "isosceles"
    else:
        classification = "scalene"

    if is_right_triangle(a, b, c):
        return f"{classification}; right-angle reinforcement required"
    return classification