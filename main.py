from os import system #La usaremos para limpiar la terminal con system("cls")
import requests, json, time, re

# _______________________________________________________________ Funciones _______________________________________________________________ #

# ______________________________ Menus ______________________________ #

def menu_principal():
    while True:
        system("cls") #Limpia la terminal
        print('-------------------------------')
        print('\tNombre Programa         ')
        print('-------------------------------')
        print('[1] Iniciar sesión')
        print('[2] Modo público')
        print('[3] Registrarse')
        print('[0] Salir')
        print('-------------------------------')
        INopcion = input("\nIngrese una opción: ")
        if INopcion.isdigit() == True:
            if int(INopcion) >= 0 and int(INopcion) <= 3:
                return (INopcion)
            else:
                print("\nIngrese una opción válida")
                time.sleep(1)
                continue
        else:
            print("\nIngrese una opción válida")
            time.sleep(1)
            continue

def menu_usuario(usuario):
    while True:
        system("cls") #Limpia la terminal
        print('\n-------------------------------')
        print('         ',usuario)
        print('-------------------------------')
        print('[1] Agregar Pelicula')
        print('[2] Editar Pelicula')
        print('[3] Eliminar Película')
        print('[4] Agregar Comentario')
        print('[5] Editar Comentario')
        print('[6] Eliminar Comentario')
        print('[7] Buscar')
        print('[0] Salir')
        print('-------------------------------')
        INopcion = input("\nIngrese una opción: ")
        if INopcion.isdigit() == True:
            if int(INopcion) >= 0 and int(INopcion) <= 7:
                return (INopcion)
            else:
                print("\nIngrese una opción válida")
                time.sleep(1)
                continue
        else:
            print("\nIngrese una opción válida")
            time.sleep(1)
            continue

def menu_buscar(): 
    while True:
        system("cls") #Limpia la terminal
        print('\n-------------------------------')
        print('          Menú buscar'         )
        print('-------------------------------')
        print('[1] Buscar por nombre')
        print('[2] Buscar por director')
        print('[3] Buscar por género')
        print('[0] Salir')
        print('-------------------------------')
        INopcion = input("\nIngrese una opción: ")
        if INopcion.isdigit() == True:
            if int(INopcion) >= 0 and int(INopcion) <= 3:
                return (INopcion)
            else:
                print("\nIngrese una opción válida")
                time.sleep(1)
                continue
        else:
            print("\nIngrese una opción válida")
            time.sleep(1)
            continue

def menu_genero():
    print('\n-------------------------------')
    print('       Escogedor de Genero       ')
    print('-------------------------------\n')

def menu_director():
    print('\n-------------------------------')
    print('      Escogedor de Director      ')
    print('-------------------------------\n')

def menu_editor():
    print('\n-------------------------------')
    print('       Editor de Peliculas       ')
    print('-------------------------------\n')

# ____________________________ Cargar JSON ___________________________ #

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

def cargar_películas():
    with open('datos_json/películas.json') as archivo_películass:
        películas = json.load(archivo_películass)
        return películas

def cargar_comentarios():
    with open('datos_json/comentarios.json') as archivo_comentarioss:
        comentarios = json.load(archivo_comentarioss)
        return comentarios

# ______________________ Iniciar Sesion/Registro _____________________ #

def iniciar_sesión():
    usuarios = requests.get('http://127.0.0.1:5000/users').json()
    while True:
        system("cls") #Limpia la terminal
        INusuario = input("\nIngrese su nombre de usuario: ")
        contador_max = len(usuarios)
        contador = 0
        for usuario in usuarios:
            if INusuario != usuario["username"]:
                contador = contador + 1
                if contador == contador_max:
                    print("\nNombre de usuario inexistente")
                    INopcion = input('\n[1] Para continuar [0] Para salir: ')
                    if INopcion =='1':
                        continue
                    else:
                        return
            elif INusuario == usuario["username"]:
                INcontraseña = input ("\nIngrese su contraseña: ")
                datos_usuarios = cargar_usuarios()
                for usuario in datos_usuarios["users"]:
                    if usuario["username"] == INusuario:
                        if INcontraseña == usuario["password"]:
                            print('\nBienvenido ' + INusuario + '!')
                            return INusuario
                        else: 
                            print ("\nContraseña incorrecta")
                            INopcion = input('\n[1] Para continuar [0] Para salir: ')
                            if INopcion =='1':
                                continue
                            else:
                                return

