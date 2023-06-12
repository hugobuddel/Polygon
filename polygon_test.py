# -*- coding: utf-8 *-*
"""Test Polygon.py."""

import ast
import unittest
from pathlib import Path

import pylab

from polygon import Point, Segment, Polygon

PATH_REGIONS = Path(__file__).resolve().parent / "polygons"


def open_str(pathname):
    """ first str() then open_str(), this should not be necessary anymore in Python 3.6 """
    return open(str(pathname))


def polygon6a():
    """Polygon test 6a."""
    coords1 = ast.literal_eval(open_str(PATH_REGIONS / "edgesself6a.txt").read())
    coords2 = ast.literal_eval(open_str(PATH_REGIONS / "edgesother6a.txt").read())

    coords1a = [ast.literal_eval(p) for p in coords1]
    coords2a = [ast.literal_eval(p) for p in coords2]

    edges1 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords1a]
    edges2 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords2a]

    poly1 = Polygon(edges=edges1)
    poly2 = Polygon(edges=edges2)

    edges3 = poly1.find_union_edges(poly2)

    intersections = []
    for edge1 in edges3:
        for edge2 in edges3:
            if len({edge1.start, edge1.end, edge2.start, edge2.end}) == 4 and edge1.intersects(edge2):
                intersections.append((edge1, edge2, edge1.intersection(edge2)))

    assert len(intersections) == 0

    l123 = len(edges3), len([e.start for e in edges3]), len([e.end for e in edges3])
    assert l123 == (110, 110, 110)

    polyt = Polygon(edges=poly1.edges)
    polyt._lazy_edges = edges3
    polyt._lazy_vertices = None
    polyt._sort_edges()
    intersections = polyt.check_self_intersection()
    edges_inter = {e1 for e1, e2, p in intersections}
    assert not edges_inter

    fig, ax = pylab.subplots(1, 1)

    for polygon, col in [
        (poly1, "g"),
        (poly2, "b"),
    ]:
        xx = polygon.xs()
        yy = polygon.ys()
        ax.fill(xx, yy, col, alpha=0.5)

    for edge in edges3:
        ax.plot(edge.xs(), edge.ys(), "k")

    for e1, e2, inter in intersections:
        ax.plot(e1.xs(), e1.ys(), "r")
        ax.plot(e2.xs(), e2.ys(), "r")

    fig.show()


def polygon6b():
    """Polygon test 6b."""
    coords1 = ast.literal_eval(open_str(PATH_REGIONS / "edgesunion6b.txt").read())

    coords1a = [ast.literal_eval(p) for p in coords1]

    edges1 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords1a]

    poly1 = Polygon()
    poly1._lazy_edges = edges1

    fig, ax = pylab.subplots(1, 1)

    for polygon, col in [
        (poly1, "g"),
        #     (poly2, 'b'),
        #     (poly3, 'r'),
    ]:
        xx = polygon.xs()
        yy = polygon.ys()
        ax.fill(xx, yy, col, alpha=0.5)

    fig.show()


def polygon6c():
    """Polygon test 6c."""
    coords1 = ast.literal_eval(open_str(PATH_REGIONS / "edgesself6c.txt").read())
    coords2 = ast.literal_eval(open_str(PATH_REGIONS / "edgesother6c.txt").read())
    coords3 = ast.literal_eval(open_str(PATH_REGIONS / "edgesunion6c.txt").read())

    coords1a = [ast.literal_eval(p) for p in coords1]
    coords2a = [ast.literal_eval(p) for p in coords2]
    coords3a = [ast.literal_eval(p) for p in coords3]

    edges1 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords1a]
    edges2 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords2a]
    edges3 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords3a]

    poly1 = Polygon(edges=edges1)
    poly2 = Polygon(edges=edges2)

    edges4 = poly1.find_union_edges(poly2)
    # TODO: Ensure 21 is the desired length.
    assert len(edges4) == 21

    intersections = []
    for edge1 in edges3:
        for edge2 in edges3:
            if len({edge1.start, edge1.end, edge2.start, edge2.end}) == 4 and edge1.intersects(edge2):
                intersections.append((edge1, edge2, edge1.intersection(edge2)))

    # TODO: Ensure that 4 interactions is actually correct.
    assert len(intersections) == 4

    fig, ax = pylab.subplots(1, 1)

    for polygon, col in [
        (poly1, "g"),
        (poly2, "b"),
        #     (poly3, 'r'),
    ]:
        xx = polygon.xs()
        yy = polygon.ys()
        ax.fill(xx, yy, col, alpha=0.5)

    for edge in edges3:
        ax.plot(edge.xs(), edge.ys(), "k")

    for e1, e2, inter in intersections:
        ax.plot(e1.xs(), e1.ys(), "r")
        ax.plot(e2.xs(), e2.ys(), "r")

    fig.show()


