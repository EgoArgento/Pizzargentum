image bg ch1 inscripcion = "images/backgrounds/ch1_inscripcion.png"
image black = Solid("#000")

# TODO:caja de pizza de diálogo

label ch1_inscripcion:
    play music "audio/restaurante.mp3" loop

    scene bg ch1 inscripcion

    show protagonista sonriente

    protagonista.c "{w=0.3}.{w=0.3}.{w=0.3}.{w=0.6} {w=0}¿Y?"

    show organizador1 indiferente
    organizador1 "¿Se le ofrece algo muchacho?"

    protagonista.c "¡Y claro! Quiero que me anoten al concurso. ¡Acá y {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}A H O R A{/b}{/shader}!"

    show organizador2 entretenida
    organizador2 "Disculpe{w=0.1}.{w=0.1}.{w=0.1}. Señor. Como {b}sabrá{/b}, la lista de concursantes fue cerrada hace dos meses."

    # TODO: agregar protagonista DELIRANTE
    protagonista.c sorprendido "¡Cualquiera! ¡No puede ser que yo no esté!"

    # TODO: agregar organizador1 FASTIDIADO
    show organizador1 sorprendido:
        xzoom -1

    organizador1 "{=susurro}¡¿Y a este tío qué le pasa?!{/=susurro} 🤌🏼🤌🏼🤌🏼🤌🏼"

    show organizador2 behind organizador1:
        xoffset -100

    organizador2 "*EHEM* {=susurro}Quien sabe.{/=susurro}"

    show organizador2:
        xoffset 0

    # TODO: Agregar organizador1 CONDESCENDIENTE
    show organizador1 indiferente:
        xzoom 1

    organizador1 "En-TON-ces podríamos revisar la lista de {b}{w=0.2}in{w=0.2}-vi{w=0.2}-ta{w=0.2}-dos{/b}, ¿¿señorrr...??"

    # TODO: agregar protagonista DELIRANTE
    protagonista.c sorprendido "¡¿¡¿MÍ autógrafo?!?!"

    $ protagonista.name = renpy.input("{color=#111}Escribí tu autógrafo:{/color}", length=32).strip() or "Vos"

    protagonista.c "{shader=jitter:u__jitter=5.0, 9.0}{color=#103F79}¡EL {color=#DAFF00}MAS{/color} {color=#103F79}GROSOOOO!{/color}{/color}{/shader}"

    show organizador1 behind organizador2

    # TODO: hacer que el diálogo sea más lento pero que siga
    # cortándose a la fuerza
    organizador2 enojada "Señor {shader=wave}{i}eL mÁs GrOsO{/i}{/shader}, sin su nombre no es posible cerciorarse de-{nw}"

    protagonista.c enojado "¿¿Posta no se dan cuenta de quién soy??"

    show organizador2 behind organizador1
    show organizador1 sorprendido:
        xzoom -1

    protagonista.c "{=susurro}La verdad que no entiendo cómo esta gente consiguió laburo.{/=susurro}"

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