def registrar_usuario():
    while True:
        system("cls") #Limpia la terminal
        print('\n--------------------------------')
        print('    Registrar nuevo usuario   ')
        print('--------------------------------')
        INnombre_usuario = input("\nIngrese su nombre de usuario: ")
        usuarios = (requests.get('http://127.0.0.1:5000/users').json())
        contador_max = len(usuarios)
        contador = 0
        for usuario in usuarios:
            if INnombre_usuario != usuario["username"]:
                contador = contador + 1 
                if contador == contador_max: # Con esto nos aseguramos que recorra todos los usuarios, y que no sea igual a otro username
                    INcontraseña_usuario = input("\nIngrese su contraseña: ")
                    print ('\nNombre de usuario: ' +  INnombre_usuario)
                    print('Contraseña: ' +  INcontraseña_usuario)
                    print('¿Los datos son correctos?')
                    INopcion = input("\n[1] Para sí [0] Para no: ")
                    if INopcion == '1':
                        nuevo_usuario={
                            "username": INnombre_usuario,
                            "password": INcontraseña_usuario
                        }
                        usuarios = requests.post('http://127.0.0.1:5000/users',json=nuevo_usuario)
                        modificar_json_usuarios(usuarios.json()) # Función que agrega el nuevo usuario al json
                        system("cls") #Limpia la terminal
                        print("¡Usuario creado con éxito!")
                        return (nuevo_usuario["username"])
                    else:
                        return
            else:
                print('\nEl nombre de usuario ', INnombre_usuario, ' ya existe')
                time.sleep(2)
                continue

# __________________________ Modificar JSON __________________________ #

def modificar_json_usuarios(usuarios_actualizado):
    usuarios_json = open ("datos_json/usuarios.json", 'w', encoding='utf-8')
    json.dump(usuarios_actualizado, usuarios_json, indent = 4)
    usuarios_json.close()
    return 

def modificar_json_películas(películas_actualizado):
    películas_json = open ("datos_json/películas.json" , "w" , encoding='utf-8')
    json.dump(películas_actualizado, películas_json, indent = 4)
    películas_json.close()
    return

def modificar_json_comentarios(comentarios_actualizado):
    comentarios_json = open ("datos_json/comentarios.json" , "w" , encoding='utf-8')
    json.dump(comentarios_actualizado, comentarios_json,indent = 4)
    comentarios_json.close()
    return

# ______________________________ Buscar ______________________________ #

def buscar_película_nombre():
    system("cls") #Limpia la terminal
    print('\n--------------------------------')
    print('Buscador de películas por nombre')
    print('--------------------------------\n')
    INpelícula = input("Ingrese el nombre de la película que desea buscar: ")
    film_search = requests.get('http://127.0.0.1:5000/films/'+INpelícula)
    if str(film_search) != '<Response [400]>':
        system("cls") #Limpia la terminal
        print('\nResultados obtenidos = ', len(film_search.json()),"\n")
        for película in film_search.json():
            time.sleep(1)
            print ('===============================')
            print ('Título: ', película["title"])
            print ('Director: ', película["director"])
            print ('Género: ', película["gender"])
            print ('Año: ', película["year"])
            print ('Sinopsis: ', película["synopsis"])
            print ('Imagen representativa: ', película["link_image"])
            print ('-------------------------------')
            print ('Comentarios:')
            print ('-------------------------------')
            buscar_comentarios(película["title"])
            print ('===============================\n')
        return
    else:
        print ("\nPelícula inexistente")
        return

