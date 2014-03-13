from unit.static_unit import StaticUnit
import unit, helper, effects
from tiles import Tile
import pygame

class Turret(StaticUnit):
    """
    A turret. Structured, it is immobile,
    but offers a heavy defense provided that it is not reached.

    Armour: Medium
    Speed: None
    Range: High
    Damage: Medium

    Other notes:
    - Placed in strategic zones.
    - The structure is generally placed within the middle of the 
    - holding site, in order to hold defense.
    """
    sprite = pygame.image.load("assets/turret.png")

    def __init__(self, **keywords):
        #load the image for the base class.
        self._base_image = Turret.sprite

        #load the base class
        super().__init__(**keywords)
        
        #sounds
        self.move_sound = "JeepMove"
        #there is no move sound required.
        self.hit_sound = "ArtilleryFire"
        #can adjust, but ArtilleryFire sounds the most authentic.

        #set unit specific things.
        self.type = "Turret"
        self.speed = 0
        self.max_atk_range = 8
        self.damage = 7
        self.defense = 1
        self.hit_effect = effects.Explosion

unit.unit_types["Turret"] = Turret
