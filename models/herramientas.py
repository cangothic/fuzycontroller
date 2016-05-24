from models.model_sections import Line, Point


def intersection(line1, line2):
    x = (line2.b-line1.b)/(line1.m-line2.m)
    y = line1.m*x + line1.b
    return Point(x, y)


def inter_point(point1, point2):
    m = (point2.y-point1.y)/(point2.x-point1.x)
    b = point2.y-point2.x*m
    return Line(m, b)


