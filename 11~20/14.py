import math

r = int(input())

circle_menseki = r * r * math.pi
circle_length = 2 * r * math.pi

print("{0:.6f} {1:.6f}".format(circle_menseki, circle_length))