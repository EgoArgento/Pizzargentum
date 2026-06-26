image bg ch7 salida = "images/backgrounds/ch7_salida_concurso_noche.png"

define bgm_ch7_titanic_flauta = "audio/titanic_flauta.ogg"

style grito is text:
    bold True
    size gui.text_size * 2

style agrandado is text:
    size gui.text_size * 1.3

style achicado1 is text:
    size gui.text_size * 0.8

style achicado2 is text:
    size gui.text_size * 0.6

label ch7_2_siamo_fuori:
    protagonista.c ansioso "Yo.{w=0.1}.{w=0.1}.{w=0.1} {nw}"

    play sound sfx_gulp volume 2.0

    extend "{w=0.2}Yo se mucho de pizza."

    ravanello burlon "{shader=jitter:u__jitter=5.0, 9.0}Shaa veo{/shader}. Por eso no responde, "

    show screen whitening_overlay(0.2)
    play sound sfx_dramatic_impact volume 3.0
    pause 0.2
    hide screen whitening_overlay

    show protagonista incredulo
    show ravanello delirante

    extend "{=grito}¡¿NO?!{/=grito}"

    protagonista.c enojado "Escucháme bien, ¡no me hablés así!"

    ravanello entusiasmado "{=agrandado}¡¿QUE NO?! ¡Pruébame que sabes de lo que hablas!{/=agrandado}"

    protagonista.c confundido "Bueno... {=achicado1}Está la pizza marinera...{/=achicado1} {=achicado2}La pizzanessa...{/=achicado2}"

    ravanello delirante "{=agrandado}{b}¡AJÁ! ¡NINGUNA DE ESAS SON PIZZAS!{/b}{/=agrandado}"

    stop music
    play sound sfx_llorando loop

    protagonista.c llorando "¡Pará loco! ¡Tené piedad!"

    play music bgm_ch4_7_merry_cherry loop

    ravanello entusiasmado "¿Eso que oigo es {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}RENDICIÓN{/b}{/shader}?"

    stop sound

    protagonista.c enojado "{b}¡NO!{/b} VOS NO SABÉS NADA."

    play sound sfx_laughin_ravanello volume 3.0

    ravanello entusiasmado "¡Sepa perder, compañero!"

    ravanello burlon "Quizás, la proxima vez anótese a un concurso de su tallita~."

    play sound sfx_pasos_rapidos volume 2.0
    show protagonista:
        easein 1.5 xalign 0.75 zoom 0.7

    protagonista.c "{shader=jitter:u__jitter=5.0, 9.0}¡¡¡¡YA VAS A VER!!!!{/shader}"

    protagonista.c "{shader=jitter:u__jitter=5.0, 9.0}{b}¡¡¡¡PARÁTE DE MAAAANOS, GIIIIIIIIL!!!!{/b}{/shader}"

    show screen whitening_overlay(0.2)
    play sound sfx_dramatic_impact volume 3.0

    stop music fadeout 0.6

    pause 1.0

    jump ch7_2_siamo_fuori_2

label ch7_2_siamo_fuori_2:
    scene bg ch7 salida

    play music bgm_ch7_titanic_flauta fadein 0.4

    hide screen whitening_overlay with dissolve

    protagonista.c "No puedo creer que me rajaran por eso..."

    play sound sfx_suspiro_quejoso

    protagonista.c "Acá todos pecho fríos loco, no se bancan una..."

    pause

    show screen darkening_overlay(1.0)
    pause 1.0

    centered "FIN"

    return