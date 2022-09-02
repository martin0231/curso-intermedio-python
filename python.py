
# Pip (package installer for python) Nos permite descargar paquetes de terceros para utilizarlos en nuestro enviroment, ademas se puede definir una versión especifica del paquete.
# |

# pip install <paquete> instala el paquete(pandas , matplotlib, bokeh, etc) que se especifique

# pip freeze muestra todos los paquetes instalados en tu ambiente virtual

# |
# Si quisiéramos que alguien mas pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:

# pip freeze > requirements.txt
# El resultado de pip freeze se escribe en requirements.txt (puedes usar otro nombre pero el mostrado es una buena practica)
# |
# para instalar paquetes desde un archivo como requirements.txt ejecutamos:

# pip install -r requirements.txt 

# EXCEPCIONES

# Algo que aparece casi al final de la lectura recomendada en el documentación de Python es que se puede agregar un “else” al try-except.

# TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
# EXCEPT: En el except se maneja el error, es decir, 
# si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.

# ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
# FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

# ASSERT 

# Assert statements

# Es una manera poco usual de manejar los errores en python
# Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo AssertionError y nos muestra un mensaje.
# Su sintaxis es:
# assert <condicion>, <"mensaje">
# <código>

# ARCHIVOS

# Modos de Apertura

# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

# Existen varias extensiones de archivos con los que podemos interactuar con python (js,csv,py,css,json,xml)
# Para abrir un archivo seguimos las siguiente estructura

# with open(<ruta>, <modo_apertura>) as <nombre>
# with Es un manejador contextual, nos ayuda a controlar el flujo del archivo 
#  (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

# open(ruta,modo_apertura): es una función que necesita de dos parámetros
# as <nombre> nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer