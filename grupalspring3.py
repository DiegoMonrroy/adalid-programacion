'''SPRINT DE ENTREGA:
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos
durante el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:
● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
● Por cada cuenta debe pedir un número telefónico para contactarse.

● El programa no terminará de preguntar por los números hasta que todas las organizaciones
tengan un número de contacto asignado.
● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
● Se debe guardar como un string.
A modo de entrega, se debe disponer un documento Word o PDF en el que se indique:
- Ruta del repositorio en GitHub

Consideraciones adicionales
- El código debe estar debidamente indentado
- El formato del documento Word queda a criterio del equipo.'''




import random

import string


#Funcion para crear usuarios a partir de una lista

def crear_usuarios():

    name = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Laura", "Diego", "Fernanda"]

    diccionarios = []

    for i in range(10):

        diccionario = {"name": name[i], "password": None, "contact": None}

        diccionarios.append(diccionario)

    return diccionarios



#llamamos a la funcion con 10 variables distintas, que seran el ID de cada cliente

A111, A112, A113, A114, A115, A116, A117, A118, A119, A120 = crear_usuarios()



#creamos una lista con las variables que almacenan a nuestros usuarios

list_user = [A111, A112, A113, A114, A115, A116, A117, A118, A119, A120]



#funcionpara crear contraseña

def crear_contraseña(list_user):

    caracteres = string.ascii_letters + string.digits # letras mayúsculas, minúsculas y números

    usuarios = []

    for user in list_user:

        password = ''.join(random.choices(caracteres, k=8)) # genera una contraseña aleatoria de 8 caracteres

        user["password"] = password

        usuarios.append(user)

    return usuarios



usuarios_con_contraseña = crear_contraseña(list_user)

print(usuarios_con_contraseña)



def ingresar_contacto(list_user):

    for user in list_user:

        contacto = input(f"Ingrese el número de contacto para {user['name']}: ")

        while len(contacto) != 8 or not contacto.isdigit():

            contacto = input("El número de contacto debe tener 8 dígitos. Ingrese nuevamente: ")

        user["contact"] = contacto

    return list_user


usuarios_con_contacto = ingresar_contacto(usuarios_con_contraseña)

print(usuarios_con_contacto)