def buscar_película_director():
    system("cls") #Limpia la terminal
    director = elegir_director()
    director_search = requests.get('http://127.0.0.1:5000/films/directors/'+director)
    if str(director_search) != '<Response [400]>':
        system("cls") #Limpia la terminal
        print ('\nPelículas disponibles de ', director, len(director_search.json()),"\n")
        for película in director_search.json():
            time.sleep(1)
            print ('===============================')
            print ('Título: ', película["title"])
            print ('Director: ', película["director"])
            print ('Género: ', película["gender"])
            print ('Año: ', película["year"])
            print ('Sinopsis: ', película["synopsis"])
            print ('Imagen representativa: ', película["link_image"])
            print ('-------------------------------')
            print ('Comentarios:')
            print ('-------------------------------')
            buscar_comentarios(película["title"])
            print ('===============================\n')
        return
    else:
        print ('\nAún no hay películas publicadas de', director)
        return

def buscar_película_género():
    system("cls") #Limpia la terminal
    genero = elegir_genero()
    genero_search = requests.get('http://127.0.0.1:5000/films/gender/'+genero)
    if str(genero_search) != '<Response [400]>':
        system("cls") #Limpia la terminal
        print ('\nPelículas disponibles de ', genero, len(genero_search.json()),"\n")
        for película in genero_search.json():
            time.sleep(1)
            print ('===============================')
            print ('Título: ', película["title"])
            print ('Director: ', película["director"])
            print ('Género: ', película["gender"])
            print ('Año: ', película["year"])
            print ('Sinopsis: ', película["synopsis"])
            print ('Imagen representativa: ', película["link_image"])
            print ('-------------------------------')
            print ('Comentarios:')
            print ('-------------------------------')
            buscar_comentarios(película["title"])
            print ('===============================\n')
        return
    else:
        print ('\nAún no hay películas publicadas de', genero)
        return

def buscar_id(usuario_logueado):
    usuario_info = requests.get('http://127.0.0.1:5000/user/'+usuario_logueado).json()
    return usuario_info["id"]

# _________________________ Comprobar año/url ________________________ #

def comprobar_url():
    while True:
        url_imagen = input("Ingrese la URL a la portada de la pelicula: ")
        url = re.compile("^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$")
        if url.search(url_imagen): # Comprobemos que sea una URL válida
            print("URL válida")
            return(url_imagen)
        else:
            print("URL no válida")
            print("Ejemplo URL válida: https://www.google.com/")
            continue

def comprobar_año():
    while True:
        año = input("Ingrese el año de la pelicula: ")
        if año.isdigit():
            if int(año) >= 1900 and int(año) <= 2023:
                return (año)
        print("Año no válido")

# _____________________ Agregar/Editar/Eliminar Pelicula ______________________ #

def agregar_película():
    películas = requests.get('http://127.0.0.1:5000/films').json()
    time.sleep(0.2)
    system("cls") #Limpia la terminal
    print('\nUsted escogió, "Agregar Pelicula". Recuerde que los generos y directores, solo pueden ser escogidos entre los')
    print('ya cargados en el sistema.')
    comprobador = True
    while comprobador:
        title_movie = input("\nIngrese el titulo de la pelicula que desea añadir: ")
        for película in películas:
            if película["title"].capitalize() == title_movie.capitalize():
                system("cls") #Limpia la terminal
                print("Ya existe una película con ese título!")
                time.sleep(2)
                return
        genero = elegir_genero()
        director = elegir_director()
        year_movie = comprobar_año()
        synopsis_movie = input("Ingrese la sinopsis de la pelicula que desea añadir: ")
        img_movie = comprobar_url()
        new_movie ={
            "title": title_movie.capitalize(),
            "year": year_movie,
            "director": director,
            "gender": genero,
            "synopsis": synopsis_movie.capitalize(),
            "link_image": img_movie
            }
        print("\nEsta seguro que desea añadir esta pelicula?\n")
        print (new_movie)
        op = input("\nOpcion [1] Si [2] No : ")
        if op == "1":
            películas = requests.post('http://127.0.0.1:5000/films',json=new_movie)
            modificar_json_películas(películas.json())
            system("cls") #Limpia la terminal
            print("\nUsted añadió correctamente su pelicula!")
            time.sleep(2)
            comprobador = False
        if op == "2":
            return
        continue

