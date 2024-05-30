# Lexer Parser Project with ANTLR

Este proyecto demuestra cómo usar ANTLR para crear un lexer y un parser. ANTLR es una poderosa herramienta para trabajar con lenguajes y genera analizadores léxicos y sintácticos a partir de gramáticas definidas en archivos `.g4`.
En este caso, trabajaremos con una gramatica para archivos .json especificos. La estructura de los documentos aceptados son las siguientes:

En el archivo **input.json** se encuentra un ejemplo que es aceptado por la gramática.

## Aclaración
En esta primera etapa 30/05/2024 solo se proporciona el analizador léxico, proximamente se realizará el analizador sintáctico.


## Requisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados:
- [Java JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [ANTLR](https://www.antlr.org/download.html)
- [Python (si usas el runtime de Python)](https://www.python.org/downloads/)


## Instalación

### 1. Instalar ANTLR

Puedes instalar ANTLR siguiendo las instrucciones de la [página oficial](https://www.antlr.org/download.html). Aquí tienes un ejemplo de cómo instalarlo en un sistema Unix:

#### bash
##### Descargar ANTLR jar
`curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar`

##### Mover el archivo a un directorio específico, por ejemplo, /usr/local/lib/
`sudo mv antlr-4.9.2-complete.jar /usr/local/lib/`

##### Configurar el alias en tu archivo de configuración de shell (por ejemplo, .bashrc o .zshrc)
`echo 'alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'' >> ~/.bashrc`

`echo 'alias grun='java org.antlr.v4.gui.TestRig'' >> ~/.bashrc`

##### Aplicar los cambios
`source ~/.bashrc`

##### Descargar ANTLR para python
`pip install antlr4-python3-runtime`


### 2. Clonar el repositorio

#### bash
`git clone <URL_del_repositorio>`

`cd nombre_del_proyecto`


### 3. Ejecutar (Python)

#### bash
##### Ejecutar el analizador
`python lexer.py input.json`




# Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.

# Redes de los contribuidores
- https://github.com/AugustoDor
- https://github.com/JuanMarighetti
- https://github.com/LukitaPeola
- https://github.com/IvooBSJ
