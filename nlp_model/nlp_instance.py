#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# todo: further redesign when all part is implemented eg: merge add_dependency and add_span

from enum import Enum

from .token import Token
from .edge import EdgeRenderType, Edge


class RenderType(Enum):
    """An enum to specify how an instance should be rendered.

    Either a single sentence is shown or two aligned sentences,
    on top of each other.
    """
    single = 'single',
    alignment = 'alignment'


class NLPInstance:
    """An NLPInstance represents a sentence or utterance and some of its (NLP) properties.

    Properties of sentence are its tokens, that have their own properties, and
    edges between tokens. Such edges can represent syntactic or semantic
    dependencies, such as SRL predicate-argument relations, as well as annotated
    spans (such as NP chunks or NER entities).
    
    Attributes:
        tokens (list): The tokens of this instance.
        edges (list): The edges of this instance.
        render_type (RenderType): How to render this instance.
        token_map (dict[int, Token]): A mapping from sentence indices to tokens.
        split_points (list): A list of token indices at which the NLP instance is to
            be split. These indices can refer to sentence boundaries in a
            document, but they can also indicate that what follows after a split
            point is an utterance in a different language (for alignment).
    """

    
    def __init__(self, tokens: tuple or list=None, edges: set or frozenset=None,
                 render_type: RenderType=RenderType.single, split_points: tuple or list=None):
        """Create an NLPInstance with the given tokens and edges.
        
        The passed collections will be copied and not changed.
        
        Args:
            tokens (tuple or list): 
            edges (set or frozenset):
            render_type (RenderType):
            split_points (tuple or list): 
        """
        self.tokens = [] 
        self.token_map = {}
        self.edges = [] 
        self.render_type = render_type
        self.split_points = []
        if tokens is not None:
            self.tokens.extend(tokens)
            for t in tokens:
                self.token_map[t.index] = t
        if edges is not None:
            self.edges.extend(edges)
        if split_points is not None:
            self.split_points.extend(split_points)



    def add_edge(self, start: int, end: int, label: str=None, edge_type: str=None,
                 render_type: EdgeRenderType=None, desc=None, note: str=None,
                 is_final: bool=True):
        """Creates and adds an edge with the given properties.
        
        Args:
            start (int): The index of the start token.
            end (int): The index of the end token.
            label (str, optional): The label of the edge. Defaults to None.
            edge_type (str, optional): The type of the edge.  Defaults to None.
            render_type (EdgeRenderType, optional): The render type of the edge.
                Defaults to None.
            desc (str, optional): The description of the edge. Defaults to None.
            note (str, optional): The note associated with the edge. Defaults to None.
            is_final (bool, optional): Is the edge final? Defaults to False.

        Raises:
            KeyError: If there was no token at one of the given positions.
        """
        if self.is_valid_edge(start, end):
            self.edges.append(Edge(self.token_map[start], self.token_map[end], label,
                                   edge_type, note, render_type, desc, is_final))
        else:
            raise KeyError("Couldn't add edge: no token at positions {} and {}.".
                           format(start, end))

            
    def is_valid_edge(self, start, end):
        """Returns whether a valid edge can be drawn between two positions.

        Args:
            start (int): The start index of the edge.
            end (int): The end index of the edge.

        Returns:
            bool: True iff there are tokens at the two given positions.
        """
        return start in self.token_map and end in self.token_map

    
    def add_span(self, start: int, end: int, label: str, span_type: str, desc: str=None):
        """Creates and adds an edge with rendertype RenderType#span.
        
        Args:      
            start (int): Index of the token the edge should start at. The token at the
                given index must already exist in the sentence.
            end (int): Index of the token the edge should end at. The token at the
                given index must already exist in the sentence.
            label (str): The label of the edge.
            span_type (str): The type of edge.
            desc (str, optional): The description of the span.

        Raises:
            KeyError: If there was no token at one of the given positions.
        """
        if self.is_valid_edge(start, end):
            self.edges.append(Edge(self.token_map[start], self.token_map[end], label,
                                   span_type, render_type=EdgeRenderType.span,
                                   description=desc))
        else:
            raise KeyError("Couldn't add edge: no token at positions {} and {}.".
                           format(start, end))

        
    def add_dependency(self, start: int, end: int, label, dep_type: str, desc: str=None,
                      is_final: bool=True):
        """Creates and adds an edge with render type RenderType#dependency.

        Args:      
            start (int): Index of the token the edge should start at. The token at the
                given index must already exist in the sentence.
            end (int): Index of the token the edge should end at. The token at the
                given index must already exist in the sentence.
            label (str): The label of the edge.
            dep_type (str): The type of edge.
            desc (str, optional): The description of the span.
            is_final (bool, optional): Whether the dependency is final. Defaults to true.

        Raises:
            KeyError: If there was no token at one of the given positions.
        """
        if self.is_valid_edge(start, end):
            self.edges.append(Edge(self.token_map[start], self.token_map[end], label, dep_type,
                                   render_type=EdgeRenderType.dependency, description=desc,
                                   is_final=is_final))
        else:
            raise KeyError("Couldn't add edge: no token at positions {} and {}.".
                           format(start, end))

        
    def add_tokens(self, tokens: tuple):
        """Adds the given collection of tokens to this instance.
        
        Args:
            tokens (tuple): The tokens to add.
        """
        self.tokens.extend(tokens)
        for t in tokens:
            self.token_map[t.index] = t

            
    def add_edges(self, edges: list):
        """Adds the given collection of edges to this instance.
        
        Args:
            edges (tuple): The edges to add.
        """
        self.edges.extend(edges)
        

    def merge(self, nlp):
        """Merges the given instance with this instance.
        
        A merge will add for every token i all properties of the token i of the
        passed instance ``nlp``. It will also add every edge between i and i in the
        given instance ``nlp`` as an edge between the tokens i and j of this
        instance, using the same type, label and rendertype as the original
        edge.
        
        Args:
            nlp (NLPInstance): The instance to merge into this instance.
        """
        for i in range(0, min(len(self.tokens), len(nlp.tokens))):
            self.tokens[i].merge(nlp.tokens(i))
        for edge in nlp.edges():
            self.add_edge(start=edge.start.index, end=edge.end.index, label=edge.label,
                          edge_type=edge.edge_type, render_type=edge.render_type,
                          note=edge.note)

            
    def add_token_with_properties(self, *properties):
        """Add a token to this NLPInstance that has the provided properties.

        Args:
            *properties: TokenProperty instances.
        """
        token = Token(len(self.tokens))
        for prop in properties:
            token.add_property(prop)
        self.tokens.append(token)
        self.token_map[token.index] = token

        
    def add_token(self, index: int=None, is_actual: bool=False) -> Token:
        """Add a token at the given index.

        This method can be used when we don't want to build the sentence in
        order.

        Note: 
            If you build the instance using this method you have to call
            NLPInstance#consistify() when you are done.
        
        Args:
            index (int, optional): The position where the token should be added.
                If not given then the position will be set to the number of already
                present tokens.
            is_actual (bool, optional): Is the token actual? Defaults to False.

        Returns:
            Token: The token that was added.
        """
        if index is None:
            vertex = Token(len(self.tokens), is_actual)
            self.tokens.append(vertex)
            self.token_map[vertex.index] = vertex
        else:
            vertex = self.token_map[index]
            if vertex is None:
                vertex = Token(index)
                self.token_map[vertex.index] = vertex

        return vertex

    
    def consistify(self):
        """Ensure that the all internal representations of the token sequence are consistent.
        
        If tokens were added with NLPInstance#add_token() this method ensures
        that all internal representations of the token sequence are consistent.
        """
        self.tokens.extend(self.token_map.values())
        self.tokens.sort()

        
    def add_split_point(self, token_index: int):
        """Add a split point token index.

        Args:
            token_index (int): A token index at which the instance should be split.
        """
        self.split_points.append(token_index)

        
    def get_edges(self, render_type: RenderType=None) -> frozenset:
        """Return all edges of this instance with a given render_type.
        
        Args:
            render_type (RenderType, optional): The render type of the edges to return.
        
        Returns:
            frozenset: All edges of this instance with the given render type. If no
            render type is specified then the set of all edges is returned.
        """
        return frozenset({e for e in self.edges if
                          e.render_type == render_type or render_type is None})

    
    def get_token(self, index: int) -> Token:
        """Return the token at the given index.

        Args:
            index (int): The index of the token to return.

        Returns:
            Token: The token at the given index.
        """
        return self.token_map[index]


    def __str__(self):
        """Return a string representation of this instance.

        Note: 
            Mostly for debugging purposes.

        Returns:
            str: A string representation of this instance.
        """
        return "{0}\n{1}\n{2}".format(", ".join(str(token) for token in self.tokens),
                                      ", ".join(str(v) for v in self.token_map.values()),
                                      ", ".join(str(e) for e in self.edges))


