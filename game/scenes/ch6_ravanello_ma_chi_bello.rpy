image bg ch6 centro = "images/backgrounds/ch6_centro_convenciones_tarde.png"
image vfx_time_counter = Movie(play="videos/time_counter.webm", mask="videos/time_counter_alpha.webm")

define bgm_ch6_combat = "audio/fassounds-funny-comedy-playful-music-179002.mp3"

label ch6_ravanello_ma_chi_bello:
    centered "Centro de convenciones, Pescara, tarde."

    scene bg ch6 centro

    play music bgm_concorso loop
    play ambient sfx_murmuring_crowd volume 0.75 loop
    hide screen darkening_overlay with dissolve

    show protagonista sonriente:
        xalign -0.5
        easein 2.0 xalign 0.0

    pause 2.0

    protagonista.c ansioso "Bueno, bueno ¡¿cuándo empieza esto?!"

    pause 2.0

    show ravanello desafiante with dissolve

    pause 1.0

    protagonista.c sonriente "¡CHE VOS! ¡El amargo del rojo!"

    ravanello confundido "¿Me hablas a mí?"

    protagonista.c "Y sí máquina..."

    play sound sfx_laughin_coughin volume 2.0

    protagonista.c ansioso "¡¿VOS vas a ser mi rival?!"

    ravanello enojado "No entiendo. ¿Quién eres?, ¿¿cuál es tu problema??"

    play music bgm_ch6_combat loop
    stop ambient

    ravanello "No importa, si quieres ganar el concurso, deberás ganarme a mí primero."

    # TODO: fix
    "WIP Agregar VFX de inicio de combate"

    show protagonista confiado
    show ravanello confiado

    # TODO: fix
    "WIP: agregar SFX de risas para prota, ¿y para ravanello?"

    protagonista.c picaro "¡Daaalee, ponele primera!"

    show vfx_time_counter

    pause 4.0

    hide vfx_time_counter

    ravanello entusiasmado "Como retador, ¡deberás responder una pregunta!"

    # TODO: fix
    "El protagonista ríe confiado por lo bajo."

    protagonista.c "{=susurro}¡Papita pa'l loro!{/=susurro}"

    ravanello confiado "¿Cuántos tipos de pizza conoces?"

    # TODO: fix
    "La cámara se acerca y aleja. Se ve un breve flash blanco. Se escucha un sonido dramático."

    ravanello "¡Nómbralos todos!"

    protagonista.c confundido "{=susurro}¿Quuuuéeeeeeeeeeeeeeeee?{/=susurro}"

    ravanello "¡Vamos cocinerito!"

    protagonista.c enojado "{=susurro}Este gil no me va a ganar.{/=susurro}"

    show screen timed_choice(
        t=10.0,
        action=Jump("ch7_2_siamo_fuori")
    )

    menu:
        protagonista.c preocupado "{=susurro}¿Qué puedo hacer?{/=susurro}"

        "Nombrar Pizzas":
            hide screen timed_choice
            jump ch7_2_siamo_fuori
        "Nombrar el plantel de Boquita del '77":
            hide screen timed_choice
            jump ch7_1_un_estate_italiana
