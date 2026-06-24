
label ch3_2_la_fortuna_no_favorece_a_quienes_esperan:
    play ambient reloj_tictac

    pause 3.0

    stop ambient

    protagonista.c sin_delantal enojado "No sé qué hago acá. No puedo perder el único trabajo que conseguí."

    show protagonista sin_delantal enojado:
        xzoom -1
        easein 1.5 xalign -1.0
    pause 1.0
    show screen darkening_overlay(1.0)
    play sound abrir_puerta

    pause 2

    centered "FIN"
    return
