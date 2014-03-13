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

    def turn_ended(self):
        """
        Called when the turn for this unit's team has ended.
        Returns True if the unit is still alive, and False otherwise.
        """
        self.turn_state = [True, False]
        # ensures that the movement button is disabled.
        return True
