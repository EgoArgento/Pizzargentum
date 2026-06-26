image bg ch7 salida = "images/backgrounds/ch7_salida_concurso_noche.png"

define bgm_ch7_titanic_flauta = "audio/titanic_flauta.ogg"

label ch7_2_siamo_fuori:
    protagonista.c ansioso "Yo.{w=0.1}.{w=0.1}.{w=0.1} {nw}"

    play sound sfx_gulp volume 2.0

    extend "{w=0.2}Yo se mucho de pizza."

    ravanello burlon "Shaa veo. Por eso no responde, {b}¡¿NO?!{/b}"

    # TODO: fix
    "El texto 'Shaa veo' se sacude en pantalla, '¡¿NO?!' tiene un tamaño mayor. Se hace un pequeño acercamiento a la escena con un flash blanco."

    protagonista.c enojado "Escucháme bien, ¡no me hablés así!"

    # TODO: fix
    "La cámara se acerca a Ravanello. Comienza a sonar un temporizador."

    ravanello entusiasmado "¡¿QUE NO?! ¡Pruébame que sabes de lo que hablas!"

    # TODO: fix
    "El texto de Ravanello se ve de tamaño mayor al anterior. La cámara se acerca al PROTAGONISTA."

    protagonista.c confundido "Bueno... Está la pizza marinera... La pizzanessa..."

    # TODO: fix
    "El texto del PROTAGONISTA decrece progresivamente en tamaño. La cámara se acerca a Ravanello."

    ravanello delirante "{b}¡AJÁ! ¡NINGUNA DE ESAS SON PIZZAS!{/b}"

    # TODO: fix
    "La pantalla se sacude mientras Ravanello habla. La cámara se acerca al PROTAGONISTA. Un vidrio no diegético se rompe. La música se corta. El temporizador termina con un *RIIING*."

    play sound sfx_llorando loop

    protagonista.c llorando "¡Pará loco! ¡Tené piedad!"

    play music bgm_ch4_7_merry_cherry loop

    ravanello entusiasmado "¿Eso que oigo es {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}RENDICIÓN{/b}{/shader}?"

    stop sound

    protagonista.c enojado "{b}¡NO!{/b} VOS NO SABES NADA."

    play sound sfx_laughin_ravanello volume 3.0

    ravanello entusiasmado "¡Sepa perder, compañero!"

    ravanello burlon "Quizás, la proxima vez anótese a un concurso de su tallita~."

    protagonista.c "¡¡¡¡YA VAS A VER!!!!"

    # TODO: fix
    "El texto se sacude en pantalla. El protagonista se aproxima rápido a Ravanello."

    protagonista.c "{b}¡¡¡¡PARÁTE DE MAAAANOS, GIIIIIIIIL!!!!{/b}"

    # TODO: fix
    "El texto se sacude en pantalla, se lee mucho más grande. Se escucha un sonido fuerte."

    show screen whitening_overlay(0.2)

    stop music fadeout 0.6

    pause 0.6

    jump ch7_2_siamo_fuori_2

label ch7_2_siamo_fuori_2:
    scene bg ch7 salida

    play music bgm_ch7_titanic_flauta fadein 0.4

    hide screen whitening_overlay with dissolve

    protagonista.c "No puedo creer que me rajaron por eso..."

    play sound sfx_suspiro_quejoso

    protagonista.c "Acá todos iguales loco, no se bancan una..."

    pause

    show screen darkening_overlay(1.0)
    pause 1.0

    centered "FIN"

    return