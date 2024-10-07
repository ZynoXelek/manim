from __future__ import annotations

from manim import *
from manim.utils.testing.frames_comparison import frames_comparison

__module_test__ = "graph"


@frames_comparison
def test_GraphLoopEdge(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (2, 3), (3, 1), (4, 5), (4, 1), (5, 1), (5, 2), (4, 4)]
    labels = True
    layout = "circular"
    g = Graph(vertices, edges, labels=labels, layout=layout)
    scene.add(g)


@frames_comparison
def test_DiGraphLoopEdge(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (2, 4), (3, 2), (4, 5), (4, 1), (5, 1), (5, 3), (4, 4)]
    labels = True
    layout = "circular"
    g = DiGraph(vertices, edges, labels=labels, layout=layout)
    scene.add(g)


@frames_comparison
def test_WeightedGraph(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 3), (2, 3), (3, 4), (4, 2), (4, 5), (5, 1), (5, 3)]
    labels = True
    layout = "circular"
    weights = {
        (1, 3): "4",
        (2, 3): Tex("5", color=RED),
        (3, 4): 0,
        (4, 2): "3",
        (4, 5): 3,
        (5, 1): "2",
        (5, 3): "1",
    }
    g = Graph(
        vertices,
        edges,
        labels=labels,
        weights=weights,
        layout=layout,
    )
    scene.add(g)


@frames_comparison
def test_WeightedDiGraph(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 4), (2, 3), (3, 4), (1, 3), (4, 2), (5, 4), (5, 1)]
    labels = True
    layout = "circular"
    weights = {
        (1, 4): "1",
        (2, 3): -1,
        (3, 4): MathTex("2"),
        (1, 3): "2",
        (4, 2): 4,
        (5, 4): 1.5,
        (5, 1): "7/2",
    }
    g = DiGraph(
        vertices,
        edges,
        labels=labels,
        weights=weights,
        layout=layout,
    )
    scene.add(g)


@frames_comparison
def test_GraphWeightedLoopEdge(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 5), (2, 4), (3, 2), (4, 5), (4, 1), (3, 3), (5, 3)]
    weights = {
        (1, 2): 1,
        (1, 5): 2,
        (2, 4): 1,
        (3, 2): 4,
        (4, 5): 3,
        (4, 1): 5,
        (3, 3): 1,
        (5, 3): 2,
    }
    labels = True
    layout = "circular"
    g = Graph(vertices, edges, labels=labels, layout=layout, weights=weights)
    scene.add(g)


@frames_comparison
def test_DiGraphWeightedLoopEdge(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 5), (2, 4), (3, 2), (4, 5), (4, 3), (3, 3), (5, 3)]
    weights = {
        (1, 2): 1,
        (1, 5): 2,
        (2, 4): 1,
        (3, 2): 4,
        (4, 5): 3,
        (4, 3): 5,
        (3, 3): 1,
        (5, 3): 2,
    }
    labels = True
    layout = "circular"
    g = DiGraph(vertices, edges, labels=labels, layout=layout, weights=weights)
    scene.add(g)


@frames_comparison
def test_WeightsConfiguration(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 5), (2, 4), (3, 2), (4, 5), (4, 3), (3, 3), (5, 3)]
    weights = {
        (1, 2): 1,
        (1, 5): 2,
        (2, 4): 1,
        (3, 2): 4,
        (4, 5): 3,
        (4, 3): 5,
        (3, 3): 1,
        (5, 3): 2,
    }
    labels = True
    layout = "circular"
    edge_config = {
        "weight_config": {
            "position_ratio": 0.3,
            "min_size_ratio": 1 / 6,
            "max_size_ratio": 1 / 4,
            "text_color": BLUE,
        },
        (1, 2): {
            "weight_config": {
                "label": "5",
                "min_size_ratio": 1 / 3,
                "max_size_ratio": 1 / 3,
                "text_color": RED,
            }
        },
    }
    g = Graph(
        vertices,
        edges,
        labels=labels,
        layout=layout,
        weights=weights,
        edge_config=edge_config,
    )
    scene.add(g)


@frames_comparison
def test_LoopsConfiguration(scene):
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 1), (1, 2), (2, 4), (3, 2), (4, 5), (4, 3), (3, 3), (5, 3), (5, 5)]
    weights = {
        (1, 1): 1,
        (1, 2): 2,
        (2, 4): 1,
        (3, 2): 4,
        (4, 5): 3,
        (4, 3): 5,
        (3, 3): 1,
        (5, 3): 2,
        (5, 5): 4,
    }
    labels = True
    layout = "circular"
    edge_config = {
        "loop_config": {"angle_between_points": PI, "path_arc": 3 * PI / 2},
        (3, 3): {
            "loop_config": {"angle_between_points": PI / 2, "path_arc": 15 / 8 * PI}
        },
    }
    g = Graph(
        vertices,
        edges,
        labels=labels,
        layout=layout,
        weights=weights,
        edge_config=edge_config,
    )
    scene.add(g)


@frames_comparison(last_frame=False)
def test_MovingGraph(scene):
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4), (1, 3), (3, 3), (4, 1)]
    weights = {
        (1, 2): 1,
        (2, 3): 2,
        (3, 4): 1,
        (1, 3): 3,
        (3, 3): 5,
        (4, 1): 1,
    }
    layout = "circular"
    edge_config = {
        "weight_config": {
            "min_size_ratio": 1 / 6,
            "max_size_ratio": 1 / 5,
        }
    }
    g = Graph(
        vertices,
        edges,
        labels=True,
        layout=layout,
        weights=weights,
        edge_config=edge_config,
    )
    scene.play(Create(g))
    scene.wait()
    scene.play(
        g[1].animate.move_to([3, 2, 0]),
        g[2].animate.move_to([0, -3, 0]),
        g[3].animate.move_to([-1, -2, 0]),
        g[4].animate.move_to([-3, 1, 0]),
    )
    scene.wait()


@frames_comparison(last_frame=False)
def test_MovingDiGraph(scene):
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4), (1, 3), (3, 3), (4, 1)]
    weights = {
        (1, 2): 1,
        (2, 3): 2,
        (3, 4): 1,
        (1, 3): 3,
        (3, 3): 5,
        (4, 1): 1,
    }
    layout = "circular"
    edge_config = {
        "weight_config": {
            "min_size_ratio": 1 / 4,
            "max_size_ratio": 1 / 3,
        }
    }
    g = DiGraph(
        vertices,
        edges,
        labels=True,
        layout=layout,
        weights=weights,
        edge_config=edge_config,
    )
    scene.play(Create(g))
    scene.wait()
    scene.play(
        g[1].animate.move_to([3, 2, 0]),
        g[2].animate.move_to([0, -3, 0]),
        g[3].animate.move_to([-1, -2, 0]),
        g[4].animate.move_to([-3, 1, 0]),
    )
    scene.wait()