def editar_película():
    menu_editor()
    time.sleep(0.2)
    película_user = elegir_película_a_editar()
    película_lista = requests.get('http://127.0.0.1:5000/films/'+película_user).json()
    película = película_lista[0]
    nueva_película = {}
    print("\nDesea editar el director? [Director Actual: " + str(película["director"]) + "] ")
    op = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
    if op == "1":
        new_director = elegir_director()
        nueva_película["director"] = new_director
    print("\nDesea editar el genero? [Genero Actual: " + str(película["gender"] + "] "))
    op = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
    if op == "1":
        new_gender = elegir_genero()
        nueva_película["gender"] = new_gender
    print("\nDesea editar la URL a la portada? [URL Actual: " + str(película["link_image"] + "] "))
    op = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
    if op == "1":
        new_url = comprobar_url()
        nueva_película["link_image"] = new_url
    print("\nDesea editar la sinopsis? [Sinopsis Actual: " + str(película["synopsis"] + "] "))
    op = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
    if op == "1":
        new_synopsis = input("Ingrese la nueva sinopsis: ")
        nueva_película["synopsis"] = new_synopsis
    print("\nDesea editar el año? [Año Actual: " + str(película["year"] + "] "))
    op = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
    if op == "1":
        new_year = comprobar_año()
        nueva_película["year"] = new_year
    print("\nEsta seguro que desea editar esta pelicula?\n")
    print (nueva_película)
    op = input("\nOpcion [1] Si [2] No : ")
    if op == "1":
        películas_mod = requests.put('http://127.0.0.1:5000/films/'+película_user, json=nueva_película).json()
        modificar_json_películas(películas_mod)
        system("cls") #Limpia la terminal
        print('Se modificó '+película_user+' correctamente')
        modificar_json_películas(películas_mod)
        time.sleep(2)
    if op == "2":
        return

def eliminar_película(usuario_logueado):
    system("cls") #Limpia la terminal
    print('\nUsted escogió, "Eliminar película"')
    película_eliminar = elegir_película_a_eliminar()
    if película_eliminar == None:
        return
    comentarios_película = requests.get('http://127.0.0.1:5000/films/'+película_eliminar+'/comments').json()
    if len(comentarios_película) > 1:
        system("cls") #Limpia la terminal
        print("No puedes borrar una película con comentarios de otras personas")
        time.sleep(2)
        return
    elif comentarios_película == []:
        print('\n¿Está seguro que quiere eliminar '+película_eliminar+'?')
        opcion = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
        if opcion == "1":
            nuevo_json = requests.delete('http://127.0.0.1:5000/films/'+película_eliminar).json()
            system("cls") #Limpia la terminal
            print('Se eliminó '+película_eliminar+' correctamente')
            modificar_json_películas(nuevo_json)
            time.sleep(2)
            return
        else:
            return
    else: 
        coincidencias = 0
        for comentario in comentarios_película:
            if comentario["username"] == usuario_logueado:
                coincidencias = coincidencias + 1
        if coincidencias == 0:
            system("cls") #Limpia la terminal
            print("No puedes borrar una película con comentarios de otras personas")
            time.sleep(2)
            return
        elif coincidencias == 1:
            for comentario in comentarios_película:
                if comentario["username"] == usuario_logueado:
                    print('\n¿Está seguro que quiere eliminar '+película_eliminar+'?')
                    opcion = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
                    if opcion == "1":
                        nuevo_json = requests.delete('http://127.0.0.1:5000/films/'+película_eliminar).json()
                        eliminar_comentarios_película(película_eliminar, usuario_logueado)
                        system("cls") #Limpia la terminal
                        print('Se eliminó '+película_eliminar+' correctamente')
                        modificar_json_películas(nuevo_json)
                        time.sleep(2)
                        return
                    else:
                        return

# ________________________ Agregar/Editar/Eliminar Comentario _________________________ #