def polygon6d():
    """Polygon test 6d."""
    coords1 = ast.literal_eval(open_str(PATH_REGIONS / "edgesself6d.txt").read())
    coords2 = ast.literal_eval(open_str(PATH_REGIONS / "edgesother6d.txt").read())
    coords3 = ast.literal_eval(open_str(PATH_REGIONS / "edgesunion6d.txt").read())

    coords1a = [ast.literal_eval(p) for p in coords1]
    coords2a = [ast.literal_eval(p) for p in coords2]
    coords3a = [ast.literal_eval(p) for p in coords3]

    edges1 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords1a]
    edges2 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords2a]
    edges3 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords3a]

    poly1 = Polygon(edges=edges1)
    poly2 = Polygon(edges=edges2)

    poly4 = poly1.union(poly2)

    intersections = []
    for edge1 in edges3:
        for edge2 in edges3:
            if len({edge1.start, edge1.end, edge2.start, edge2.end}) == 4 and edge1.intersects(edge2):
                intersections.append((edge1, edge2, edge1.intersection(edge2)))

    assert len(intersections) == 0

    fig, ax = pylab.subplots(1, 1)

    for polygon, col in [
        (poly1, "g"),
        (poly2, "b"),
        # TODO: Determine whether it is better to plot the edges of poly4
        (poly4, "r"),
    ]:
        xx = polygon.xs()
        yy = polygon.ys()
        ax.fill(xx, yy, col, alpha=0.5)

    for edge in edges3:
        ax.plot(edge.xs(), edge.ys(), "k")

    for e1, e2, inter in intersections:
        ax.plot(e1.xs(), e1.ys(), "r")
        ax.plot(e2.xs(), e2.ys(), "r")

    xs = [inter.x for e1, e2, inter in intersections]
    ys = [inter.y for e1, e2, inter in intersections]
    ax.scatter(xs, ys)

    fig.show()


def polygon7a():
    """Polygon test 7a."""
    coords1 = [
        (15998.0, 12128.0),
        (16178.0, 12148.0),
        (16318.0, 12188.0),
        (17967.252, 12347.252),
        (17967.252, 11868.748),
        (17488.748, 11868.748),
        (15948.0, 11998.0),
        (15968.0, 11948.0),
    ]

    points1 = [Point(x, y) for x, y in coords1]

    poly1 = Polygon()
    poly1._lazy_vertices = points1
    iss = poly1.check_self_intersection()
    (edge1, edge2, intersection) = iss[0]
    edge1begin = Segment(edge1.start, intersection)
    edge1end = Segment(intersection, edge1.end)
    edge2begin = Segment(edge2.start, intersection)
    edge2end = Segment(intersection, edge2.end)
    index_edge1 = poly1.edges.index(edge1)
    index_edge2 = poly1.edges.index(edge2)
    # Should hold due to the way check_self_intersection works.
    assert index_edge1 < index_edge2, "Wrong Order"
    edges1a = poly1.edges[:index_edge1] + [edge1begin, edge2end] + poly1.edges[index_edge2 + 1 :]
    edges1b = [edge1end] + poly1.edges[index_edge1 + 1 : index_edge2] + [edge2begin]
    poly1a = Polygon(edges=edges1a)
    poly1b = Polygon(edges=edges1b)

    fig, ax = pylab.subplots(1, 1)

    xx = [p.x for p in points1]
    yy = [p.y for p in points1]
    ax.fill(xx, yy, "g", alpha=0.5)

    for polygon, col in [
        #     (poly1, 'g'),
        (poly1a, "b"),
        (poly1b, "r"),
    ]:
        xx = polygon.xs()
        yy = polygon.ys()
        ax.fill(xx, yy, col, alpha=0.5)

    fig.show()


def polygon7b():
    """Polygon test 7b."""
    coords1 = ast.literal_eval(open_str(PATH_REGIONS / "edgesself7b.txt").read())
    coords2 = ast.literal_eval(open_str(PATH_REGIONS / "edgesother7b.txt").read())
    coords3 = ast.literal_eval(open_str(PATH_REGIONS / "edgesunion7b.txt").read())
    coords4 = ast.literal_eval(open_str(PATH_REGIONS / "edgesdone7b.txt").read())
    coords5 = ast.literal_eval(open_str(PATH_REGIONS / "edgestodo7b.txt").read())

    coords1a = [ast.literal_eval(p) for p in coords1]
    coords2a = [ast.literal_eval(p) for p in coords2]
    coords3a = [ast.literal_eval(p) for p in coords3]
    coords4a = [ast.literal_eval(p) for p in coords4]
    coords5a = [ast.literal_eval(p) for p in coords5]

    edges1 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords1a]
    edges2 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords2a]
    edges3 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords3a]
    edges4 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords4a]
    edges5 = [Segment(Point(x1, y1), Point(x2, y2)) for (x1, y1), (x2, y2) in coords5a]

    poly1 = Polygon(edges=edges1)
    poly2 = Polygon(edges=edges2)

    poly4 = Polygon(edges=edges4)
    poly5 = Polygon(edges=edges5)

    intersections = []
    for edge1 in edges3:
        for edge2 in edges3:
            if len({edge1.start, edge1.end, edge2.start, edge2.end}) == 4 and edge1.intersects(edge2):
                intersections.append((edge1, edge2, edge1.intersection(edge2)))

    assert len(intersections) == 0

    poly1.union(poly2)
    poly2.union(poly1)

    fig, ax = pylab.subplots(1, 1)

    for polygon, col in [
        (poly1, "g"),
        (poly2, "b"),
        (poly4, "r"),
        (poly5, "y"),
    ]:
        xx = polygon.xs()
        yy = polygon.ys()
        ax.fill(xx, yy, col, alpha=0.5)

    for edge in edges3:
        ax.plot(edge.xs(), edge.ys(), "k")

    xs = poly4.xs()
    ys = poly4.ys()
    ax.scatter(xs, ys)

    for e1, e2, inter in intersections:
        ax.plot(e1.xs(), e1.ys(), "r")
        ax.plot(e2.xs(), e2.ys(), "r")

    xs = [inter.x for e1, e2, inter in intersections]
    ys = [inter.y for e1, e2, inter in intersections]
    ax.scatter(xs, ys)
    fig.show()


class PolygonTest(unittest.TestCase):
    """Test Polygon class."""

    def test_polygons(self):
        """Test Polygons.

        No Exception raised is good enough.
        Manually inspect the figures to determine whether they are correct.
        """
        polygon6a()
        polygon6b()
        polygon6c()
        polygon6d()
        polygon7a()
        polygon7b()


if __name__ == "__main__":
    unittest.main()
