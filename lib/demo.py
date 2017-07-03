
import numpy as np
import matplotlib.pyplot as plt
from lib.cover import rough_cover
from lib.uniform_fill import uniform_fill_tri


def unzip(x):
    'lazy implementation'
    return np.array(x).T


def to_array(arc):
    return [ np.array(p) for p in arc ]


def circ(a, b, n=50):
    return [ [ np.cos(x), np.sin(x) ] for x in np.linspace(a, b, 40) ]


def dual_disk():
    arc1 = circ( np.pi*(1/12), np.pi*(2-1/12) )
    arc2 = circ( np.pi*(1+1/12), np.pi*(3-1/12) )
    shifted = [ [x+2, y] for x,y in arc2 ]
    arc = arc1 + shifted
    return to_array( arc )


def crenelation():
    arc = [ [0,0], [1,0], [1,1], [2,1], [2,0],
        [3,0], [3,3], [2,3], [2,2], [1,2], [1,3],
        [0,3], [0,2], [-1,2], [-1,3], [-2,3],
        [-2,0], [-1,0], [-1,1], [0,1] ]
    return to_array( arc )


def s():
    arc = [ [0,0], [2,0], [2,3], [1,3], [1,4], [2,4],
        [2,5], [0,5], [0,2], [1,2], [1,1], [0,1] ]
    return to_array( arc )


def plot_arc( arc, ax, plot_tris=True, uniform_fill=True ):

    # plot outline
    ax.plot(*unzip(arc + arc[:1]), '#bbbbbb', linewidth=12)

    tris = rough_cover( arc )

    # plot triangles
    if plot_tris:
        for tri in tris:
            ax.plot(*unzip(tri + tri[:1]))

    # compute uniform scatter of points in each triangle with constant density
    density = 50 # points per 1 unit square
    points = []
    for x,y,z in tris:
        p = y-x
        q = z-x
        area = (p[0]*q[1] - p[1]*q[0]) / 2.0
        n = int(round(density * area))
        points += uniform_fill_tri(x, y, z, n)

    # plot points
    if uniform_fill:
        ax.scatter(*unzip(points), s=1)


if __name__ == '__main__':

    plot_tris = True
    uniform_fill = True

    fig, axs = plt.subplots( 1, 3, figsize=(16,6) )

    plot_arc( crenelation(), axs[0], plot_tris, uniform_fill )
    plot_arc( dual_disk(), axs[1], plot_tris, uniform_fill )
    plot_arc( s(), axs[2], plot_tris, uniform_fill )

    plt.show()
