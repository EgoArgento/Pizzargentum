image bg ch6 centro = "images/backgrounds/ch6_centro_convenciones_tarde.png"


label ch6_1_ravanello_ma_chi_bello:
    centered "Centro de convenciones, Pescara, tarde."

    scene bg ch6 centro

    play music bgm_ch1_2 loop
    play ambient sfx_murmuring_crowd volume 0.75 loop
    hide screen darkening_overlay with dissolve

    show protagonista sonriente:
        xalign -0.5
        easein 2.0 xalign 0.0

    pause 2.0

    # TODO: agregar IMPACIENTE
    protagonista.c impaciente "Bueno, bueno ¡¿cuándo empieza esto?!"

    pause 2.0

    show ravanello desafiante with dissolve

    pause 1.0

    protagonista.c sonriente "¡CHE VOS! ¡El amargo del rojo!"

    ravanello confundido "¿Me hablas a mí?"

    protagonista.c "Y sí máquina. ¡¿VOS vas a ser mi rival?!"

    "WIP: SFX de risa atragantada."

    ravanello enojado "No entiendo. ¿Quién eres?, ¿¿cuál es tu problema??"

    "WIP: agregar música de combate"
    stop ambient

    ravanello "No importa, si quieres ganar el concurso, deberás ganarme a mí primero."

    "WIP Agregar VFX de inicio de combate"

    # TODO: Agregar protagonista confiado
    show protagonista confiado
    show ravanello confiado

    "WIP: agregar SFX de risas para prota, ¿y para ravanello?"

    protagonista.c picaro "¡Daaalee, ponele primera!"

    "Suena bocina de conteo. Se muestra en pantalla '3, 2, 1' Y una última bocina acentúa el final."

    # TODO: ravanello entusiasmado
    ravanello entusiasmado "Como retador, ¡deberás responder una pregunta!"

    "El protagonista ríe confiado por lo bajo."

    protagonista.c "{=susurro}¡Papita pa'l loro!{/=susurro}"

    ravanello confiado "¿Cuántos tipos de pizza conoces?"

    "La cámara se acerca y aleja. Se ve un breve flash blanco. Se escucha un sonido dramático."

    ravanello "¡Nómbralos todos!"

    # TODO: agregar confundido
    protagonista.c confundido "{=susurro}¿Quuuuéeeeeeeeeeeeeeeee?{/=susurro}"

    "Aparece en pantalla un contador de tiempo restante. La música cambia a Acid jazz, similar a 'Discussion -HEAT UP-'."

    ravanello "¡Vamos cocinerito!"

    protagonista.c enojado "{=susurro}Este gil no me va a ganar.{/=susurro}"

    show screen timed_choice(
        t=3.0,
        action=Jump("ch4_2_la_vieja_confiable_fallo")
    )

    menu:
        # TODO: agregar PREOCUPADO
        protagonista.c preocupado "{=susurro}¿Qué puedo hacer?{/=susurro}"

        "Nombrar Pizzas":
            jump ch6_2_siamo_fuori
        "Nombrar el plantel de Boquita del '77":
            jump ch6_1_ravanello_ma_chi_bello_2

label ch6_1_ravanello_ma_chi_bello_2:
    # TODO: agregar confiado
    protagonista.c confiado "Primero que nada, no sabés a quién te estás enfrentando."

    ravanello confundido "{=susurro}¿¡Mah-?!{/=susurro}"

    "Se hace un pequeño acercamiento a la escena con un flash blanco."

    protagonista.c "¡¿Mi pizza favorita? {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}¡¡La O.Gatti!!{/b}{/shader}"

    ravanello "{=susurro}¿QUUUÉEeeeEeEe? ¡Esa no la conozco!{/=susurro}"

    "La cámara se acerca más. Comienza a sonar un temporizador."

    protagonista.c delirante "¡¿Y sabés cual es más grossa todavía?! {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}¡¡LA GIANCARLO!!{/b}{/shader}"

    "La cámara se acerca y aleja. El texto '¡¡LA GIANCARLO!!' se sacude en pantalla. Luego, la cámara se acerca a Ravanello."

    # TODO: agregar ravanello asustado
    ravanello asustado "{=susurro}No puede ser, ¿tan poco se de pizza?{/=susurro}"

    "La cámara se acerca al PROTAGONISTA."

    # TODO: VFX fortíssimo
    protagonista.c "{b}¡¡¿Y SABÉS CÚAL ES MÁS GRANDE?!!{/b}"

    "La pantalla se sacude mientras el protagonista habla. La cámara se acerca a Ravanello. Un vidrio no diegético se rompe. La música se corta. El temporizador termina con un *RIIING*."

    ravanello llorando "¡Ya basta, me rindo!"

    "Se escucha el llanto de Ravanello. Retoma la música tranquila anterior."

    protagonista.c enojado "{=susurro}¡No me podés cortar a la mitad...! Ya sabía yo que éste era amargo.{/=susurro}"

    ravanello asustado "No sabía que mi ignorancia llegaba a tanto, me disculpo señor."

    protagonista.c confiado "{=susurro}Está bien, lo perdono. Desde el '83 que a  los diablitos no los quiere ni la vieja.{/=susurro}"

    protagonista.c "No te preocupes, pibe. El camino de los grandes no cualquiera lo comprende."

    ravanello llorando "¿Cree usted que lograré alcanzar a Ego algún día?"

    protagonista.c "¡¿A Ego?! ¡JA!"

    "El protagonista se ríe."

    protagonista.c delirante "¡A ese gallina nadie lo juna!"

    "El texto 'gallina' se sacude con los colores de River Plate. La música cambia a 'Dale, Dale Boca'."

    ravanello "Pero-{nw}"

    protagonista.c "¡Pero nada!"
    protagonista.c "¡Dale! ¡Que pase el que sigue!"

    pause

    show screen darkening_overlay(1.0)
    pause 1.0

    centered "Continuará"

    return