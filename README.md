# Aguas Nuevas Bedrock Addon

Addon Bedrock 1.20.x con 10 bloques de agua con efectos al pisarlos/entrar en ellos.
No usa cubetas ni simulación real de agua del motor; usa bloques renderizados semitransparentes, compatibles con una estética tipo "Vibrant Visuals".

## Instalación
1. Genera las texturas PNG:
   - Instala Pillow si no lo tienes:
     pip install pillow
   - Ejecuta desde la carpeta resource_pack:
     python generate_textures.py

2. Verifica la estructura y comprime:
   - Debes tener las carpetas `behavior_pack/` y `resource_pack/` en la raíz del ZIP.
   - Comprime ambas carpetas en un ZIP y renombra la extensión a `.mcaddon` (por ejemplo `aguas_nuevas.mcaddon`).

3. Importa el `.mcaddon` en Minecraft Bedrock y activa el Resource Pack y Behavior Pack en tu mundo.

## Efectos por bloque
- water_lime: Regeneración
- water_cyan: Velocidad
- water_red: Fuerza
- water_orange: Resistencia al fuego
- water_purple: Veneno
- water_lightblue: Levitación
- water_darkblue: Lentitud
- water_indigo: Visión nocturna
- water_aqua: Invisibilidad
- water_yellow: Salto alto

## Notas
- Si quieres que suba también el `.mcaddon` ya empaquetado con texturas incluidas, dímelo y lo preparo (puede tardar un poco más).