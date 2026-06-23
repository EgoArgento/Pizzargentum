image bg ch3 pizzeria_cocina_chieti = "images/backgrounds/ch3_pizzeria_cocina_chieti.png"

define bgm_ch3 = "audio/pizzatron_3000.ogg"

label ch3_argentino_que_se_respeta_no_espera_1:
    scene bg ch3 pizzeria_cocina_chieti
    hide screen darkening_overlay with dissolve

    show protagonista sin_delantal sorprendido

    protagonista.c "¿Y esto? ¿Se dejó media pizza?"
    # TODO: agregar PÍCARO
    protagonista.c sin_delantal sonriente "¡Matanga! Alguien la tiene que aprovechar."
    protagonista.c sin_delantal enojado "¡Pará! ¡Pero esto sigue crudo! ¡Nunca una bien!"
    protagonista.c sin_delantal incredulo "¡Uff! ¡Le tengo que meter pata y comerla antes de que llegue el tanito!"
    protagonista.c sin_delantal delirante "No puede ser muy difícil esto. A ver..."

    $ protagonista.migrar_data()

    play music bgm_ch3 loop

    # Empieza minijuego
    show protagonista sin_delantal sonriente

    jump ch3_minijuego_pizza_1

label ch3_minijuego_pizza_1:
    show screen timed_choice(3.0, Jump("final_malo_2"))

    menu:
        protagonista.c sin_delantal sonriente "¿Qué puedo hacer con esta pizza?"

        "Colorcarle tomate" if "tomate" not in protagonista.ch3_minijuego_seleccion:
            hide screen timed_choice
            $ protagonista.ch3_karma -= 5
            $ protagonista.ch3_minijuego_seleccion.append("tomate")
            protagonista.c sin_delantal sonriente "Creo que esto llevaba tomate, ¿no?"
            if len(protagonista.ch3_minijuego_seleccion) < 2:
                jump ch3_minijuego_pizza_1
            else:
                jump ch3_minijuego_pizza_2

        "Colocarle ananá" if "anana" not in protagonista.ch3_minijuego_seleccion:
            hide screen timed_choice
            $ protagonista.ch3_karma += 5
            $ protagonista.ch3_minijuego_seleccion.append("anana")
            protagonista.c sin_delantal sonriente "¡APA! ¿¿Y esto??"
            if len(protagonista.ch3_minijuego_seleccion) < 2:
                jump ch3_minijuego_pizza_1
            else:
                jump ch3_minijuego_pizza_2

        "Colocarle anchoas" if "anchoas" not in protagonista.ch3_minijuego_seleccion:
            hide screen timed_choice
            $ protagonista.ch3_karma += 5
            $ protagonista.ch3_minijuego_seleccion.append("anchoas")
            protagonista.c sin_delantal sonriente "Uuuuh, esto tiene pinta de que es caro... Mejor aprovecho."
            if len(protagonista.ch3_minijuego_seleccion) < 2:
                jump ch3_minijuego_pizza_1
            else:
                jump ch3_minijuego_pizza_2

        "Colocarle queso" if "queso" not in protagonista.ch3_minijuego_seleccion:
            hide screen timed_choice
            $ protagonista.ch3_karma -= 5
            $ protagonista.ch3_minijuego_seleccion.append("queso")
            protagonista.c sin_delantal sonriente "Esto más o menos tiene pinta de muzza."
            if len(protagonista.ch3_minijuego_seleccion) < 2:
                jump ch3_minijuego_pizza_1
            else:
                jump ch3_minijuego_pizza_2

label ch3_minijuego_pizza_2:
    if "anana" in protagonista.ch3_minijuego_seleccion and "anchoas" in protagonista.ch3_minijuego_seleccion:
        protagonista.c sin_delantal delirante "¡A ESTO LE PONÉS SALSA CRIOLLA Y QUEDA JOYA!"

    show screen timed_choice(3.0, Jump("final_malo_2"))

    menu:
        protagonista.c sin_delantal sonriente "¿Cómo termino la pizza?"

        "Meter la pizza al horno":
            hide screen timed_choice
            $ protagonista.ch3_karma -= 5
            protagonista.c sin_delantal sonriente "¡Ahí va! Estaba medio paliducha."
            jump ch3_argentino_que_se_respeta_no_espera_2

        "Darle un besito para la buena suerte":
            hide screen timed_choice
            $ protagonista.ch3_karma += 5
            # TODO: agregar SFX de muak
            protagonista.c sin_delantal sonriente "*muak* ¡Grosa como {b}papáaa{/b}!"
            jump ch3_argentino_que_se_respeta_no_espera_2

label ch3_argentino_que_se_respeta_no_espera_2:
    if protagonista.ch3_karma == -15:
        jump final_malo_2

    show screen darkening_overlay(0.2)

    centered "Continuará."

    return

label final_malo_2:
    # WIP

    centered "FIN"
    return