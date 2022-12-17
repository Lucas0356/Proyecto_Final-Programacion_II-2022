from os import system #La usaremos para limpiar la terminal con system("cls")
import requests, json
from http import HTTPStatus

# _______________________________________________________________ Funciones _______________________________________________________________

def menu_principal():
    system("cls") #Limpia la terminal
    print('-------------------------------')
    print('       Nombre Programa         ')
    print('-------------------------------')
    print('[1] Iniciar sesión')
    print('[2] Modo público')
    print('[0] Salir')
    print('-------------------------------')
    return
    
def menu_usuario(usuario):
    print('-------------------------------')
    print('         ',usuario)
    print('-------------------------------')
    print('[1] Agregar Pelicula')
    print('[2] Editar Pelicula')
    print('[3] Agregar Comentario')
    print('[4] Editar Comentario')
    print('[5] Buscar')
    print('-------------------------------')
    return

def menu_genero():
    print('\n-------------------------------')
    print('       Escogedor de Genero       ')
    print('-------------------------------\n')
    
def menu_director():
    print('\n-------------------------------')
    print('      Escogedor de Director      ')
    print('-------------------------------\n')

def cargar_usuarios():
    with open('datos_json/usuarios.json') as archivo:
        datos_json = json.load(archivo)
        return datos_json

def cargar_generos():
    with open('datos_json/generos.json') as archivo_generos:
        generos = json.load(archivo_generos)
        return generos

def cargar_directores():
    with open('datos_json/directores.json') as archivo_directores:
        directores = json.load(archivo_directores)
        return directores

def iniciar_sesión(usuarios):
    while True:
        INusuario = input("\nIngrese su nombre de usuario: ")
        contador_max = len(usuarios)
        contador = 0
        for usuario in usuarios:
            if INusuario != usuario["username"]:
                contador = contador + 1
                if contador == contador_max:
                    print ("\nNombre de usuario inexistente")
                    continue
            elif INusuario == usuario["username"]:
                INcontraseña = input ("\ningrese su contraseña: ")
                datos_usuarios = cargar_usuarios()
                for usuario in datos_usuarios["users"]:
                    if usuario["username"] == INusuario:
                        if INcontraseña == usuario["password"]:
                            print('\nBienvenido ' + INusuario + '!')
                            return INusuario
                        else: 
                            print ("\nContraseña incorrecta")
                            continue

def buscar_película_nombre():
    INpelícula = input("Ingrese la película que desea buscar: ")
    film_search = requests.get('http://127.0.0.1:5000/films/'+INpelícula)
    if str(film_search) != '<Response [400]>':
        print(film_search.json())
        return
    else:
        print ("\nPelícula inexistente")
        return

def elegir_genero():
    menu_genero()
    generos = cargar_generos()
    i = 0
    for genero in generos["genders"]:
        print ('[' + str(i) + '] ' + str(genero["gender"]))
        i = i + 1
    opcion_genero = input("\nIngrese el genero que desea: ")
    if opcion_genero == '0':
        genero = "Accion"
    elif opcion_genero == '1':
        genero = "Aventura"
    elif opcion_genero == '2':
        genero = "Ciencia Ficcion"
    elif opcion_genero == '3':
        genero = "Comedia"
    elif opcion_genero == '4':
        genero = "Drama"
    elif opcion_genero == '5':
        genero = "Fantasia"
    elif opcion_genero == '6':
        genero = "Suspenso"
    elif opcion_genero == '7':
        genero = "Terror"
    return genero

def elegir_director():
    menu_director()
    directores = cargar_directores()
    i = 0
    for director in directores["directors"]:
        print ('[' + str(i) + '] ' + str(director["director"]))
        i = i + 1
    opcion_genero = input("\nIngrese el director que desea: ")
    if opcion_genero == '0':
        director = "Alfonso Cuaron"
    elif opcion_genero == '1':
        director = "Clint Eastwood"
    elif opcion_genero == '2':
        director = "Francis Ford Coppola"
    elif opcion_genero == '3':
        director = "Gore Verbinski"
    elif opcion_genero == '4':
        director = "Goro Taniguchi"
    elif opcion_genero == '5':
        director = "James Cameron"
    elif opcion_genero == '6':
        director = "Jeff Fowler"
    elif opcion_genero == '7':
        director = "Quentin Tarantino"
    elif opcion_genero == '8':
        director = "Robert Zemeckis"
    elif opcion_genero == '9':
        director = "Sam Raimi"
    elif opcion_genero == '10':
        director = "Steven Spielberg"
    elif opcion_genero == '11':
        director = "Tetsuro Kodama"
    elif opcion_genero == '12':
        director = "Tim Burton"
    elif opcion_genero == '13':
        director = "Woody Allen"
    
    return director


# _______________________________________________________________ Código _______________________________________________________________

menu_principal()
opcion = input("ingrese una opción: ")
if opcion == '1':
    usuarios = requests.get('http://127.0.0.1:5000/users')
    usuarioin = iniciar_sesión(usuarios.json())
    menu_usuario(usuarioin)
    buscar_película_nombre()

elif opcion == '2':
    ultimas10 = requests.get('http://127.0.0.1:5000/films/last10')
    print(ultimas10.json())
elif opcion == '0':
    exit