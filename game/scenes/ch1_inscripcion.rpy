
label ch1_inscripcion:    
    play music "audio/restaurante.mp3" loop
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pescaracon_placeholder

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show protagonista normal
    protagonista.c "..."
    show organizador1 normal at right:
        zoom 4
        xzoom -1
    organizador1 "¿Si? ¿Se le ofrece algo muchacho?"
    protagonista.c levanta_cejas "¡Y claro! Quiero que me anoten al concurso acá y ahora."
    show organizador2 normal at bit_right:
        zoom 1.5
    o2 "Disculpe.. Señor. Como habrá de conocer, la lista de concursantes fue cerrada con dos meses de antelación."
    show protagonista sorprendido:
        zoom 1.25
    protagonista.c "No, es que no puede ser que yo no esté. "
    o1 "(... ¿y a este qué le pasa? 🤌🏼🤌🏼🤌🏼🤌🏼)"
    o1 "Podriamos entonces revisar la lista de {i}invitados{/i}, señor.."
    
    $ protagonista.name = renpy.input("Mi nombre???", length=32).strip() or "Vos"

    protagonista.c "¿¿Mi nombre??  {shader=jitter:u__jitter=5.0, 9.0}{color=#103F79}¡EL {color=#DAFF00}MAS{/color} {color=#103F79}GROSOOOO!{/color}{/color}{/shader}"

    o2 "Señor, sin su nombre no es posible cerciorarse de-{nw}"

    protagonista.c enojado "¿¿No se dan cuenta de quién soy, no??"
    protagonista.c "(La verdá no entiendo cómo esta gente consiguió un laburo)"

    show vos sonriente

    protagonista.c "A ver, a ver, ¿ No ven mi delantal?"
    stop music fadeout 1.0
    play music "dalebo.mp3"
    play sound "bullicio.mp3"



    protagonista.c "Está bien, los veo interesados."

    o1 "En realidad señor-{nw}"
    show vos enojado
    protagonista.c " {shader=jitter:u__jitter=5.0, 9.0}SHHHHHhhshHSH.{/shader}"


    show vos sonriente
    protagonista.c "Todo comenzó cuando.."
    stop sound
    scene black with dissolve
    # show eileen happy

    # These display lines of dialogue.

    #  e "You've created a new Ren'Py game."

    return
