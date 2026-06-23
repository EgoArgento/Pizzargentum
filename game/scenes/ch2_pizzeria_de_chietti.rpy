image bg ch2 pizzeria_interior_chieti = "images/backgrounds/ch2_pizzeria_interior_chieti.png"
define abrir_puerta = "audio/sfx/door-open-close-with-bell-96884.ogg"

label ch2_pizzeria_de_chietti:
    centered "Alguna vez en Chietti.\n{i}Un pueblucho muy chiquito para mí.{/i}"

    play music bgm_ch1_2 loop

    scene bg ch2 pizzeria_interior_chieti
    hide screen darkening_overlay with dissolve

    protagonista.c "¡Laburo de @#$\%&!"
    window hide

    play sound abrir_puerta
    pause 2.0

    show protagonista sin_delantal sonriente
    protagonista.c "¿Holaaa?"
    protagonista.c "¿Hay alguien acá?"
    protagonista.c sin_delantal enojado "Loco, ¿nadie labura o qué?"
    protagonista.c sin_delantal incredulo "{=susurro}Me queda poco tiempo de descanso. Si espero mucho y vuelvo tarde me rajan.{/=susurro}"

    menu:
        "Quedarme y... ¿esperar?":
            jump ch2_pizzeria_de_chietti_cont
        "Irme, qué voy a hacer...":
            jump final_malo_1

label ch2_pizzeria_de_chietti_cont:
    protagonista.c sin_delantal incredulo "Que me rajen, una depresión volver sin comer nada. No puede tardar tanto el tanito."

    # FIXME: PLEASE
    "WIP: añadir reloj que muestre que pasan 15 minutos."
    "WIP: Añadir EFECTO de brillo en la puerta de la cocina."

    # TODO: agregar PÍCARO
    protagonista.c sin_delantal sonriente "UHH ¡Durmió!"

    show screen darkening_overlay(0.2)
    pause 0.4

    jump ch3_argentino_que_se_respeta_no_espera_1

label final_malo_1:
    protagonista.c sin_delantal enojado "No sé qué hago acá. No puedo perder el único trabajo que conseguí."

    show screen darkening_overlay(1.0)
    play sound abrir_puerta
    hide protagonista

    pause 2

    centered "FIN"
    return
