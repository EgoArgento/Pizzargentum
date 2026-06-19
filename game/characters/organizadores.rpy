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
image organizador1 indiferente = At("images/organizador1 indiferente.png", organizador_setup)
image organizador1 sorprendido = At("images/organizador1 sorprendido.png", organizador_setup)

image organizador2 entretenida = At("images/organizador2 entretenida.png", organizador2_setup)
image organizador2 enojada = At("images/organizador2 enojada.png", organizador2_setup)
image organizador2 desinteresada = At("images/organizador2 desinteresada.png", organizador2_setup)

# Textos

style susurro is text:
    italic True
    size 24
    color "#333"