# Cualquier configuración global que haya que realizar,
# se debe ejecutar en esta sección
init python:
    renpy.music.register_channel("ambient", "sfx", loop=True)

label start:
    jump ch1_inscripcion
