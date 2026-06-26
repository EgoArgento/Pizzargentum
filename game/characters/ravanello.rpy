init offset = -1

define ravanello = Character(
    name="Ravanello",
    image="ravanello",
    who_color="#400D0D",
    who_outlines=[(2, "#f99", 0, 0)],
)

define sfx_laughin_ravanello = "audio/sfx/deep-laugh-chucklemp3-14518.ogg"

transform ravanello_setup:
    right
    zoom 0.2

image ravanello asustado = At("images/ravanello asustado.png", ravanello_setup)
image ravanello burlon = At("images/ravanello burlon.png", ravanello_setup)
image ravanello confundido = At("images/ravanello confundido.png", ravanello_setup)
image ravanello confiado = At("images/ravanello confiado.png", ravanello_setup)
image ravanello delirante = At("images/ravanello delirante.png", ravanello_setup)
image ravanello desafiante = At("images/ravanello desafiante.png", ravanello_setup)
image ravanello enojado = At("images/ravanello enojado.png", ravanello_setup)
image ravanello entusiasmado = At("images/ravanello entusiasmado.png", ravanello_setup)
image ravanello llorando = At("images/ravanello llorando.png", ravanello_setup)
