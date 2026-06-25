
label ch4_1_el_nacimiento_del_dios_de_la_pizza:
    if protagonista.ch3_karma == -15:
        jump ch4_2_la_vieja_confiable_fallo

    # TODO: agregar ORGULLOSO
    protagonista.c "Casi que me da pena comerla..."
    # TODO: agregar PENSANTE
    protagonista.c "*Crunch crunch*..."
    protagonista.c sin_delantal delirante "NAAA, ¡SOY UN GROSOOOOO!"

    "WIP SFX Portazo fuerte"
    "WIP Música chistosa y frenética (khe)"

    show cocinero enojado

    cocinero "¿Y usted quién es? ¡¿Qué hace acá?!"

    protagonista.c "Taniiito, ¡ya tardabas mucho!"

    cocinero "¿Pero qué dice? SALGA AHORA MISMO DE MI COCINA."

    protagonista.c "Veníii, te dejo mirar nomás porque sos vos."

    cocinero "PERO-{nw}"

    # Suenan sonidos de sifones, las letras en pantalla se mueven fuera del cajón de diálogo.
    protagonista.c "SHHHHHhhshHSH..."

    protagonista.c "Mirá... ¡TREMENDA!, ¿no?"

    cocinero aterrado "¿¿Pero qué hizo??"

    ## TODO: DELIRANTE fortíssimo. Cómo?
    protagonista.c "¡Otra coronación de gloria!"

    cocinero enojado "¡LE PIDO QUE SE VAYA O VOY A TENER QUE LLAMAR A LA POLICÍA!"

    protagonista.c "¡Vení para acá y dame eso!"

    "WIP SFX de tela arrancándose."

    cocinero llora "¿PERO QUÉ HACE?"

    # TODO: sacudir jajaja
    protagonista.c sin_delantal delirante "¿Qué hago? ¿QUE QUÉ HAGO? {b}JAJAJAJA{/b}"

    ## TODO: DELIRANTE fortíssimo, con delantal. Cómo?
    protagonista.c delirante "¡VOY A CONVERTIRME EN EL MEJOR CHEF DE PIZZA!"

    protagonista.c  "¡EL CAPO DE LA PIZZA!"

    "WIP Sonidos de recuerdo"

    show screen darkening_overlay(0.2)

    jump ch5_inscripcion_segunda_vuelta
