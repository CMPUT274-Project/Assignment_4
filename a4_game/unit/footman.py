from unit.ground_unit import GroundUnit
import unit, helper, effects
from tiles import Tile
import pygame

class Footman(GroundUnit):
    """
    A footman. Posessing no technology, they conquer all by sheer magnitude.
    Popularised in 1924, they were designed by Werner Herzog in the middle of 
    Arabia with the intention of swarming one's defenses. Only produced by factories.

    Armour: Low
    Speed: High
    Range: Low
    Damage: Low
    
    Other notes:
    - Can move through any land terrain.
    - Will be destroyed by most anything, but can be used to swarm defenses.
    """
    sprite = pygame.image.load("assets/footman.png")
    
    def __init__(self, **keywords):
        #load the image for the base class.
        self._base_image = Footman.sprite

        #load the base class
        super().__init__(**keywords)
        
        #sounds
        self.move_sound = "JeepMove"
        self.hit_sound = "MachineGunFire"

        #set unit specific things.
        self.type = "Footman"
        self.speed = 10
        self.max_atk_range = 2
        self.damage = 3
        self.defense = 1
        self.hit_effect = effects.Ricochet
        
        self._move_costs = {'plains': 2,
                             'sand': 2,
                             'forest': 2,
                             'road': 1,
                             'mountain': 3}

unit.unit_types["Footman"] = Footman
