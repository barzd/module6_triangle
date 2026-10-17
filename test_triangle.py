import math

import pytest

from triangle import classify_triangle, is_valid_triangle


@pytest.mark.parametrize("sides", [(0, 4, 5), (-1, 4, 5), (1, 2, 4)])
def test_invalid_triangle(sides):
	assert is_valid_triangle(*sides) is False
	assert classify_triangle(*sides) == "Invalid"


def test_degenerate_triangle_is_invalid():
	sides = (1, 2, 3)

	assert is_valid_triangle(*sides) is False
	assert classify_triangle(*sides) == "Invalid"


def test_equilateral_triangle():
	assert classify_triangle(4, 4, 4) == "equilateral"
	assert is_right_triangle(4, 4, 4) is False


def test_isosceles_triangle():
	assert classify_triangle(5, 5, 6) == "isosceles"


def test_scalene_triangle():
	assert classify_triangle(4, 5, 6) == "scalene"


def test_right_triangle_with_non_integer_hypotenuse():
	hypotenuse = 5 * math.sqrt(2)

	assert is_right_triangle(5, 5, hypotenuse) is True


def test_non_right_triangle():
	assert is_right_triangle(2, 3, 4) is False
