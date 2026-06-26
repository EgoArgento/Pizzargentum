define sfx_portazo = "audio/sfx/door-closed-hardly-7041.ogg"
define sfx_rasgar_tela = "audio/sfx/cloth_rippingwav-14481.ogg"

define bgm_ch4_7_merry_cherry = "audio/anystyle-merry-cherry-175063.ogg"

label ch4_1_el_nacimiento_del_dios_de_la_pizza:
    if protagonista.ch3_karma == -15:
        jump ch4_2_la_vieja_confiable_fallo

    protagonista.c sin_delantal orgulloso "Casi que me da pena comerla..."
    play sound sfx_masticar
    protagonista.c sin_delantal pensante con_pizza "*Crunch crunch* *ñom ñom*..."
    protagonista.c sin_delantal delirante "NAAA, ¡SOY UN GROSOOOOO!"

    play sound sfx_portazo volume 2.0

    play music bgm_ch4_7_merry_cherry loop

    show cocinero enojado

    cocinero "¿Y usted quién es? ¡¿Qué hace acá?!"

    protagonista.c "Taniiito, ¡ya tardabas mucho!"

    cocinero "¿Pero qué dice? SALGA AHORA MISMO DE MI COCINA."

    protagonista.c "Veníii, te dejo mirar nomás porque sos vos."

    cocinero "PERO-{nw}"

    # TODO: las letras en pantalla se mueven fuera del cajón de diálogo.
    play sound sfx_shh
    protagonista.c "SHHHHHhhshHSH..."

    protagonista.c "Mirá... ¡TREMENDA!, ¿no?"

    cocinero aterrado "¿¿Pero qué hizo??"

    protagonista.c sin_delantal delirante fortissimo "¡Otra coronación de gloria!"

    cocinero enojado "¡LE PIDO QUE SE VAYA O VOY A TENER QUE LLAMAR A LA POLICÍA!"

    protagonista.c "¡Vení para acá y dame eso!"

    show protagonista sin_delantal delirante:
        xalign 0.0
        easein 0.5 xalign 0.85

    pause 0.5

    show protagonista sin_delantal delirante:
        xzoom 1
        xalign 0.85
        linear 0.2 xalign 1.0
        pause 0.1
        xzoom -1
        linear 0.2 xalign 0.85
        pause 0.1
        repeat

    show cocinero behind protagonista:
        xzoom 1
        xalign 1.0
        linear 0.2 xalign 0.85 yalign 0.6
        pause 0.1
        xzoom -1
        linear 0.2 xalign 1.0 yalign 1.0
        pause 0.1
        repeat

    pause 0.5

    show cocinero llorando:
        xzoom 1
        xalign 1.0
        linear 0.2 xalign 0.85 yalign 0.6
        pause 0.1
        xzoom -1
        linear 0.2 xalign 1.0 yalign 1.0
        pause 0.1
        repeat

    pause 0.5

    play sound sfx_rasgar_tela volume 2.0
    pause 1.0

    show protagonista delirante:
        xzoom 1
        xalign 0.85
        easein 0.5 xalign 0

    show cocinero sin_delantal llorando:
        xzoom 1
        easein 0.2 xalign 1.0 yalign 1.0

    cocinero "¿PERO QUÉ HACE?"

    protagonista.c delirante "¿Qué hago? ¿QUE QUÉ HAGO? {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}JAJAJAJA{/b}{/shader}"

    protagonista.c delirante fortissimo "¡VOY A CONVERTIRME EN EL MEJOR CHEF DE PIZZA!"

    protagonista.c "¡EL CAPO DE LA PIZZA!"

    stop sound fadeout 1.0
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    show screen darkening_overlay(1.0)

    pause 1.0

    jump ch5_inscripcion_segunda_vuelta
