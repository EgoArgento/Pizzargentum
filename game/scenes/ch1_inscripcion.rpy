image bg ch1 inscripcion = "images/backgrounds/ch1_inscripcion.png"
image black = Solid("#000")

label ch1_inscripcion:
    play music "audio/restaurante.mp3" loop

    scene bg ch1 inscripcion

    show protagonista normal

    protagonista.c "..."

    show organizador1 normal
    organizador1 "¿Si? ¿Se le ofrece algo muchacho?"

    protagonista.c levanta_cejas "¡Y claro! Quiero que me anoten al concurso acá y ahora."
    show organizador2 desinteresada
    organizador2 "Disculpe.. Señor. Como habrá de conocer, la lista de concursantes fue cerrada con dos meses de antelación."

    protagonista.c sorprendido "No, es que no puede ser que yo no esté. "
    organizador1 sorprendido "(... ¿y a este qué le pasa? 🤌🏼🤌🏼🤌🏼🤌🏼)"
    organizador1 "Podriamos entonces revisar la lista de {i}invitados{/i}, señor.."

    $ protagonista.name = renpy.input("Mi nombre???", length=32).strip() or "Vos"

    protagonista.c "¿¿Mi nombre??  {shader=jitter:u__jitter=5.0, 9.0}{color=#103F79}¡EL {color=#DAFF00}MAS{/color} {color=#103F79}GROSOOOO!{/color}{/color}{/shader}"

    organizador2 enojada "Señor, sin su nombre no es posible cerciorarse de-{nw}"

    protagonista.c enojado "¿¿No se dan cuenta de quién soy, no??"
    protagonista.c "(La verdá no entiendo cómo esta gente consiguió un laburo)"

    stop music fadeout 1.0
    play music "audio/dalebo.mp3"
    play sound "audio/bullicio.mp3"

    protagonista.c normal "A ver, a ver, ¿No ven mi delantal?"

    protagonista.c "Está bien, los veo interesados."

    organizador1 "En realidad señor-{nw}"

    protagonista.c enojado " {shader=jitter:u__jitter=5.0, 9.0}SHHHHHhhshHSH.{/shader}"

    protagonista.c normal "Todo comenzó cuando.."

    stop sound
    scene black with dissolve
