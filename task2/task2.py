import sys

path_1 = sys.argv[1]
path_2 = sys.argv[2]

with open(path_1, 'r') as circle_file, open(path_2, 'r') as points_file:
    center_x, center_y = map(int, circle_file.readline().split())
    radius = int(circle_file.readline())
    points_coord = [line.strip().split() for line in points_file.readlines()]


def check_point(x: float, y: int) -> int:
    d_x = abs(center_x - x)
    d_y = abs(center_y - y)
    if d_x ** 2 + d_y ** 2 > radius ** 2:
        return 2
    elif d_x ** 2 + d_y ** 2 == radius ** 2:
        return 0
    else:
        return 1



for point in points_coord:
    x, y = map(int, point)
    print(check_point(x=x, y=y))