def nlp_diff(gold_instance: NLPInstance, guess_instance: NLPInstance) -> NLPInstance:
    """Calculate the difference between two NLP instances in terms of their edges.
    
    Args:
        gold_instance (NLPInstance): The gold instance.
        guess_instance (NLPInstance): The guess instance.

    Returns:
        NLPInstance: An NLPInstance with Matches, False Negatives and False Positives
        of the difference.
    """
    diff = NLPInstance()
    diff.render_type = gold_instance.render_type
    for split_point in gold_instance.split_points:
        diff.add_split_point(split_point)
    diff.add_tokens(gold_instance.tokens)
    goldIdentities = gold_instance.get_edges()
    guessIdentities = guess_instance.get_edges()
    fn = goldIdentities - guessIdentities
    fp = guessIdentities - goldIdentities
    matches = goldIdentities & guessIdentities
    for edge in fn:
        Type = edge.edge_type + ":FN"
        diff.add_edge(start=edge.start.index, end=edge.end.index, label=edge.label, note=edge.note, edge_type=Type,
                     render_type=edge.render_type, desc=edge.description)
    for edge in fp:
        Type = edge.edge_type + ":FP"
        diff.add_edge(start=edge.start.index, end=edge.end.index, label=edge.label, note=edge.note, edge_type=Type,
                     render_type=edge.render_type, desc=edge.description)

    for edge in matches:
        Type = edge.edge_type + ":Match"
        diff.add_edge(start=edge.start.index, end=edge.end.index, label=edge.label, note=edge.note, edge_type=Type,
                     render_type=edge.render_type, desc=edge.description)
    return diff
