# Tabla de verdad a codigo VHDL
## !Importante!
Este script unicamente es capaz de manejar archivos CSV y generar codigo para estructuras de tipo **Switch** en lenguaje VHDL.
## intoduccion
Un script exscrito en python que toma una tabla de verdad en csv de tipo binadio con entradas y salidas y las convierte en cadenas completas y en codigo VHDL para un switch

## Uso
#### ! phyton3 es requerido para el uso de este script
La tabla de verdad debera tener una columna que servira para identificar la separacion entre entradas y salidas.
ESTA COLUMNA SOLO DEBE CONTENER EL SEPARADOR 

Por defecto el script utiliza `` | `` sin embargo es posible cambiar este separador a la como parametro a la hora de ejecutar

El script imprimira y generara las salidas detectadas y un archivo txt con el mismo nombre del archivo de entrada y el codigo para un swich VHDL.

## Parametros
 **Archivo de entrada:** Parametro posicional **OBLIGATORIO** con la ruta del archivo csv
 **Ejemplo:** ```main.py ./tabla_verdad.csv```

---
 **Separador:** *opcional* Este indica el caracter o cadena de caracteres usada en la cadena de caracteres utilizada para la columna separadora __Valor por defecto: `` | ``__
 
 **Ejemplo:** ```main.py ./tabla_verdad.csv --separador 'separadora'```

----
 **Codigo:** *opcional* Para la produccion de codigo VHDL, este indica el nombre que se le dio al conjunto de bits de salida para la tabla.
 __Valor por defecto: `` display ``__
 
 **Ejemplo:** ```main.py ./tabla_verdad.csv --codigo 'pantalla'```

 
