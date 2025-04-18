En este archivo se hablarán de lo que se va a hacer en este curso

## Contenido del curso
1. Introducción
2. Repaso de python
3. PROYECTO 1
4. get/Post/put/delete y otras ordenes
5. PROYECTO 2
6. Clases y manejo de errores
7. PROYECTO 3
8. Databases y ORM
9. Autentificacion JWT
10. Enrutamiento (Routing)
11. PROYECTO 3.5
12. DB y Migración de DB
13. PROYECTO 4
14. Unidad Integración y testing
15. PROYECTO 5
16. Full stack development

##Sección 2 - Repaso de Python

###String formatting

El uso de la f antes del print: (tenemos una variable llamada first_name = "Eric")

print ("hi"+ first_name) es igual a print (f"hi {first_name}), esto se llama formato f-string

Otra forma sería :

sentence = "hi {}"
print(sentence.format(first_name))

###OOP (object oriented programming)
La idea dseria definir una clase que es como un diccionario con funciones dentro, y un programa main que importe todas las clases 

La funcion __innit__(self): que se suele definir vacía indica lo que hay que hacer con la clase cuando se inicializa, a veces es así  __innit__(self, parametro1, parametro2= 4,..): y liuego udsariamos esas entradas para definir self.argiumento1=argumento1,...

Mediante encapsulation podemos definir algunas variables como publicas o privadas de forma que se puedan cambair por el usuario o no, si definimos:

self.__typer_of_enemy, para la variable type of enemy, esas dobles barras hacen que no se pueda cambiar (seria "privada"). Tendríamos que definir algunas funciones ("getters and setters") para definir o modificar esas variables privadas

####Notas 
- Lo que pidas como input lo recibirá como string, debras aplicarle un float o int para convertirlo a otro formato.

-Los sets son como las listas pero se marcan cpn {} y no pueden tener repetidos y no tienen orden.

-Las tuplas se marcan con (

-Dentro de un while o for, si pongo un continue salta el resto del bucle y salta a la siguiente iteracion

-Dentro de un mismo programa puedo llamar a funciones definidas más adelante

