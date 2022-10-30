# Proyecto Sharks Attacks

![img](https://img.freepik.com/foto-gratis/tiburon-gris-blanco_628469-340.jpg?w=1800&t=st=1667171042~exp=1667171642~hmac=536d8c2f5f5898650391fe3e780004a5536a1c5615d03c7ca2ffd5a1c9990534)


Se trata de una limpieza de datos de un DataSet que trata de registros de ataques de tiburones en relación a diferentes variebles. Hay que limpiar el archivo ya que en el mismo hay gran cantidad de valores nulos, datos incoherentes, variedad de formatos y algunos errores de escritura o transcioción.

Se importa el archivo a un Jupyter Notebook y todas la librerías necesarias para trabajar sobre el mismo para realizar la limpieza de los datos aportados convertidos en un Data Frame.

Se establece un objertivo basado en tres hipótesis para tras haber limpiado el archivo poder estudiar las mismas. Las hipótesis han sido escogidas de manera aleatoria únicamente con el objetivo de poder realiar una visualizaciónd de lso datos limpios que nos aporten una información relevante para las hipótesis escogidas.



### Limpieza inicial de los datos en bruto.

En primer lugar se realiza una limpieza de las columnas con alto porcentaje de valores nulos (NaN), más de 23.000. Posteriormente se eliminan filas duplicadas, comprobando que la gran mayoría de las filas inferiores no tienen ningún valor.

Se continua con la limpieza columna a columna de valores nulos y unificación de formatos de la siguiente manera:

Limpieza de datos tras análisis de columnas:

En todas ellas se realizará las sustitución de los valores nulos de manera genérica por 'unkown', habiendo alguna particularidad en alguna de ellas.

1. Columas case_number y date. Ya que son columnas que nos expresan el mismo tipo de dato, se va a eliminar la de date y se expresará la de case_number en formato año.mes.día.

2. Columna type. Únicamente se eliminan valores nulos.

3. Columna country. Mediante la creación de dos funciones apoyadas en regex se ponen los nombres de los países en mayúscula y se eliminan caracteres especiles que había en alguno de los nombres.

4. Columna area. Se toma la decisión de no modificar nigún valor más en la columna area a parte de quitar los nulos, ya que no es determinante para nuestra hipótesis porque se va a tener en cuenta un grado mayor que es el país.

5. Columna location. Únicamente se eliminan valores nulos.

7. Columna name. Se crea una función para limpiar los valores diferentes a lo que podrían ser que los sustituye por 'unkown'.

8. Columna sex_. Se crea una función que únicamente exprese los valores conocidos en Male o Female.

9. Columna age. Mediante el calculo de la media se crea una funcion para expresar todos los datos que no son nulos en un dato de edad concreta.

10. Columna injury.Solo se quitan valores nulos.

11. Columna fatal. De la misma manera que en columnas anteriores, se crea una función que no devuelva el tipo de lesión en función de la gravedad de la misma, que devuele Yes, No o N/A.

12. Columna time. Se crean dos funciones para dividir el día en cuatro partes y aplicarlo según las horas de 00 a 23.

13. Columna species_. Con patrones de ergex se crea una función que agrupa las diversas especies en unas determinadas.

14. Columna href_formula. Se sustituyen por valor desconocido las celdas que no aportan una dirección web accesible.

15. Columna investigator_or_source. Se rellenan valores nulos con 'unknown'.

Aunque no se mencionan anteriormente, las columnas pdf y original_order no sufren ningún cambio ya que no ofrecen ningún valor nulo. Cabe destacar que no se modifica original_order ya que como su propio nombre indica, aunque descienda hasta el valor 2 y no el 1, se cosidera que al ser el orden original carece de sentido su modificación.


La parte de visulización ofrece los gráficos para concer el resultado de las hipótesis reflejadas al principio.



### Partes del proyecto.

Jupyter Notebook de limpieza y parte de visualización.
Documento gitignore.
Una carpeta src con archivos de limpieza de código
Un archivo Readme


CONCLUSIÓN FINAL:

Hipótesis 1--> Se verifica que dicho país se trata de USA.

Hipótesis 2--> Descartando los valores desconocidos, se verifica que pescando ha sido cuando se han producido el mayot número de ataques.
Hipótesis 3--> Los valores más altos de ataque se dan en hombres que en mujeres en un rango de edad de unos 48 años.