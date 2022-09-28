import os
from re import L
from telnetlib import PRAGMA_HEARTBEAT
from webbrowser import get
import xml.etree.ElementTree as ET
from xml.dom import minidom
from time import sleep
from ListaSimple import Lista_simple
from claseEmpresa import Empresa
from claseEscritorios import Escritorio
from clasePuntoAtencion import PuntoAtencion
from claseTransaccion import Transaccion
listaEscritorios=Lista_simple()
opConfig=0
fin=100

escritoriosData=[]
puntosAtData=[]
empresaData=[]
transaccionData=[]


prueba=[]
while fin==100:
    print("***** PROYECTO 2: LABORATORIO DE IPC 2 *****")
    print("")
    print("1. Configuración de empresas")
    print("2. Selección de empresa y punto de atención")
    print("3. Manejo de puntos de atención")
    print("4. Salir")
    op=int(input())
    if op==1:
        opConfig=100
        while(opConfig!=5):
            os.system ("cls")
            print("*** Configuración de empresas ***")
            print("")
            print(" 1. Limpiar sistema ")
            print(" 2. Cargar archivo de configuración del sistema ")
            print(" 3. Crear nueva empresa ")
            print(" 4. Cargar archivo con configuración inicial para la prueba ")
            print(" 5. Regresar Menu Principal")
            opConfig=int(input())
            if opConfig==1:
                os.system ("cls")
                sleep(2)
                print("...")
                sleep(2)
                print("...")
                sleep(2)
                print("...")
                sleep(2)
                print("*** SISTEMA LIMPIO ***")
            if opConfig==2:
                os.system ("cls")
                print("***** 2. Cargar archivo de configuración del sistema *****")
                parser = ET.XMLParser(encoding="utf-8")
                tree = ET.parse('a.xml',parser=parser)
                root = tree.getroot()
                for empresa in root:
                    puntosAtData.clear()
                    escritoriosData.clear()
                    transaccionData.clear()
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
                                            
                                            escritoriosData.append(Escritorio(idEscritorio, identificacion,encargado))
                                prueba.append(PuntoAtencion(idPA, nombrePA,direccionPA,escritoriosData))            
                                puntosAtData.append(PuntoAtencion(idPA, nombrePA,direccionPA,escritoriosData))                       
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
                                transaccionData.append(Transaccion(idTS,nombreTS,tiempoAtencion))
                    empresaData.append(Empresa(idEmpresa,NombreEmpresa,AbreviaturaEmpresa,puntosAtData,transaccionData))
                

                print("********************* DATA OBTENIDA ***************************")
                """
                print(str(len(empresaData)))
                for i in range(len(empresaData)):
                    print(empresaData[i].nombre)
                    for k in range(len(empresaData[i].puntosAtencion)):
                        for j in range(len(empresaData[i].puntosAtencion[k].escritorios)):
                            print(empresaData[i].puntosAtencion[k].escritorios[j].idEsc)
                """   
                sleep(5)                           
            if opConfig==3:
                os.system ("cls")
                print("***** 3. Crear nueva empresa *****")
                
            if opConfig==4:
                os.system ("cls")
                print("***** 4. Cargar archivo con configuración inicial para la prueba *****")
                parser = ET.XMLParser(encoding="utf-8")
                tree = ET.parse('1.xml',parser=parser)
                root = tree.getroot()
                for config in root:
                    idConfig = config.attrib['id']
                    print(idConfig)
                    for escriActi in config:
                        for listaEscri in escriActi:
                            if listaEscri.tag == 'escritorio':
                                idEscri=listaEscri.attrib['idEscritorio']
                                print(idEscri)
                    for clientes in config:
                        for listaClientes in clientes:
                            if listaClientes.tag == 'cliente':
                                idClientes=listaClientes.attrib['dpi']
                                print(idClientes)
                                for datos in listaClientes:
                                    if datos.tag == 'nombre':
                                        nomCliente=datos.text
                                        print(nomCliente)
                                    for trans in datos:
                                        if trans.tag=='transaccion':
                                            idTrans=trans.attrib['idTransaccion']
                                            print(idTrans)
                
                sleep(10)
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
        
        

