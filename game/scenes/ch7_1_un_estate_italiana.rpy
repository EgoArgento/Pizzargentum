
label ch7_1_un_estate_italiana:
    $ protagonista.migrar_data()

    protagonista.c confiado "Primero que nada, no sabés a quién te estás enfrentando."

    ravanello confundido "{=susurro}¿¡Mah-?!{/=susurro}"

    # TODO: fix
    "Se hace un pequeño acercamiento a la escena con un flash blanco."

    protagonista.c "¡¿Mi pizza favorita? {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}¡¡La O.Gatti!!{/b}{/shader}"

    ravanello "{=susurro}¿QUUUÉEeeeEeEe? ¡Esa no la conozco!{/=susurro}"

    # TODO: fix
    "La cámara se acerca más. Comienza a sonar un temporizador."

    protagonista.c delirante "¡¿Y sabés cual es más grossa todavía?! {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}¡¡LA GIANCARLO!!{/b}{/shader}"

    # TODO: fix
    "La cámara se acerca y aleja. El texto '¡¡LA GIANCARLO!!' se sacude en pantalla. Luego, la cámara se acerca a Ravanello."

    ravanello asustado "{=susurro}No puede ser, ¿tan poco se de pizza?{/=susurro}"

    # TODO: fix
    "La cámara se acerca al PROTAGONISTA."

    protagonista.c delirante fortissimo "{b}¡¡¿Y SABÉS CÚAL ES MÁS GRANDE?!!{/b}"

    # TODO: fix
    "La pantalla se sacude mientras el protagonista habla. La cámara se acerca a Ravanello. Un vidrio no diegético se rompe. La música se corta. El temporizador termina con un *RIIING*."

    ravanello llorando "¡Ya basta, me rindo!"

    # TODO: fix
    "Se escucha el llanto de Ravanello."

    stop music fadeout 0.3
    pause 0.3
    play music bgm_concorso loop fadein 0.3

    protagonista.c enojado "{=susurro}¡No me podés cortar a la mitad...! Ya sabía yo que éste era amargo.{/=susurro}"

    ravanello asustado "No sabía que mi ignorancia llegaba a tanto, me disculpo señor."

    protagonista.c confiado "{=susurro}Está bien, lo perdono. Desde el '83 que a  los diablitos no los quiere ni la vieja.{/=susurro}"

    protagonista.c "No te preocupes, pibe. El camino de los grandes no cualquiera lo comprende."

    ravanello llorando "¿Cree usted que lograré alcanzar a Ego algún día?"

    play sound sfx_laughin volume 2.0

    protagonista.c "¡¿A Ego?! ¡JA!"

    stop music fadeout 0.4
    pause 0.4
    play music bgm_dalebo loop fadein 0.4

    protagonista.c delirante "¡A ese GALLINA nadie lo juna!"
    # TODO: fix
    "El texto 'gallina' se sacude con los colores de River Plate."

    ravanello "Pero-{nw}"

    protagonista.c "¡Pero nada!"
    protagonista.c "¡Dale! ¡Que pase el que sigue!"

    stop music fadeout 0.4
    pause 0.4

    play music bgm_un_estate_italiana loop fadein 0.5

    $ persistent.complete = True

    show screen darkening_overlay(1.0)
    pause 1.0

    centered "Continuará..."

    return