def agregar_comentario(usuario_logueado):
    comentarios_usuario = requests.get('http://127.0.0.1:5000/users/'+usuario_logueado+'/comments').json()
    comentarioss = []
    if comentarios_usuario != {}:
        print ("\nSus comentarios actualmente son:\n")
    for comentario in comentarios_usuario:
        print (str(comentario["film"]) + '  -  ' + str(comentario["comment"]))
        comentarioss.append({
            "film":comentario["film"],
            "comment":comentario["comment"]
        })
    if comentarioss == []:
        print ("\nAún no hay comentarios")
    while True:
        op = input ("\nDesea agregar algun comentario? [1 Sí] [2 No]: ")
        if op == "1":
            película_a_comentar = elegir_película_a_comentar()
            coincidencias = 0
            for película in comentarios_usuario:
                if película_a_comentar == película["film"]:
                    coincidencias = + 1
            if coincidencias == 0:
                new_comment = input("\nQue comentario desea agregar en '" + película_a_comentar + "': ")
                new_content = {
                    "username" : usuario_logueado,
                    "film" : película_a_comentar,
                    "comment" : new_comment,
                }
                comentarios = requests.post('http://127.0.0.1:5000/users/' + usuario_logueado + '/comments',json=new_content)
                modificar_json_comentarios(comentarios.json())
                print("\nComentario añadido correctamente!")
                time.sleep(2)
                return
            else:
                print("\nYa has realizado un comentario en esta pelicula!")
                print("[Recuerde que no se puede realizar mas de un comentario en la misma película. Debe volver al")
                print("menu principal y modificar el comentario ya existente]")
            continue
        elif op == "2":
            return
        else:
            print("\nError! Debe de escoger entre '1' y '2' segun sus preferencias")

def editar_comentario(usuario_logueado):
    comentarios_usuario = requests.get('http://127.0.0.1:5000/users/'+usuario_logueado+'/comments').json()
    lista_comentarios = []
    lista_películas = []
    contador = 1
    print ('\nSus comentarios son los siguientes...')
    print ('\n[0] Para salir')
    for comentario in comentarios_usuario:
            print ('[' + str(contador) + '] ' + str(comentario["film"]) + '  -  ' + str(comentario["comment"]))
            lista_comentarios.append({
                comentario["film"]: comentario["comment"]
            })
            lista_películas.append(comentario["film"])
            contador = contador + 1
            time.sleep(0.5)
    if lista_comentarios == []:
        print ("\nAún no hay comentarios")
    while True:
        opcion_comentario = input("\nElija una opción: ")
        if opcion_comentario.isdigit() == True:
            if int(opcion_comentario) <= len(comentarios_usuario) and int(opcion_comentario) >= 0:
                if int(opcion_comentario) == 0:
                    return
                else:
                    nuevo_comentario = input("Ingrese su comentario modificado: ")
                    pelicula_nombre = lista_películas[int(opcion_comentario)-1] 
                    comentarios_modificado = {"film": pelicula_nombre, "comment": nuevo_comentario}
                    datos_actualizados = requests.put('http://127.0.0.1:5000/users/'+usuario_logueado+'/comments', json=comentarios_modificado).json()
                    modificar_json_comentarios(datos_actualizados)
                    system("cls") #Limpia la terminal
                    print("¡Comentario modificado con éxito!")
                    time.sleep(2)
                    return (lista_comentarios[int(opcion_comentario)-1])
        print("\nError! Dato ingresado inválido")

def eliminar_comentario(usuario_logueado):
    comentarios = cargar_comentarios()
    película = elegir_película_borrar_comentario()
    comentarioss = []
    if comentarios != []:
        for comentario in comentarios["comments"]:
            if usuario_logueado == comentario["username"]:
                if película == comentario["film"]:
                    comentarioss.append({
                        "username": comentario["username"],
                        "film": película,
                        "comment": comentario["comment"]}
                    )
    if comentarioss == [] or comentarios == []:
        print("\nNo existe ningún comentario en esa película")
        time.sleep(2)
        return 
    else:
        print("\nEstá seguro que desea borrar su comentario '" + str(comentarioss[0]["comment"]) + "' en la película '" + str(comentarioss[0]["film"]) + "'?")
        opcion = input("\n[Presione 1 para sí] [Cualquier otra tecla para no]: ")
        if opcion == "1":
            nuevo_json = requests.delete('http://127.0.0.1:5000/users/'+ usuario_logueado + '/comments', json= {"film" : película}).json()
            system("cls") #Limpia la terminal
            print("Se eliminó su comentario " + str(comentarioss[0]["comment"]) +" de la película '" + str(comentarioss[0]["film"]) + "' correctamente")
            modificar_json_comentarios(nuevo_json)
            time.sleep(2)
            return
        else:
            return

