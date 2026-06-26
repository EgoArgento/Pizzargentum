# Cualquier configuración global que haya que realizar,
# se debe ejecutar en esta sección
init python:
    renpy.music.register_channel("ambient", "sfx", loop=False)

define bgm_un_estate_italiana = "audio/un_estate_italiana.ogg"

screen timed_choice(t, action):
    default remaining = t

    timer 0.05 repeat True action If(
        remaining > 0,
        SetScreenVariable("remaining", remaining - 0.05),
        [Hide("timed_choice"), action]
    )
    $ fraction = remaining / t if t > 0 else 0

    bar:
        value remaining
        range t
        xalign 0.5
        yalign 0.1
        xmaximum 300
        right_bar "#222"

        if fraction > 0.5:
            left_bar "#3c3"
        elif fraction > 0.25:
            left_bar "#fa0"
        else:
            left_bar "#f33"


label start:
    jump ch1_inscripcion
