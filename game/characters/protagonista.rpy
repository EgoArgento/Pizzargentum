init offset = -1

init python:
    class MainCharacter:
        name: str
        c: Character

        def __init__(self):
            self.name = "Vos"
            self.c = Character(
                self.get_name,
                dynamic=True,
                image="protagonista",
                who_color="#F50106",
                who_outlines=[(2, "#7A2626", 0, 0)],
            )
            self.ch3_minijuego_seleccion = []
            self.ch3_karma = 0

        def get_name(self):
            return self.name

        # Función para aplicar migración de datos.
        # Llegado el caso de que realicemos cambios
        # en la estructura, con esta función nos aseguramos
        # que las partidas guardadas no quedarán rotas.
        def migrar_data(self):
            if hasattr(self, 'ch3_minijuego_seleccion') is False:
                self.ch3_minijuego_seleccion = []
            if hasattr(self, 'ch3_karma') is False:
                self.ch3_karma = 0

default protagonista = MainCharacter()

# Transformations
transform character_setup:
    left
    zoom 0.2

#
define sfx_protagonista_tsk = "audio/sfx/tsk-37433.ogg"
define sfx_protagonista_huh = "audio/sfx/confused-huh-352694.ogg"
define sfx_pasos = "audio/sfx/steps-40285.ogg"
define sfx_pasos_rapidos = "audio/sfx/steps-40285-faster.ogg"
define sfx_shh = "audio/sfx/shhhhhh-491234.ogg"
define sfx_masticar = "audio/sfx/munchin-95618.ogg"
define sfx_chefs_kiss = "audio/sfx/beetpro-kiss-19-11100.ogg"
define sfx_laughin_coughin = "audio/sfx/cackling-laugh-85211.ogg"
define sfx_laughin = "audio/sfx/cackling-laugh-85211-2.ogg"
#
image protagonista ansioso = At("images/protagonista ansioso.png", character_setup)
image protagonista confiado = At("images/protagonista confiado.png", character_setup)
image protagonista confundido = At("images/protagonista confundido.png", character_setup)
image protagonista delirante fortissimo = At("images/protagonista delirante fortissimo.png", character_setup)
image protagonista delirante = At("images/protagonista delirante.png", character_setup)
image protagonista enojado = At("images/protagonista enojado.png", character_setup)
image protagonista incredulo = At("images/protagonista incredulo.png", character_setup)
image protagonista llorando = At("images/protagonista llorando.png", character_setup)
image protagonista orgulloso = At("images/protagonista orgulloso.png", character_setup)
image protagonista pensante con_pizza = At("images/protagonista pensante con_pizza.png", character_setup)
image protagonista pensante = At("images/protagonista pensante.png", character_setup)
image protagonista picaro = At("images/protagonista picaro.png", character_setup)
image protagonista preocupado = At("images/protagonista preocupado.png", character_setup)
image protagonista sonriente = At("images/protagonista sonriente.png", character_setup)
image protagonista sorprendido = At("images/protagonista sorprendido.png", character_setup)

image protagonista sin_delantal ansioso = At("images/protagonista sin_delantal ansioso.png", character_setup)
image protagonista sin_delantal delirante fortissimo = At("images/protagonista sin_delantal delirante fortissimo.png", character_setup)
image protagonista sin_delantal delirante = At("images/protagonista sin_delantal delirante.png", character_setup)
image protagonista sin_delantal enojado = At("images/protagonista sin_delantal enojado.png", character_setup)
image protagonista sin_delantal incredulo = At("images/protagonista sin_delantal incredulo.png", character_setup)
image protagonista sin_delantal orgulloso = At("images/protagonista sin_delantal orgulloso.png", character_setup)
image protagonista sin_delantal orgulloso = At("images/protagonista sin_delantal orgulloso.png", character_setup)
image protagonista sin_delantal pensante con_pizza = At("images/protagonista sin_delantal pensante con_pizza.png", character_setup)
image protagonista sin_delantal picaro = At("images/protagonista sin_delantal picaro.png", character_setup)
image protagonista sin_delantal preocupado = At("images/protagonista sin_delantal preocupado.png", character_setup)
image protagonista sin_delantal sonriente = At("images/protagonista sin_delantal sonriente.png", character_setup)
image protagonista sin_delantal sorprendido = At("images/protagonista sin_delantal sorprendido.png", character_setup)

transform delantal_setup:
    zoom 0.9
    yoffset -50

image delantal primer plano = At("images/delantal primer plano.png", delantal_setup)