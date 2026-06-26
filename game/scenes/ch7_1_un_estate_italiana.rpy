screen sifonazo_imagen():
    add "protagonista sifon" at wander
    add "protagonista sifon" at wander
    add "protagonista sifon" at wander
    add "protagonista sifon" at wander
    add "protagonista sifon" at wander
    add "protagonista sifon" at wander

label ch7_1_un_estate_italiana:
    $ protagonista.migrar_data()

    protagonista.c confiado "Primero que nada, no sabés a quién te estás enfrentando."

    ravanello confundido "{=susurro}¿¡Mah-?!{/=susurro}"

    protagonista.c sonriente "¡¿Mi pizza favorita?!"

    show screen whitening_overlay(0.2)
    play sound sfx_dramatic_impact volume 3.0
    pause 0.2
    hide screen whitening_overlay

    protagonista.c delirante "{shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}¡¡La O.Gatti!!{/b}{/shader}"

    ravanello asustado "{=susurro}¿QUUUÉEeeeEeEe? ¡Esa no la conozco!{/=susurro}"

    protagonista.c delirante "¡¿Y sabés cual es más grossa todavía?!"

    protagonista.c "{shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}¡¡LA GIANCARLO!!{/b}{/shader}"

    ravanello confundido "{=susurro}No puede ser, ¿tan poco se de pizza?{/=susurro}"

    protagonista.c delirante fortissimo "{b}¡¡¿Y SABÉS CÚAL ES MÁS GRANDE?!!{/b}"

    stop music

    show screen whitening_overlay(0.2)
    play sound sfx_dramatic_impact volume 3.0
    pause 0.3
    hide screen whitening_overlay

    play sound sfx_llorando loop

    ravanello llorando "¡Ya basta, me rindo!"

    stop music fadeout 0.3
    pause 0.3
    play music bgm_concorso loop fadein 0.3

    protagonista.c enojado "{=susurro}¡No me podés cortar a la mitad...! Ya sabía yo que éste era amargo.{/=susurro}"

    stop sound

    ravanello asustado "No sabía que mi ignorancia llegaba a tanto, me disculpo señor."

    protagonista.c confiado "{=susurro}Está bien, lo perdono. Desde el '83 que a  los diablitos no los quiere ni la vieja.{/=susurro}"

    protagonista.c "No te preocupes, pibe. El camino de los grandes no cualquiera lo comprende."

    ravanello llorando "¿Cree usted que lograré alcanzar a Ego algún día?"

    play sound sfx_laughin volume 2.0

    protagonista.c "¡¿A Ego?! ¡JA!"

    stop music fadeout 0.4
    pause 0.4
    play music bgm_dalebo loop fadein 0.4

    protagonista.c delirante "¡A ese {shader=jitter:5.0,9.0}{color=#fff}GA{/color}{color=#f00}LLI{/color}{color=#fff}NA{/color}{/shader} nadie lo juna!"

    ravanello "Pero-{nw}"

    play sound sfx_shh loop

    show screen sifonazo_imagen()
    protagonista.c "{shader=jitter:u__jitter=5.0, 9.0|wave}SHHHHHhhshHSH.{/shader}"
    hide screen sifonazo_imagen
    stop sound

    play sound sfx_pasos_rapidos volume 2.0
    show ravanello:
        xzoom -1
        easein 1.5 xalign 2.0

    protagonista.c "¡Dale! ¡Que pase el que sigue!"

    stop music fadeout 0.4
    pause 0.4

    play music bgm_un_estate_italiana loop fadein 0.5

    $ persistent.complete = True

    show screen darkening_overlay(1.0)
    pause 1.0

    centered "Continuará..."

    return