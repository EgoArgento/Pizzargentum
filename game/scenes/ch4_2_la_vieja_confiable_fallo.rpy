label ch4_2_la_vieja_confiable_fallo:
    # TODO: hacer que si se llega por falta de tiempo
    # cambien algunos diálogos.

    # TODO: agregar PREOCUPADO
    protagonista.c sin_delantal incredulo "Bueno, mal olor no tiene."

    "WIP SFX Portazo fuerte"

    show cocinero enojado

    cocinero "¿Y usted quién es? ¡¿Qué hace acá?!"

    protagonista.c sin_delantal nervioso "Taniiito, ¡ya te tardabas mucho!"

    cocinero "¿Pero qué dice? ¡SALGA AHORA MISMO DE MI COCINA!"

    protagonista.c "Disculpá, disculpá."

    protagonista.c "{=susurro}Siamo fuori...{/=susurro}"

    cocinero "¡SALGA AHORA!"

    "WIP Sonido de pasos"
    "WIP Mover al personaje fuera de pantalla"

    play sound abrir_puerta
    pause 2.0
    hide protagonista

    show screen darkening_overlay(1.0)

    protagonista.c "Me echaron a patadas y encima me olvidé la pizza adentro."

    centered "FIN"

    return