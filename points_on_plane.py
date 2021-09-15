def new_point_on_plane(point1, point2, x3):
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    y3 = slope * (x3 - point1[0]) + point1[1]
    return y3

def is_point_on_plane(point1, point2, point3):
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    y3_expected = slope * (point3[0] - point1[0]) + point1[1]
    if y3_expected == point3[1]:
        return True
    else:
        return False