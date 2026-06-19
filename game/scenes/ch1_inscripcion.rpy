image bg ch1 inscripcion = "images/backgrounds/ch1_inscripcion.png"
image black = Solid("#000")

# TODO: Configurar para que texto baja dentro de caja
# TODO: Configurar colores de org1 org2 characters.

# TODO: usar prota levanta_cejas
# TODO: usar prota sorprendido

label ch1_inscripcion:
    hide screen darkening_overlay

    play music "audio/restaurante.mp3" loop

    scene bg ch1 inscripcion

    show protagonista sonriente

    protagonista.c "{w=0.3}.{w=0.3}.{w=0.3}.{w=0.6} {w=0}¿Y?"

    show organizador1 indiferente
    organizador1 "¿Se le ofrece algo muchacho?"

    protagonista.c "¡Y claro! Quiero que me anoten al concurso. ¡Acá y {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}A H O R A{/b}{/shader}!"

    show organizador2 desinteresada
    organizador2 "Disculpe{w=0.1}.{w=0.1}.{w=0.1}. Señor. Como {b}sabrá{/b}, la lista de concursantes fue cerrada hace dos meses."

    protagonista.c sorprendido "¡Cualquiera! ¡No puede ser que yo no esté!"

    show organizador1 enojado:
        xzoom -1

    organizador1 "{=susurro}¡¿Y a este tío qué le pasa?!{/=susurro} 🤌🏼🤌🏼🤌🏼🤌🏼"

    show organizador2 behind organizador1:
        xoffset -100
    show organizador2 entretenida

    organizador2 "*EHEM* {=susurro}Quien sabe.{/=susurro}"

    show organizador2 desinteresada:
        xoffset 0

    show organizador1 desconfiado:
        xzoom 1

    organizador1 "En-TON-ces podríamos revisar la lista de {b}{w=0.2}in{w=0.2}-vi{w=0.2}-ta{w=0.2}-dos{/b}, ¿¿señorrr...??"

    protagonista.c delirante "¡¿¡¿MÍ autógrafo?!?!"

    $ protagonista.name = renpy.input("{color=#111}Escribí tu autógrafo:{/color}", length=32).strip() or "Vos"

    protagonista.c "{shader=jitter:u__jitter=5.0, 9.0}{color=#103F79}¡EL {color=#DAFF00}MAS{/color} {color=#103F79}GROSOOOO!{/color}{/color}{/shader}"

    show organizador1 behind organizador2

    # TODO: hacer que el diálogo sea más lento pero que siga
    # cortándose a la fuerza
    organizador2 enojada "Señor {shader=wave}{i}eL mÁs GrOsO{/i}{/shader}{w=0.4}, sin su nombre no es posible cerciorarse de-{w=0.2}{nw}"

    protagonista.c enojado "¿¿Posta no se dan cuenta de quién soy??"

    protagonista.c incredulo "{=susurro}La verdad que no entiendo cómo esta gente consiguió laburo.{/=susurro}"

    play sound "audio/sfx/record_scratch-108233.mp3"
    stop music

    show organizador2 behind organizador1
    show organizador2 sorprendida
    show organizador1 sorprendido:
        xzoom -1

    pause 2.0

    show organizador2 enojada
    show organizador1 enojado:
        xzoom 1

    organizador1y2 "Perdón, ¿qué has dicho?"

    protagonista.c sonriente "A ver, a ver, ¿No ven mi delantal?"

    play music "audio/dalebo.mp3"
    play sound "audio/sfx/bullicio.mp3"

    protagonista.c "¡No se diga más! El pueblo me llama, siéntense los de la galera y escuchen esta osada historia."

    organizador1 "En realidad señor-{nw}"

    protagonista.c enojado " {shader=jitter:u__jitter=5.0, 9.0|wave}SHHHHHhhshHSH.{/shader}"

    protagonista.c sonriente "Todo comenzó cuando..."

    stop sound
    stop music fadeout 3.0
    show screen darkening_overlay(3.0)

    hide protagonista

    show organizador1 indiferente:
        xzoom -1
        xoffset -700
    show organizador2 desinteresada:
        xoffset -600

    organizador2 "{=susurro}No nos pagan lo suficiente como para resolver esto.{/=susurro}{nw}"

    window hide
    hide organizador1
    hide organizador2

    pause 1.0

    jump ch2_pizzeria_de_chietti
