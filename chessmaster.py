#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generic Chess."""


import time


class ChessPiece():
    """Knows position and where to go."""
    prefix  = ''
    
    def __init__(self, position):
        """A constructor."""
        self.position = position
        self.moves = []
        legalmove = ChessPiece.is_legal_move(self, position)
        if not legalmove:
            excep = "'{}' is not a legal start position"
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """A class function that gives numeric tuple.
        Args:
            tile(string): single two-item string arguemnt
        Returns:
            tuple: a 0-based y-coordinate and 0-based x-coordinate; two-item

        Examples:
            algebraic_to_numeric('e7')
            >>>(4, 6)
        """
        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        numb = [1, 2, 3, 4, 5, 6, 7, 8]
        if len(tile) != 2:
            return None
        if tile[0] in letter and int(tile[1]) in numb:
            return (letter.find(tile[0]), int(tile[1])-1
        else:
            return None

    def is_legal_move(self, position):
        """Tests to ensure starting position is legal and on board.
        Args:
            position(str): coordinates
        Returns:
            (bool): T or F
        Examples:
            is_legal_move('a2')
            >>> False
        """
        tuple1 = self.algebraic_to_numeric(position)
        if tuple1:
            return True
        else:
            return False
                    
    def move(self, position):
        """Tracks moves."""
        legal= self.is_legal_move(position)
        if legal:
            timestamp = time.time()
            oldposition = self.prefix + self.position
            position = self.position
            newposition = self.prefix + position
            moves = (oldposition, newposition, timestamp)
            self.moves.append(moves)
            return moves
        else:
            return False


class Rook(ChessPiece):
    """Rook moves."""
    prefix = 'R'
                    
    def is_legal_move(self, position)"
    """Tests to ensure starting position is legal and on board."""
    legal1 = ChessPiece.is_legal_move(self, position)
    if legal1:
        xmove = self.position[0]
        ymove = self.position[1]
        if xmove != position[0]:
            if ymove == position[1]:
                return True
            else:
                return False
        if ymove != position[1]:
            if xmove == position[0]:
                return True
            else:
                return False
    else:
        return False

                    
class Bishop(ChessPiece):
    """Bishop moves."""
    prefix = 'B'
                    
    def is_legal_move(self, position):
        """Tests to ensure starting position is legal and on board."""
        oldposition = self.algrebraic_to_numeric(self.position)
        newposition = self.algebraic_to_numeric(position)
        legal2 = ChessPiece.is_legal_move(self, position)
        if legal2:
            xdistance = int(newposition[0] - oldposition[0])
            ydistance = int(newposition[1] - oldposition[1])
            if (abs(xdistance) <= 1 and abs(ydistance) <= 1) or
               (abs(xdistance) == 1 and abs(ydistance) == 0) or
               (abs(xdistance) == 0 and abs(ydistance) == 1):
                return True
            else:
                return False
        else:
            return False

                    
class King(ChessPiece):
    """King moves."""
    prefix = 'K'
                    
    def is_legal_move(self, position):
        """Tests to ensure starting position is legal and on board."""
        oldposition = self.algrebraic_to_numeric(self.position)
        newposition = self.algebraic_to_numeric(position)
        legal3 = ChessPiece.is_legal_move(self, position)
        if legal3:
            xdistance = int(newposition[0] - oldposition[0])
            ydistance = int(newposition[1] - oldposition[1])
            if (abs(xdistance) <= 1 and abs(ydistance) <= 1) or
               (abs(xdistance) == 1 and abs(ydistance) == 0) or
               (abs(xdistance) == 0 and abs(ydistance) == 1):
                return True
            else:
                return False

                    
class ChessMatch
    """ChessMatch info."""
                    
    def __init__(self, pieces=None):
        """Constructor docstr."""
        if pieces=None:
            self.reset(pieces)
        else:
            pieces = self.pieces
            self.log = []
        def reset(self):
            """Reset doctr.
            Args:
                log(list): list of movies.
                pieces(dict): history.
            Retruns:
                pieces (dict): fixed dict of str.
            """
            self.log = []
            self.pieces = {'Ra1': Rook('a1'),
                           'Rh1': Rook('h1'),
                           'Ra8': Rook('a8'),
                           'Rh8': Rook('h8'),
                           'Bc1': Bishop('c1'),
                           'Bf1': Bishop('f1'),
                           'Bc8': Bishop('c8'),
                           'Bf8': Bishop('f8'),
                           'Ke1': King('e1'),
                           'Ke8': King('e8')}
            return self.pieces
