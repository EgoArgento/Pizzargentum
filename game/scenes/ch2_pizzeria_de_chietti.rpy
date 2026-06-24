image bg ch2 pizzeria_interior_chieti = "images/backgrounds/ch2_pizzeria_interior_chieti.png"
define abrir_puerta = "audio/sfx/door-open-close-with-bell-96884.ogg"
define reloj_tictac = "audio/sfx/clock-tick-tik-tak-76043.ogg"

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

    show screen timed_choice(3.0, Jump("ch3_2_la_fortuna_no_favorece_a_quienes_esperan"))

    menu:
        "Quedarme y... ¿esperar?":
            hide screen timed_choice
            jump ch3_2_la_fortuna_no_favorece_a_quienes_esperan
        "Campeón que se respeta no espera":
            hide screen timed_choice
            jump ch2_pizzeria_de_chietti_cont

label ch2_pizzeria_de_chietti_cont:
    protagonista.c sin_delantal incredulo "Que me rajen, una depresión volver sin comer nada."

    # FIXME: Pícaro
    protagonista.c sin_delantal sonriente "¡A ver esa cocinaaa!"

    show protagonista sin_delantal sonriente:
        linear 1.5 xalign 1.0 zoom 0.6 yalign 0.3

    pause 2.0

    # TODO: agregar PREOCUPADO
    protagonista.c sin_delantal incredulo "¿Holaa?"

    # TODO: agregar PÍCARO
    protagonista.c sin_delantal delirante "UHH ¡Durmió!"

    jump ch3_1_argentino_que_se_respeta_no_espera
