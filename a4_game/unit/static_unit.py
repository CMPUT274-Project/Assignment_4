from unit.base_unit import BaseUnit
import unit, helper
from tiles import Tile
import pygame

class StaticUnit(BaseUnit):
    """
    The basic static unit.
    - Does not move.

    """
    def __init__(self, **keywords):
        #load the base class
        super().__init__(**keywords)

        #set unit specific things.
        self.type = "Static unit"

    def is_passable(self, tile, pos):
        return False
