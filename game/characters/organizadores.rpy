init offset = -1

define organizador1 = Character(
    name="Organizador",
    image="organizador1",
    who_color="#5725bb",
    who_outlines=[(2, "#210e46", 0, 0)],
)
define sfx_organizador1_huh = "audio/sfx/huh-002-120386-5.ogg"
define sfx_organizador1_hmm = "audio/sfx/hmm-mhmm-76486.ogg"

define organizador2 = Character(
    name="Organizadora",
    image="organizador2",
    who_color="#f1ffd6",
    who_outlines=[(2, "#3a3d33", 0, 0)],
)
define sfx_organizador2_ehem = "audio/sfx/woman-clears-throat-411743.ogg"
define sfx_organizador2_sigh = "audio/sfx/woman-sigh-101931.ogg"

define organizador1y2 = Character(
    name="Organizador y Organizadora",
    who_color="#5725bb",
    who_outlines=[(2, "#f1ffd6", 0, 0)],
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
image organizador1 cansado = At("images/organizador1 cansado.png", organizador_setup)
image organizador1 confundido = At("images/organizador1 confundido.png", organizador_setup)
image organizador1 desconfiado = At("images/organizador1 desconfiado.png", organizador_setup)
image organizador1 enojado = At("images/organizador1 enojado.png", organizador_setup)
image organizador1 indiferente = At("images/organizador1 indiferente.png", organizador_setup)
image organizador1 sorprendido = At("images/organizador1 sorprendido.png", organizador_setup)

image organizador2 cansada = At("images/organizador2 cansada.png", organizador2_setup)
image organizador2 confundida = At("images/organizador2 confundida.png", organizador2_setup)
image organizador2 desinteresada = At("images/organizador2 desinteresada.png", organizador2_setup)
image organizador2 enojada = At("images/organizador2 enojada.png", organizador2_setup)
image organizador2 entretenida = At("images/organizador2 entretenida.png", organizador2_setup)
image organizador2 sorprendida = At("images/organizador2 sorprendida.png", organizador2_setup)

# Textos

style susurro is text:
    italic True
    size gui.text_size - 5
    color "#444D"