def eliminar_comentarios_película(película,usuario_logueado):
    nuevo_json = requests.delete('http://127.0.0.1:5000/users/'+ usuario_logueado + '/comments', json= {"film" : película}).json()
    modificar_json_comentarios(nuevo_json)
    return

# _____________________ Seleccion info pelicula ______________________ #

def elegir_película_borrar_comentario():
    print("\nA continuación se mostrarán las películas ...\n")
    películas = cargar_películas()
    time.sleep(2)
    lista_películas = []
    contador = 1
    for película in películas["films"]:
        print ('[' + str(contador) + '] ' + str(película["title"]))
        lista_películas.append(película)
        contador = contador + 1
        time.sleep(0.5)
    while True:
        opcion_película = input("\nEn que pelicula desea borrar su comentario? ")
        if opcion_película.isdigit() == True:
            if int(opcion_película) <= len(películas["films"]) and int(opcion_película) >= 0:
                if int(opcion_película) == 0:
                    return
                else: 
                    return (lista_películas[int(opcion_película)-1]["title"])
        print("\nError! Dato ingresado inválido")

def elegir_película_a_comentar():
    print("\nA continuación se mostrarán las películas disponibles a comentar ...\n")
    películas = cargar_películas()
    time.sleep(2)
    lista_películas = []
    contador = 1
    for película in películas["films"]:
        print ('[' + str(contador) + '] ' + str(película["title"]))
        lista_películas.append(película)
        contador = contador + 1
        time.sleep(0.5)
    while True:
        opcion_película = input("\nQue pelicula desea comentar? ")
        if opcion_película.isdigit() == True:
            if int(opcion_película) <= len(películas["films"]) and int(opcion_película) >= 0:
                if int(opcion_película) == 0:
                    return
                else: 
                    return (lista_películas[int(opcion_película)-1]["title"])
        print("\nError! Dato ingresado inválido")

def elegir_película_a_editar():
    print("\nA continuación se mostrarán las películas disponibles ...\n")
    print("[Recuerde que el género y el director, solo se pueden elegir según los ya provistos por el sistema.]\n")
    películas = cargar_películas()
    time.sleep(2)
    lista_películas = []
    contador = 1
    print ('[0] Para salir')
    for película in películas["films"]:
        print ('[' + str(contador) + '] ' + str(película["title"]))
        lista_películas.append(película)
        contador = contador + 1
        time.sleep(0.5)
    while True:
        opcion_película = input("\nQue pelicula desea editar? ")
        if opcion_película.isdigit() == True:
            if int(opcion_película) <= len(películas["films"]) and int(opcion_película) >= 0:
                if int(opcion_película) == 0:
                    return
                else: 
                    return (lista_películas[int(opcion_película)-1]["title"])
        print("\nError! Dato ingresado inválido")

def elegir_película_a_eliminar():
    system("cls") #Limpia la terminal
    print("\nA continuación se mostrarán las películas disponibles ...\n")
    películas = cargar_películas()
    time.sleep(2)
    lista_películas = []
    contador = 1
    print ('[0] Para salir')
    for película in películas["films"]:
        print ('[' + str(contador) + '] ' + str(película["title"]))
        lista_películas.append(película)
        contador = contador + 1
        time.sleep(0.5)
    while True:
        opcion_película = input("\n¿Qué pelicula desea eliminar? ")
        if opcion_película.isdigit() == True:
            if int(opcion_película) <= len(películas["films"]) and int(opcion_película) >= 0:
                if int(opcion_película) == 0:
                    return
                else: 
                    return (lista_películas[int(opcion_película)-1]["title"])
        print("\nError! Dato ingresado inválido")

