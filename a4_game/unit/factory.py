from unit.static_unit import StaticUnit
from unit.base_unit import BaseUnit

from pygame.sprite import LayeredUpdates
from collections import namedtuple

import unit, helper, effects
import tiles
import sys, pygame

class Factory(StaticUnit):
    """
    A factory. While it provides no actual damage,
    it spawns a jeep at the beginning of every turn. 
    Possessing high defenses, it is difficult to take down. However, when 
    surrounded, it can be destroyed with ease.
    
    Armour: High
    Speed: None
    Range: None
    Damage: None

    Other notes:
    - Placed near the centre of the base.
    - Spawns a jeep on top of the unit at the beginning of every turn, 
      unless the jeep of the previous day has not yet moved.
    """
    sprite = pygame.image.load("assets/factory.png")

    def __init__(self, **keywords):
        
        #load the image for the base class.
        self._base_image = Factory.sprite

        #load the base class
        super().__init__(**keywords)

        #sounds
        self.hit_sound = "ArtilleryFire"

        #set unit specific things.
        self.type = "Factory"
        self.speed = 0
        self.max_atk_range = 0
        self.damage = 0
        self.defense = 1
        self.hit_effect = effects.Explosion
        self.turn_state = [True, False]

    def ready_to_build(self, pos):
        """
        Checks if the given position is over a unit.
        """
        for u in BaseUnit.active_units:
            if (u.tile_x == pos[0] and u.tile_y == pos[1] + 1):
                return False
            # if found, return something is in.

        # if not return nothing found.
        return True

    def turn_ended(self):
        """
        Called when the turn is ended.
        """
        self.turn_state = [True, False]
        return True

    def build_jeep(self):
        if self.ready_to_build(self.tile_pos):
            #builds the jeep
            new_unit = unit.unit_types['Jeep'](team = self.team, 
                                               tile_x = self.tile_pos[0],
                                               tile_y = self.tile_pos[1] + 1,
                                               activate = True,
                                               angle = 0)
            return new_unit
        return None
        

unit.unit_types["Factory"] = Factory
