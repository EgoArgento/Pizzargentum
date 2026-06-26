
image bg ch5 inscripcion = "images/backgrounds/ch5_inscripcion_tarde.png"
define sfx_recuerdo_finish = "audio/sfx/remembrance-harp-72958-finish.ogg"

label ch5_inscripcion_segunda_vuelta:
    play sound sfx_recuerdo_finish
    centered "Área de recepción a concurso, Pescara, tarde."

    scene bg ch5 inscripcion

    hide screen darkening_overlay with dissolve

    play music bgm_concorso loop
    play ambient sfx_murmuring_crowd volume 0.75 loop

    show protagonista orgulloso
    show organizador1 cansado
    show organizador2 cansada

    protagonista.c "Y así, el tanito reconoció su derrota y me regaló su delantal."
    protagonista.c "¡Y para mejor! Un sastrecito me bordó las palabras. ¡Zarpado, ¿no?!"

    # TODO: agregar organizador2 CONFUNDIDA
    organizador2 confundida "¿Y a qué te refieres con el más ca-{nw}"

    show organizador1 cansado:
        xzoom -1

    organizador1 "{=susurro}No le sigas la corriente, ¡a ver si se queda hablando media hora más!{/=susurro}"

    show organizador1 cansado:
        xzoom 1

    protagonista.c ansioso "¿Y? ¿Me van a anotar, o me van a {b}anotar{/b}?"

    organizador1 "Sí, señor... No se preocupe. Tampoco necesitamos que nos diga su nombre."

    protagonista.c delirante "{=susurro}¡JA! ¡Sabían mi nombre~! ¡Solo querían que les contase YO MÍSMO mí historia!{/=susurro}"

    organizador1 "Al final del pasillo. La competencia debería estar empezando en cualquier momento."

    organizador2 enojada "{=susurro}Perdimos tanto tiempo con este loco...{/=susurro}"

    protagonista.c orgulloso "¡No se diga más! ¡Los voy a recordar cuando me haga famoso!"

    play sound sfx_pasos

    # TODO: agregar organizador1 CONFUNDIDO
    organizador1 confundido "¡Señor! ¡Se olvida las-!{nw}"

    protagonista.c delirante "¡No me extrañen! ¡Les voy a dar un baile a estos y vuelvo!"
    protagonista.c "¡Se los juro por Dieguito!"

    show screen darkening_overlay(1.0)

    jump ch6_1_ravanello_ma_chi_bello