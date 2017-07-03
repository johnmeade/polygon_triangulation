About
======

This repo contains Python code to triangulate polygons and fill them uniformly
with points. The repo currently contains:

* a fast but approximate tringle-covering algorithm

* a function which will uniform-randomly fill an arbitrary triangle with points

The approximate cover algorithm is `from cover import rough_cover`. It should run in linear time and will cover the interior of any polygon. It is
approximate because of an edge case with two consequences:

* there may be areas that are covered twice

* areas may be covered that are outside the polygon boundary.

For many roughly-convex polygons it will compute an exact triangulation.
Exact triangulation in linear time is possible, but it is fairly complex.
A more straightforward `n*log(n)` algorithm also exists for exact
triangulation.

WIP: an exact triangulation algorithm


Installation
=============

Note: Windows users will have to go hunt down and install `numpy` and possibly
other dependencies manually...

This code may not work with Python 2, use Python 3 if possible.

```
# [ Optional, Recommended ] Set up a virtual environment:
$ virtualenv -p python3 .venv
$ source .venv/bin/activate

# To install from frozen dependencies:
$ pip install -r requirements.txt

# If this doesn't work try installing from direct dependencies:
$ pip install -r requirements.in
```


Usage
======

Note: You may need to install additional packages to show matplotlib windows
for the demos (there will be console output telling you which package)

You can run a demo like so:

```
$ python -m lib.demo
```
