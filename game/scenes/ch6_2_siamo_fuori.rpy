label ch6_2_siamo_fuori:
    # TODO: agregar NERVIOSO
    protagonista.c nervioso "Yo... Yo se mucho de pizza."

    "El PROTAGONISTA ríe nervioso."

    ravanello burlon "Shaa veo. Por eso no responde, {b}¡¿NO?!{/b}"

    "El texto 'Shaa veo' se sacude en pantalla, '¡¿NO?!' tiene un tamaño mayor. Se hace un pequeño acercamiento a la escena con un flash blanco."

    protagonista.c enojado "Escucháme bien, ¡no me hablés así!"

    "La cámara se acerca a Ravanello. Comienza a sonar un temporizador."

    # TODO: ravanello entusiasmado
    ravanello entusiasmado "¡¿QUE NO?! ¡Pruébame que sabes de lo que hablas!"

    "El texto de Ravanello se ve de tamaño mayor al anterior. La cámara se acerca al PROTAGONISTA."

    # TODO: agregar confundido
    protagonista.c confundido "Bueno... Está la pizza marinera... La pizzanessa..."

    "El texto del PROTAGONISTA decrece progresivamente en tamaño. La cámara se acerca a Ravanello."

    # TODO: ravanello delirante
    ravanello delirante "{b}¡AJÁ! ¡NINGUNA DE ESAS SON PIZZAS!{/b}"

    "La pantalla se sacude mientras Ravanello habla. La cámara se acerca al PROTAGONISTA. Un vidrio no diegético se rompe. La música se corta. El temporizador termina con un *RIIING*."

    # TODO: agregar llorando
    protagonista.c llorando "¡Pará loco! ¡Tené piedad!"

    "Se escucha la respiración agitada del protagonista. Suena música chistosa del estilo de 'Jaunty Gumption'."

    # TODO: ravanello entusiasmado
    ravanello entusiasmado "¿Eso que oigo es {shader=jitter:1.0,6.0|wave:u__amplitude=3.0:u__frequency=6.0}{b}RENDICIÓN{/b}{/shader}?"

    protagonista.c enojado "{b}¡NO!{/b} VOS NO SABES NADA."

    "Se escucha la risa de Ravanello."

    ravanello desafiante "¡Sepa perder, compañero!"

    # TODO: agregar ravanello burlon
    ravanello burlon "Quizás, la proxima vez anótese a un concurso de su tallita~."

    protagonista.c "¡¡¡¡YA VAS A VER!!!!"

    "El texto se sacude en pantalla. El protagonista se aproxima rápido a Ravanello."

    protagonista.c "{b}¡¡¡¡PARÁTE DE MAAAANOS, GIIIIIIIIL!!!!{/b}"

    "El texto se sacude en pantalla, se lee mucho más grande. Se escucha un sonido fuerte."

    "FADE TO WHITE"

    jump ch6_2_siamo_fuori_2

label ch6_2_siamo_fuori_2:
    "FADE IN FROM WHITE"

    "No se percibe el entorno ni al protagonista, tampoco hay sonidos ambientales."

    protagonista.c enojado "No puedo creer que me rajaron por eso..."

    "Se escucha un quejido del protagonista."

    protagonista.c "Acá todos iguales loco, no se bancan una..."

    pause

    show screen darkening_overlay(1.0)
    pause 1.0

    centered "FIN"

    return