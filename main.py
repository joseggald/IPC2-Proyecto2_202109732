
import xml.etree.ElementTree as ET
from xml.dom import minidom
from time import sleep
from claseEscritorios import Escritorio

opConfig=0
fin=100
escri=[]

while fin==100:
    print("***** PROYECTO 2: LABORATORIO DE IPC 2 *****")
    print("")
    print("1. Configuración de empresas")
    print("2. Selección de empresa y punto de atención")
    print("3. Manejo de puntos de atención")
    print("4. Salir")
    op=int(input())
    if op==1:
        while(opConfig>5 or opConfig==0):
            
            print("*** Configuración de empresas ***")
            print("")
            print(" 1. Limpiar sistema ")
            print(" 2. Cargar archivo de configuración del sistema ")
            print(" 3. Crear nueva empresa ")
            print(" 4. Cargar archivo con configuración inicial para la prueba ")
            print(" 5. Regresar Menu Principal")
            opConfig=int(input())
            if opConfig==1:
                sleep(2)
                print("...")
                sleep(2)
                print("...")
                sleep(2)
                print("...")
                sleep(2)
                print("*** SISTEMA LIMPIO ***")
            if opConfig==2:
                parser = ET.XMLParser(encoding="utf-8")
                tree = ET.parse('a.xml',parser=parser)
                root = tree.getroot()
                for empresa in root:
                    print("***********************************************************")
                    idEmpresa = empresa.attrib['id']
                    print(idEmpresa)
                    for contenido in empresa:
                        if contenido.tag == 'nombre':
                            NombreEmpresa = contenido.text
                            print(NombreEmpresa)
                        if contenido.tag == 'abreviatura':
                            AbreviaturaEmpresa = contenido.text
                            print(AbreviaturaEmpresa)
                        for listaPA in contenido:
                            if listaPA.tag == 'puntoAtencion': 
                                idPA = listaPA.attrib['id']
                                print(idPA)
                                for contPA in listaPA:
                                    if contPA.tag == 'nombre':
                                        nombrePA=contPA.text
                                        print(nombrePA)
                                    if contPA.tag == 'direccion':
                                        direccionPA=contPA.text
                                        print(direccionPA)
                                    for listaEscritorio in contPA:
                                        if listaEscritorio.tag == 'escritorio':
                                            idEscritorio = listaEscritorio.attrib['id']
                                            print(idEscritorio)
                                            for escritorios in listaEscritorio:
                                                if escritorios.tag == 'identificacion':
                                                    identificacion=escritorios.text
                                                    print(identificacion)
                                                if escritorios.tag == 'encargado':
                                                    encargado=escritorios.text
                                                    print(encargado)
                        for listaTS in contenido:
                            if listaTS.tag == 'transaccion': 
                                idTS = listaTS.attrib['id']
                                print(idTS)
                                for contTS in listaTS:
                                    if contTS.tag == 'nombre':
                                        nombreTS=contTS.text
                                        print(nombreTS)
                                    if contTS.tag == 'tiempoAtencion':
                                        tiempoAtencion=contTS.text
                                        print(tiempoAtencion)

            if opConfig==3:
                pass
            if opConfig==4:
                pass
            if opConfig==5:
                pass
            if opConfig>5 or opConfig==0:
                print("Opcion no valida!")
                print("Vuelva a intentarlo...")
    if op==2:
        print("*** Selección de empresa y punto de atención ***")
        print("")
    if op==3:
        print("*** Manejo de puntos de atención ***")
        print("")
    if op==4:
        fin=0
    if op>4 or op==0:
        print("Opcion no valida!")
        print("Vuelva a intentarlo...")
        
        