def elegir_genero():
    menu_genero()
    generos = cargar_generos()
    print("A continuación se mostrarán los generos disponibles ...\n")
    time.sleep(2)
    i = 0
    for genero in generos["genders"]:
        print ('[' + str(i) + '] ' + str(genero["gender"]))
        time.sleep(0.5)
        i = i + 1
    genero = "vacío"
    while genero == "vacío":
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
        else:
            print("\nError! Debe ingresar el numero que corresponda segun el genero que desea.")
    return genero

def elegir_director():
    menu_director()
    directores = cargar_directores()
    print("A continuacion se mostrarán los directores disponibles ...\n")
    time.sleep(2)
    i = 0
    for director in directores["directors"]:
        print ('[' + str(i) + '] ' + str(director["director"]))
        time.sleep(0.5)
        i = i + 1
    director = "vacío"
    while director == "vacío":
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
        else:
            print("Error! Debe ingresar el numero que corresponda segun el director que desea.")
    return director

# ____________________________ Ultimas 10 ____________________________ #

def ultimas_diez():
    ultimas10 = requests.get('http://127.0.0.1:5000/films/last10')
    system("cls") #Limpia la terminal
    print('\nÚltimas 10 películas cargadas al sistema:',"\n")
    for película in ultimas10.json():
        time.sleep(1)
        print ('===============================')
        print ('Título: ', película["title"])
        print ('Director: ', película["director"])
        print ('Género: ', película["gender"])
        print ('Año: ', película["year"])
        print ('Sinopsis: ', película["synopsis"])
        print ('Imagen representativa: ', película["link_image"])
        print ('-------------------------------')
        print ('Comentarios:')
        print ('-------------------------------')
        buscar_comentarios(película["title"])
        print ('===============================\n')
    return

# _________________________ Buscar Comentario ________________________ #

def buscar_comentarios(film_title):
    comentarios_película = requests.get('http://127.0.0.1:5000/films/'+film_title+'/comments').json()
    if comentarios_película != []:
        for comentario in comentarios_película:
            print ('Usuario: ', comentario["username"])
            print ('Comentario: ', comentario["comment"])
            print ('-------------------------------')
    else:
        print ("Sin comentarios")
        print ('-------------------------------')
        return

# _______________________________________________________________ Código __________________________________________________________________ #

bucle = 1 # Lo usaremos para luego romper el bucle
while bucle == 1:
    INopcion = menu_principal()
    if INopcion == '1':
        usuarioIN = iniciar_sesión()
        if usuarioIN == None:
            continue
        while True:
            INopcion = menu_usuario(usuarioIN) #Nombre de usuario
            if INopcion == '1': # Agregar película
                agregar_película()
                continue
            elif INopcion == '2': # Editar película
                editar_película()
            elif INopcion == '3': # Borrar película
                eliminar_película(usuarioIN)
            elif INopcion == '4': # Agregar comentario
                agregar_comentario(usuarioIN)
            elif INopcion == '5': # Editar comentario
                editar_comentario(usuarioIN)
            elif INopcion == '6': # Borrar comentario
                eliminar_comentario(usuarioIN)
            elif INopcion == '7': # Menú buscar
                INopcion = menu_buscar()
                if INopcion == '1': # Buscar por nombre
                    buscar_película_nombre()
                    INopcion = input("\nIngrese algo para volver al menú: ")
                    continue
                elif INopcion == '2': # Buscar por director
                    buscar_película_director()
                    INopcion = input("\nIngrese algo para volver al menú: ")
                    continue
                elif INopcion == '3': # Buscar por género
                    buscar_película_género()
                    INopcion = input("\nIngrese algo para volver al menú: ")
                    continue
                elif INopcion == '0': # Salir
                    continue
            elif INopcion == '0': # Salir
                break
    elif INopcion == '2': # Modo público
        ultimas_diez()
        INopcion = input("\nIngrese algo para volver al menú: ")
        continue
    elif INopcion == '3': # Registrar nuevo usuario
        nuevo_usuario = registrar_usuario()
        if nuevo_usuario == None:
            continue
        else:
            time.sleep(3)
            continue
    elif INopcion == '0': # Salir
        exit
    bucle = 0 # Para romper el bucle