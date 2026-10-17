import math

from triangle import classify_triangle


def test_triangle_customer_workflow():
	assert classify_triangle(0, 4, 5) == "Invalid"
	assert classify_triangle(1, 2, 3) == "Invalid"
	assert classify_triangle(5, 5, 6) == "isosceles"

	hypotenuse = 5 * math.sqrt(2)
	assert classify_triangle(5, 5, hypotenuse) == (
		"isosceles; right-angle reinforcement required"
	)
