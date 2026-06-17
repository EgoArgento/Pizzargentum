init offset = -1

init python:
    class MainCharacter:
        def __init__(self):
            self.name = "Vos"
            self.c = Character(
                self.get_name,
                dynamic=True,
                image="protagonista",
                who_color="#ff0000",
            )
        def get_name(self):
            return self.name

default protagonista = MainCharacter()

# Transformations
transform character_setup:
    left
    zoom 0.2

#
image protagonista normal = At("images/protagonista normal.png", character_setup)
image protagonista enojado = At("images/protagonista enojado.png", character_setup)
image protagonista levanta_cejas = At("images/protagonista levanta_cejas.png", character_setup)
image protagonista sorprendido = At("images/protagonista sorprendido.png", character_setup)