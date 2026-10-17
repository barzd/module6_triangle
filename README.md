An equilateral triangle has three equal angles, each measuring 60 degrees. A right triangle must have a 90-degree angle, so an equilateral triangle can never also be right.

| test_invalid_triangle | Yes  | Edited | These sides cannot make a triangle. |
| test_degenerate_triangle_is_invalid | Yes  | Kept | These sides make a flat triangle. |
| test_equilateral_triangle | Yes  | Kept | An equilateral triangle is not right. |
| test_isosceles_triangle | Yes  | Kept | Two sides are equal. |
| test_scalene_triangle | Yes  | Kept | All sides are different. |
| test_right_triangle_with_non_integer_hypotenuse | Yes  | Edited | It allows for tiny rounding differences in the hypotenuse. |

## Acceptance Criteria

• Invalid triangles: If any side is 0 or negative, or if the sides cannot form a triangle, it returns "Invalid".
• Triangle types: Every valid triangle is labeled as equilateral, isosceles, or scalene.
• Right triangles: If it is a valid right triangle, it adds the note right-angle reinforcement required to the result.
