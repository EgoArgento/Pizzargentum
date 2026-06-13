# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform bit_right:
    right
    xoffset 150

define o1= Character("Organizador 1")
define o2= Character("Organizador 2")
# The game starts here.

label start:
    # Cualquier configuración global que haya que realizar,
    # se debe ejecutar en esta sección

    jump ch1_inscripcion
