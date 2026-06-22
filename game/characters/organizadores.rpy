define organizador1 = Character(
    name="Organizador",
    image="organizador1",
    who_color="#0f0",
)
define sfx_organizador1_huh = "audio/sfx/huh-002-120386-5.ogg"
define sfx_organizador1_hmm = "audio/sfx/hmm-mhmm-76486.ogg"

define organizador2 = Character(
    name="Organizadora",
    image="organizador2",
    who_color="#00f",
)
define sfx_organizador2_ehem = "audio/sfx/woman-clears-throat-411743.ogg"

define organizador1y2 = Character(
    name="Organizador y Organizadora",
    who_color="#0ff",
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
image organizador1 desconfiado = At("images/organizador1 desconfiado.png", organizador_setup)
image organizador1 enojado = At("images/organizador1 enojado.png", organizador_setup)
image organizador1 indiferente = At("images/organizador1 indiferente.png", organizador_setup)
image organizador1 sorprendido = At("images/organizador1 sorprendido.png", organizador_setup)

image organizador2 cansada = At("images/organizador2 cansada.png", organizador2_setup)
image organizador2 desinteresada = At("images/organizador2 desinteresada.png", organizador2_setup)
image organizador2 enojada = At("images/organizador2 enojada.png", organizador2_setup)
image organizador2 entretenida = At("images/organizador2 entretenida.png", organizador2_setup)
image organizador2 sorprendida = At("images/organizador2 sorprendida.png", organizador2_setup)

# Textos

style susurro is text:
    italic True
    size 24
    color "#333"