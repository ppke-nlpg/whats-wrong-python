#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .token_layout import TokenLayout, middle
from ..model.edge import EdgeRenderType
from .svg_writer import Line, QuadraticBezierCurve


class AlignmentRenderer:
    """An AlignmentRenderer renders two aligned sentences.

    Attributes:
        _token_layout1 (TokenLayout): The the token layout for the first
            sentence.
        _token_layout2 (TokenLayout): The the token layout for the second
            sentence.
        _height_factor (int): Controls the height of the graph.
        _is_curved (bool): Whether the graph is should be curved or rectangular.
    """

    def __init__(self):
        """Initialize an AlignmentRenderer.
        """
        self._token_layout1 = TokenLayout()
        self._token_layout2 = TokenLayout()
        self._height_factor = 100              # TODO: Constants?
        self._is_curved = True
        self._token_layout1.to_split_point = 0
        self._token_layout2.from_split_point = 0
        self.fp_color = (255, 0, 0)   # Red    # TODO: Constants?
        self.fn_color = (0, 0, 255)   # Blue   # TODO: Constants?
        self.match_color = (0, 0, 0)  # Black  # TODO: Constants?

    def render(self, instance, scene):
        """Renders the given instance as a pair of aligned sentences.

        Args:
            instance (NLPInstance): The instance to render.
            scene (Scene): The graphics object to draw upon.

        Returns:
            tuple: The width and height of the drawn object.
        """
        token_xbounds1 = self._token_layout1.estimate_token_bounds(instance, {}, scene)
        token_xbounds2 = self._token_layout2.estimate_token_bounds(instance, {}, scene)

        width = 0
        height = 0

        # place dependencies on top
        dim = self._token_layout1.layout(instance, {}, scene)
        height += dim[1]
        if dim[0] > width:
            width = dim[0]

        # TODO: This should be in some layout class?
        for edge in instance.get_edges(EdgeRenderType.dependency):
            if 'eval_status_FP' in edge.properties:
                edge_color = self.fp_color
            elif 'eval_status_FN' in edge.properties:
                edge_color = self.fn_color
            else:
                edge_color = self.match_color
            bound1 = token_xbounds1[edge.start]
            bound2 = token_xbounds2[edge.end]
            if self._is_curved:
                start = (middle(bound1), height)
                ctrl1 = (middle(bound1), height + self._height_factor // 2)
                ctrl2 = (middle(bound2), height + self._height_factor // 2)
                end = (middle(bound2), height + self._height_factor)
                scene.add(QuadraticBezierCurve(scene, start, ctrl1, ctrl2, end, edge_color))
            else:
                start = (middle(bound1), height)
                end = (middle(bound2), height + self._height_factor)
                scene.add(Line(scene, start, end, edge_color))

        # add spans
        scene.translate(0, dim[1] + self._height_factor)
        dim = self._token_layout2.layout(instance, {}, scene)
        height += dim[1] + self._height_factor
        if dim[0] > width:
            width = dim[0]

        return width, height + 1

    @property
    def margin(self):
        """Returns the margin between tokens.

        Returns:
            int: The margin between tokens.
        """
        return self._token_layout1.margin()

    @margin.setter
    def margin(self, value):
        """Sets the margin between tokens.

        Args:
            value (int): The margin between tokens.
        """
        self._token_layout1.margin = value
        self._token_layout2.margin = value
