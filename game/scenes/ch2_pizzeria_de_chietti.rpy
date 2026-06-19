image bg ch2 pizzeria_interior_chieti = "images/backgrounds/ch2_pizzeria_interior_chieti.png"
image bg ch2 pizzeria_cocina_chieti = "images/backgrounds/ch2_pizzeria_cocina_chieti.png"

label ch2_pizzeria_de_chietti:
    hide screen darkening_overlay

    play music "audio/restaurante.mp3" loop
    scene bg ch2 pizzeria_interior_chieti

    pause 1000