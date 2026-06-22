image bg ch1 inscripcion = "images/backgrounds/ch1_inscripcion.png"

define bgm_ch1 = "audio/restaurante.mp3"
define bgm_dalebo = "audio/dalebo.mp3"
define sfx_crickets = "audio/sfx/felix_quinol-cricket-sound-113945.ogg"
define sfx_bullicio = "audio/sfx/bullicio.ogg"
define sfx_murmuring_crowd = "audio/sfx/happy-crowd-at-interval-23485.ogg"
define sfx_record_scratch = "audio/sfx/record_scratch-108233.ogg"

# TODO: Configurar para que texto baja dentro de caja
# TODO: Configurar colores de org1 org2 characters.

label ch1_inscripcion:
    hide screen darkening_overlay

    play music bgm_ch1 loop
    play ambient sfx_murmuring_crowd volume 0.75

    scene bg ch1 inscripcion

    # TODO: mover de izq a dcha?
    show protagonista sonriente:
        xalign -0.5
        easein 1 xalign 0.0
    window show

    pause 2.0

    $ renpy.music.set_volume(volume=0.3, delay=3.0)
    stop sound fadeout 0.3
    pause 0.3
    play ambient sfx_crickets volume 0.3

    protagonista.c "..."

    pause 1.0
    play ambient sfx_crickets volume 1

    protagonista.c incredulo "........."

    pause 1.0
    play ambient sfx_crickets volume 2
    play sound sfx_protagonista_tsk volume 2

    protagonista.c enojado "......... ¿Y?"

    stop sound
    $ renpy.music.set_volume(0.7, delay=1.0)
    play ambient sfx_murmuring_crowd volume 0.25

    show organizador1 indiferente
    play sound sfx_organizador1_hmm volume 1.5
    organizador1 "¿Se le ofrece algo muchacho?"

    protagonista.c sonriente "¡Y claro! Quiero que me anoten al concurso. ¡Acá y {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}A H O R A{/b}{/shader}!"

    show organizador2 desinteresada
    organizador2 "Disculpe{w=0.1}.{w=0.1}.{w=0.1}. Señor. Como {b}sabrá{/b}, la lista de concursantes fue cerrada hace dos meses."

    protagonista.c sorprendido "¡Cualquiera! ¡No puede ser que yo no esté!"

    show organizador1 enojado:
        xzoom -1

    play sound sfx_organizador1_huh
    organizador1 "{=susurro}¡¿Y a este tío qué le pasa?!{/=susurro} 🤌🏼🤌🏼🤌🏼🤌🏼"

    show organizador2 behind organizador1:
        xoffset -100
    show organizador2 entretenida

    play sound sfx_organizador2_ehem
    organizador2 "{=susurro}{i}*ehem*{/i} Quién sabe...{/=susurro}"

    show organizador2 desinteresada:
        xoffset 0

    show organizador1 desconfiado:
        xzoom 1

    organizador1 "En-TON-ces podríamos revisar la lista de {b}{w=0.2}in{w=0.2}-vi{w=0.2}-ta{w=0.2}-dos{/b}, ¿¿señorrr...??"

    protagonista.c delirante "¡¡Obvio que te doy MÍ autógrafo!!"

    $ protagonista.name = renpy.input("{color=#111}Escribí tu autógrafo:{/color}", length=32).strip() or "Vos"

    protagonista.c "{shader=jitter:u__jitter=5.0, 9.0}{color=#103F79}¡EL {color=#DAFF00}MAS{/color} {color=#103F79}GROSOOOO!{/color}{/color}{/shader}"

    show organizador1 behind organizador2

    # TODO: hacer que el diálogo sea más lento pero que siga
    # cortándose a la fuerza
    organizador2 enojada "Señor {shader=wave}{i}eL mÁs GrOsO{/i}{/shader}{w=0.4}, sin su nombre no es posible cerciorarse de-{w=0.2}{nw}"

    protagonista.c enojado "¿¿Posta no se dan cuenta de quién soy??"

    protagonista.c incredulo "{=susurro}La verdad que no entiendo cómo esta gente consiguió laburo.{/=susurro}"

    stop music
    play sound sfx_record_scratch

    show organizador2 behind organizador1
    show organizador2 sorprendida
    show organizador1 sorprendido:
        xzoom -1

    pause 2.0

    show organizador2 enojada
    show organizador1 enojado:
        xzoom 1

    organizador1y2 "Perdón, ¿qué has dicho?"

    protagonista.c sonriente "A ver, a ver, ¿no ven mi delantal?"

    show delantal primer plano
    window hide

    play music bgm_dalebo
    play sound sfx_bullicio

    pause

    window show

    hide delantal

    protagonista.c "¡No se diga más! El pueblo me llama, siéntense los de la galera y escuchen esta osada historia."

    organizador1 "En realidad señor-{nw}"

    protagonista.c enojado " {shader=jitter:u__jitter=5.0, 9.0|wave}SHHHHHhhshHSH.{/shader}"

    protagonista.c sonriente "Todo comenzó cuando..."

    stop sound fadeout 5.0
    stop ambient fadeout 5.0
    stop music fadeout 5.0
    show screen darkening_overlay(7.0)

    hide protagonista

    show organizador1 cansado:
        xzoom -1
        xoffset -700
    show organizador2 cansada:
        xoffset -600

    organizador2 "{=susurro}No nos pagan lo suficiente como para resolver esto.{/=susurro}{w=5}{nw}"

    window hide
    hide organizador1
    hide organizador2

    pause 1.0

    jump ch2_pizzeria_de_chietti
