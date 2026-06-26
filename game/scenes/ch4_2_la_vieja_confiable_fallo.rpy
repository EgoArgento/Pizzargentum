# TODO: Corregir sprites en discusión con Cocinero
# TODO: Corregir sprites en ch5

define ch4_2_timeout = False

label ch4_2_la_vieja_confiable_fallo_timeout:
    $ ch4_2_timeout = True

    jump ch4_2_la_vieja_confiable_fallo

label ch4_2_la_vieja_confiable_fallo:
    if ch4_2_timeout is False:
        protagonista.c sin_delantal preocupado "Bueno, mal olor no tiene."

    play sound sfx_portazo volume 2.0

    pause 2.0

    show cocinero enojado

    cocinero "¿Y usted quién es? ¡¿Qué hace acá?!"

    protagonista.c sin_delantal ansioso "Taniiito, ¡ya te tardabas mucho!"

    cocinero "¿Pero qué dice? ¡SALGA AHORA MISMO DE MI COCINA!"

    protagonista.c "Disculpá, disculpá."

    protagonista.c "{=susurro}Siamo fuori...{/=susurro}"

    cocinero "¡SALGA AHORA!"

    play sound sfx_pasos_rapidos volume 2.0

    show protagonista:
        easein 1.5 xalign 1.5

    pause 1.2

    play sound sfx_abrir_puerta
    pause 2.0
    hide protagonista

    show screen darkening_overlay(1.0)

    protagonista.c "Me echaron a patadas y encima me olvidé la pizza adentro."

    centered "FIN"

    return