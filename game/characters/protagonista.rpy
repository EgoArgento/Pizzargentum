init offset = -1

init python:
    class MainCharacter:
        def __init__(self):
            self.name = "Vos"
            self.c = Character(
                self.get_name,
                dynamic=True,
                image="protagonista",
                who_color="#F50106",
            )
        def get_name(self):
            return self.name

default protagonista = MainCharacter()

# Transformations
transform character_setup:
    left
    zoom 0.2

#
image protagonista delirante = At("images/protagonista delirante.png", character_setup)
image protagonista enojado = At("images/protagonista enojado.png", character_setup)
image protagonista incredulo = At("images/protagonista incredulo.png", character_setup)
image protagonista sin_delantal = At("images/protagonista sin_delantal.png", character_setup)
image protagonista sonriente = At("images/protagonista sonriente.png", character_setup)
image protagonista sorprendido = At("images/protagonista sorprendido.png", character_setup)

transform delantal_setup:
    zoom 0.9
    yoffset -50

image delantal primer plano = At("images/delantal primer plano.png", delantal_setup)