def is_valid_triangle(a, b, c):
    """
    Check if the given sides can form a valid triangle.

    return bool True if the sides can form a valid triangle, False otherwise.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)


def classify_triangle(a, b, c):
    """
    Classify the triangle based on the lengths of its sides.

    return str The type of triangle: 'equilateral', 'isosceles', or 'scalene'.
    """
    
    
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"