image bg ch3 pizzeria_cocina_chieti = "images/backgrounds/ch3_pizzeria_cocina_chieti.png"

label ch3_argentino_que_se_respeta_no_espera:
    scene bg ch3 pizzeria_cocina_chieti
    hide screen darkening_overlay with dissolve

    show protagonista sin_delantal sorprendido

    protagonista.c "¿Y esto? ¿Se dejó media pizza?"
    # TODO: agregar PÍCARO
    protagonista.c sin_delantal sonriente "¡Matanga! Alguien tiene que aprovechar."
    protagonista.c sin_delantal enojado "¡Pará! ¡Pero esto sigue crudo! ¡Nunca una bien!"