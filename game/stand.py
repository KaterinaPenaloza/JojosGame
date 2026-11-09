from enum import Enum

class StandType(Enum):
    CLOSE_RANGE = "close range"
    LONG_RANGE = "long range"

class Stand:
    def __init__(self, stand_name, stand_type, stand_power, stand_speed, stand_range, stand_durability, stand_precision, stand_potential):
        # Atributos de instancia
        self.name = stand_name
        self.type = stand_type
        self.power = stand_power
        self.speed = stand_speed
        self.range = stand_range
        self.durability = stand_durability
        self.precision = stand_precision
        self.potential = stand_potential

    def __str__(self):
        return f"{self.name}"

# Team Bucciarati
sticky_fingers = Stand("Sticky Fingers", StandType.CLOSE_RANGE, 5, 5, 3, 2, 3, 2)
gold_experience = Stand("Gold Experience", StandType.CLOSE_RANGE, 3, 5, 3, 2, 3, 5)
sex_pistols = Stand("Sex Pistols", StandType.LONG_RANGE, 1, 3, 4, 5, 5, 4)
aerosmith = Stand("Aerosmith", StandType.LONG_RANGE, 4, 4, 4, 3, 1, 3)
purple_haze = Stand("Purple Haze", StandType.CLOSE_RANGE, 5, 4, 3, 1, 1, 4)
moody_blues = Stand("Moody Blues", StandType.CLOSE_RANGE, 3, 3, 5, 5, 3, 3)
spice_girl = Stand("Spice Girl", StandType.CLOSE_RANGE,5,5,3,4,2,3)
# La Squadra Esecuzioni
metallica = Stand("Metallica", StandType.CLOSE_RANGE,3,3,3,5,3,3)
little_feet = Stand("Little Feet", StandType.CLOSE_RANGE,2,4,1,5,2,3)
man_in_the_mirror = Stand("Man in the Mirror", StandType.CLOSE_RANGE,3,3,4,2,3,1)
grateful_death = Stand("Grateful Death", StandType.CLOSE_RANGE,4,1,4,5,1,3)
beach_boy = Stand("Beach Boy", StandType.LONG_RANGE,3,4,4,3,3,5)
baby_face = Stand("Baby Face", StandType.LONG_RANGE,5,4,5,5,1,1)
white_album = Stand("White Album", StandType.CLOSE_RANGE,5,3,3,5,1,1)