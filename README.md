# Pizzargentum

## Mecánicas

- El uso del continuado automático para los diálogos tiene ser únicamente utilizado como interrupción al diálogo de otro personaje.

## Organización

> Todo aquello que está dentro de la carpeta game se considera parte del juego de renpy.

- **script.rpy**: entrypoint de la aplicación.
- **characters**: carpeta de configuración de personajes.
- **scenes**: carpeta de escenas. Cada archivo debe representar una escena. Se deben nombrar con la siguiente plantilla: `{XX.YY}-{nombre_completo}.rpy`. Ej: `01-inscripcion.rpy`.
- **audio**: carpeta de sonidos y música.
- **libs**: dependencias de 3os para renpy.
- **images**: imágenes para las escenas y personajes.
  - **Personajes**: las imágenes de personajes deben seguir el formato obligatorio de renpy: `{CHARACTER_NAME} {STATE}.png`. Ej: `protagonista feliz.png`.
- **gui**: carpeta de UI. Todo lo que debe ser parte del diseño de la UI debe ser realizado acá.
- **tl**: carpeta de traducciones. Deben contener traducciones dentro de una carpeta del idioma relacionado y dentro los archivos `.rpym`. Ej: `tl/es/common.rpym`.