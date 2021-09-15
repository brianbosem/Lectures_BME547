import pytest

@pytest.mark.parametrize("point1, point2, x3, expected", [
    # FILL IN TEST CASES
    ((1,4), (2,4), 7, 4),
    ((-3, 6), (8,2), 19, -2),
    ((2, 1), (1, 2), 3, 0),
    ((7, 3), (2, 4), -3, 5),
    ((6, 1), (-12, 10), 26, -9) ])

def test_points_on_plane(point1, point2, x3, expected):
    from points_on_plane import new_point_on_plane
    answer = new_point_on_plane(point1, point2, x3)
    assert answer == expected

@pytest.mark.parametrize("point1, point2, point3, expected", [
    # FILL IN TEST CASES
    ((1,4), (2,4), (7,4), True),
    ((-3, 6), (8,2), (19,-2), True),
    ((2, 1), (1, 2), (3, 0), True),
    ((7, 3), (2, 4), (-3, 5), True), 
    ((6, 1), (-12, 10), (26, -9), True),
    ((1,4), (2,4), (9,22), False),
    ((-3, 6), (8,2), (19, -3), False),
    ((2, 1), (1, 2), (3, 10), False),
    ((7, 3), (2, 4), (-32, 5), False),
    ((6, 1), (-12, 10), (2, -9), False)
    ])

def test_tf_points_on_plane(point1, point2, point3, expected):
    from points_on_plane import is_point_on_plane
    answer = is_point_on_plane(point1, point2, point3)
    assert answer == expected