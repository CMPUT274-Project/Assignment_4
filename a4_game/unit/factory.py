from unit.static_unit import StaticUnit
import unit, helper, effects
from tiles import Tile
import pygame

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

unit.unit_types["Factory"] = Factory
