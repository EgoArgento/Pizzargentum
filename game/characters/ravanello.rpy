init offset = -1

define ravanello = Character(
    name="Ravanello",
    image="ravanello",
    who_color="#f05",
)

transform ravanello_setup:
    right
    zoom 0.2

image ravanello confundido = At("images/ravanello confundido.png", ravanello_setup)
image ravanello confiado = At("images/ravanello confiado.png", ravanello_setup)
image ravanello desafiante = At("images/ravanello desafiante.png", ravanello_setup)
image ravanello enojado = At("images/ravanello enojado.png", ravanello_setup)
image ravanello llorando = At("images/ravanello llorando.png", ravanello_setup)
