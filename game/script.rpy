# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform bit_right:
    right
    xoffset 150

define o1= Character("Organizador 1")
define o2= Character("Organizador 2")
# The game starts here.

label start:
    play music "audio/restaurante.mp3" loop
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pescaracon_placeholder

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    " "
    $ povname = "Vos"
    show protagonista sonriente:
        zoom 0.2
        xoffset -0.2
    V "..."
    show protagonista sonriente at left:
        zoom 0.2
        xoffset -0.2
    show organizador1 default at right:
        zoom 4
        xzoom -1
    o1 "¿Si? ¿Se le ofrece algo muchacho?"
    V "¡Y claro! Quiero que me anoten al concurso acá y ahora."
    show organizador2 default at bit_right:
        zoom 1.5
    o2 "Disculpe.. Señor. Como habrá de conocer, la lista de concursantes fue cerrada con dos meses de antelación."
    show vos delirante:
        zoom 1.25
    V "No, es que no puede ser que yo no esté. "
    o1 "(... ¿y a este qué le pasa? 🤌🏼🤌🏼🤌🏼🤌🏼)"
    o1 "Podriamos entonces revisar la lista de {i}invitados{/i}, señor.."
    $ povname = renpy.input("Mi nombre???", length=32)

    $ povname = povname.strip()

    if not povname:
        $ povname = "Vos"

    V "¿¿Mi nombre??  {shader=jitter:u__jitter=5.0, 9.0}{color=#103F79}¡EL {color=#DAFF00}MAS{/color} {color=#103F79}GROSOOOO!{/color}{/color}{/shader}"

    o2 "Señor, sin su nombre no es posible cerciorarse de-{nw}"

    show vos enojado

    V "¿¿No se dan cuenta de quién soy, no??"
    V "(La verdá no entiendo cómo esta gente consiguió un laburo)"

    show vos sonriente

    V "A ver, a ver, ¿ No ven mi delantal?"
    stop music fadeout 1.0
    play music "dalebo.mp3"
    play sound "bullicio.mp3"



    V "Está bien, los veo interesados."

    o1 "En realidad señor-{nw}"
    show vos enojado
    V " {shader=jitter:u__jitter=5.0, 9.0}SHHHHHhhshHSH.{/shader}"


    show vos sonriente
    V "Todo comenzó cuando.."
    stop sound
    scene black with dissolve
    # show eileen happy

    # These display lines of dialogue.

    #  e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
