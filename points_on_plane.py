def new_point_on_plane(point1, point2, x3):
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    y3 = slope * (x3 - point1[0]) + point1[1]
    return y3
