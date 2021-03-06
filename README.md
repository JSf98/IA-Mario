# IA-Mario

Inteligencia artificial que tiene como objetivo aprender a jugar mediante un algoritmo genético a un nivel acuático del juego Super Mario World. 

## Requisitos

* Sistema operativo Windows 10
* Emulación mediante emulador SNES9X
  * Cambiar, dentro de 'input configuration', a configuración 'wasd'
* Nivel acuático: Donut Secret 1
* Python 3.8
* Monitor 1920x1080 escala 100% (sino hay que ajustar valores de recorte al capturar la pantalla y aquellos valores que agilizan el proceso de aprendizaje) 
* CPU intel i7 gen 8 o similares (requisito mínimo recomendado)

## Como instalarlo

1. Clonar el repositorio
2. Instalar las librerías necesarias. Se recomiendo utilizar un entorno virtual con la versión específica de Python. 

## Como iniciarlo y resultados

Una vez se han instalado las librerías, es necesario tener abierto el videojuego antes de darle al botón de ejecución. Existe una clase 'Singleton' con la cual el usuario puede jugar con los valores de configuración de las redes. Es necesario que el usuario prepare un 'slot' dentro del emulador de tal forma que cada vez que acabe una red, este pueda reiniciarse correctamente dentro del propio nivel. Los resultados se guardarán dentro de la carpeta 'Experiments'. 
