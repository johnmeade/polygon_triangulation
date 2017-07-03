
import numpy as np
from random import random as r


def _rough_cover( arc, n ):
    # Triangulate an arc by successively clipping off triangles.

    if len(arc) < 3: return []

    # counter hits 0 when we have travelled around the entire perimeter
    # without finding a triangle
    # => the arc must be convex clockwise
    # => reverse arc and continue
    if n == 0: return _rough_cover( list( reversed( arc ) ), len( arc ) )

    # Determine the order of the points using the z-component of the cross
    # product. Returns negative if clockwise, positive if counter-clockwise,
    # or 0 if there is no order.
    a, b, c = arc[:3]
    p, q = b-a, c-a
    cross_z = p[0] * q[1] - p[1] * q[0]
    if cross_z >= 0: arc.pop(1)

    # move to next vertex
    arc.append( arc.pop(0) )

    # add triangle if CCW, then recursively cover
    if cross_z > 0: return [ (a, b, c) ] + _rough_cover( arc, len(arc) )
    else: return _rough_cover( arc, n-1 )


def rough_cover( arc ):
    '''Finds an approximate triangulation cover for a polygonal region. This
    runs in linear time and is able to perfectly triangulate "simple"
    (roughly convex) regions. For more complex shapes, there may be areas that
    are covered twice, or areas may be covered that are outside the
    polygon boundary.

    The polygonal region must be encoded as a list of points in
    counter-clockwise order. The last point in
    the arc is implicitly joined to the first point in the arc. The return
    value is an array of triangles which covers the region, where a triangle
    is a list of three points (in CCW order).
    '''
    # make a copy to avoid side-effects
    arc = list( arc )
    # convert to numpy arrays if needed
    n = len( arc )
    if n > 0 and type(arc[0]) is not np.ndarray:
        arc = [ np.array( x ) for x in arc ]
    return _rough_cover( arc, n )
