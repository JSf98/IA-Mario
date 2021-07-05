# IA-Mario

Inteligencia artificial que tiene como objetivo aprender a jugar mediante un algoritmo genético a un nivel acuático del juego Super Mario World. 

## Requisitos

* Sistema operativo Windows 10
* Emulación mediante emulador SNES9X
  * Cambiar, dentro de 'input configuration', a configuración 'wasd'
* Nivel acuático: Donut Secret 1
* Python 3.8
* Monitor 1920x1080 escala 100% (sino hay que ajustar valores de recorte al capturar la pantalla) 
* CPU intel i7 gen 8 o similares (requisito mínimo recomendado)

## Como instalarlo

1. Clonar el repositorio
2. Instalar las librerías necesarias. Se recomiendo utilizar un entorno virtual con la versión específica de Python. 

## Como iniciarlo y resultados

Una vez se han instalado las librerias, es necesario tener abierto el videojuego antes de darle al botón de ejecución. Existe una clase 'Singleton' con la cual el usuario puede jugar con los valores de configuración de las redes. Los resultados se guardaran dentro de la carpeta 'Experiments'. 
