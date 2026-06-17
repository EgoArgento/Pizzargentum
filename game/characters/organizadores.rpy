define organizador1 = Character(
    name="Organizador",
    image="organizador1",
)

define organizador2 = Character(
    name="Organizadora",
    image="organizador2",
)

# Trasnformations
transform organizador_setup:
    right
    zoom 0.2

transform organizador2_setup:
    right
    zoom 0.2
    xoffset 250

#
image organizador1 normal = At("images/organizador1 normal.png", organizador_setup)
image organizador1 sorprendido = At("images/organizador1 sorprendido.png", organizador_setup)

image organizador2 normal = At("images/organizador2 normal.png", organizador2_setup)
image organizador2 enojada = At("images/organizador2 enojada.png", organizador2_setup)
image organizador2 desinteresada = At("images/organizador2 desinteresada.png", organizador2_setup)
