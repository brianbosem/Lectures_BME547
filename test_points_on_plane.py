import pytest

@pytest.mark.parametrize("point1, point2, x3, expected", [
    # FILL IN TEST CASES
    ((1,4), (2,4), 7, 4)
    ((-3, 6), (8,2), 12, 6/11)
    ((2, 1), (1, 2), 3, 0)
    ((7, 3), (2, 4), -3, 5)
    ((6, 1), (-12, 10), 26, -9)
])

def test_points_on_plane(point1, point2, x3, expected):
    from points_on_plane import new_point_on_plane
    answer = new_point_on_plane(point1, point2, x3)
    assert answer == expected