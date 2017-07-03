
from random import random as r


def uniform_fill_tri(x,y,z,n):
    '''Uniform-randomly fill a triangle (x,y,z) with n points'''

    a, b = y-x, z-x
    points = []

    for i in range(n):
        r0, r1 = r(), r()
        if r0 + r1 > 1:
            # this point would land *outside* triangle, so we
            # reflect it back inside by inverting random nums
            r0, r1 = 1-r0, 1-r1
        points.append( x + r0 * a + r1 * b )

    return points
