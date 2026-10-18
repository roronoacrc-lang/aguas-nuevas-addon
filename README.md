# Aguas Nuevas Bedrock Addon

Addon Bedrock 1.20.x con 10 bloques de agua con efectos al pisarlos/entrar en ellos.
No usa cubetas ni simulación real de agua del motor; usa bloques renderizados semitransparentes, compatibles con una estética tipo "Vibrant Visuals".

## Instalación
1. Instala Pillow si no lo tienes:
   pip install pillow
2. Genera las texturas PNG:
   python resource_pack/generate_textures.py
3. Comprime `behavior_pack` y `resource_pack` juntos en la raíz del ZIP y cámbialo a `.mcaddon`.
4. Importa el `.mcaddon` en Minecraft Bedrock.

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

## Importante para Minecraft
El archivo debe ser un ZIP que contenga `behavior_pack` y `resource_pack` directamente en la raíz. Si metes una carpeta extra, Minecraft mostrará el nombre de la carpeta en lugar del nombre del .mcaddon.
