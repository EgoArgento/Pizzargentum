init offset = -1

define cocinero = Character(
    name="Cocinero",
    image="cocinero",
    who_color="#afa",
)

# Trasnformations
transform cocinero_setup:
    right
    zoom 0.2

image cocinero aterrado = At("images/cocinero aterrado.png", cocinero_setup)
image cocinero enojado = At("images/cocinero enojado.png", cocinero_setup)
image cocinero llorando = At("images/cocinero llorando.png", cocinero_setup)
image cocinero sin_delantal llorando = At("images/cocinero sin_delantal llorando.png", cocinero_setup)
