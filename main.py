import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from time import sleep
from ListaSimple import Lista_simple
from claseCI import ConfigInicial
from claseClientes import Clientes
from claseEmpresa import Empresa
from claseEscritorios import Escritorio
from clasePuntoAtencion import PuntoAtencion
from claseTransaccion import Transaccion

opConfig=0
fin=100
empresaData=Lista_simple()
empresaLista=[]
configData=Lista_simple()
configLista=[]
actualSeleccionEmpresa=100
actualSeleccionPunto=100
while fin==100:
    os.system ("cls")
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
                empresaData=Lista_simple()
                empresaLista.clear()
                configData=Lista_simple()
                configLista.clear()
                actualSeleccion=None
                
                print("...")
                sleep(2)
                print("...")
                sleep(2)
                print("...")
                sleep(2)
                print("*** SISTEMA LIMPIO ***")
                sleep(5)
            if opConfig==2:
                estInicial=False
                os.system ("cls")
                print("***** 2. Cargar archivo de configuración del sistema *****")
                parser = ET.XMLParser(encoding="utf-8")
                tree = ET.parse('a.xml',parser=parser)
                root = tree.getroot()
                for empresa in root:
                    idEmpresa = empresa.attrib['id']
                    print(idEmpresa)
                    escritoriosData=Lista_simple()
                    escritoriosLista=[]
                    puntosAtData=Lista_simple()
                    puntosAtLista=[]
                    transaccionData=Lista_simple()
                    clientesData=Lista_simple()
                    transaccionLista=[]  
                    clientesLista=[]                  
                    for contenido in empresa:  
                        if contenido.tag == 'nombre':
                            NombreEmpresa = contenido.text
                        if contenido.tag == 'abreviatura':
                            AbreviaturaEmpresa = contenido.text                 
                        for listaPA in contenido:  
                            if listaPA.tag == 'puntoAtencion': 
                                idPA = listaPA.attrib['id']  
                                for contPA in listaPA:
                                    if contPA.tag == 'nombre':
                                        nombrePA=contPA.text
                                    if contPA.tag == 'direccion':
                                        direccionPA=contPA.text
                                    for listaEscritorio in contPA:
                                        if listaEscritorio.tag == 'escritorio':
                                            idEscritorio = listaEscritorio.attrib['id']
                                            for escritorios in listaEscritorio:
                                                if escritorios.tag == 'identificacion':
                                                    identificacion=escritorios.text
                                                if escritorios.tag == 'encargado':
                                                    encargado=escritorios.text   
                                            escritoriosData.agregar_al_final(Escritorio(idEscritorio, identificacion,encargado,estInicial))
                                            escritoriosLista.append(Escritorio(idEscritorio, identificacion,encargado,estInicial))
                                puntosAtData.agregar_al_final(PuntoAtencion(idPA, nombrePA,direccionPA,escritoriosData))   
                                puntosAtLista.append(PuntoAtencion(idPA, nombrePA,direccionPA,escritoriosLista))                                                                       
                        for listaTS in contenido:
                            if listaTS.tag == 'transaccion': 
                                idTS = listaTS.attrib['id']
                                for contTS in listaTS:
                                    if contTS.tag == 'nombre':
                                        nombreTS=contTS.text
                                    if contTS.tag == 'tiempoAtencion':
                                        tiempoAtencion=int(contTS.text)
                                transaccionData.agregar_al_final(Transaccion(idTS,nombreTS,tiempoAtencion))
                                transaccionLista.append(Transaccion(idTS,nombreTS,tiempoAtencion))
                    empresaData.agregar_al_final(Empresa(idEmpresa,NombreEmpresa,AbreviaturaEmpresa,puntosAtData,transaccionData,clientesData))
                    empresaLista.append(Empresa(idEmpresa,NombreEmpresa,AbreviaturaEmpresa,puntosAtLista,transaccionLista,clientesLista))
                print("") 
                print("Se han obtenido un total de: "+str(len(empresaLista))+" Empresas.")  
                print("")  
                print("********************* PROCESO COMPLETADO ***************************")  
                sleep(5)                                     
            if opConfig==3:
                
                stop=False  
                while(stop!=True):
                    escritoriosData=Lista_simple()
                    escritoriosLista=[]
                    puntosAtData=Lista_simple()
                    puntosAtLista=[]
                    transaccionData=Lista_simple()
                    clientesData=Lista_simple()
                    clientesLista=[]
                    transaccionLista=[]
                    os.system ("cls")
                    print("***** 3. Crear nueva empresa *****")
                    print("")

                    print("Ingrese el id de Empresa: ")
                    id_empresa=input()
                    if len(empresaLista)==0:
                        stop=True
                    for i in range(len(empresaLista)):
                        if id_empresa==empresaLista[i].idEmpresa:
                            stop=False
                            break
                        else:
                            stop=True
                    if stop==False:
                        print("Empresa ya existente con ese id, porfavor vuelva a intertalo.")
                os.system ("cls")
                print("Ingrese el nombre de la Empresa: ")
                nom_empresa=input()
                print("Ingrese la abreviatura de la Empresa: ")
                abre_empresa=input()
                print("Ingrese la cantidad de puntos de atención: ")
                tam_pta=int(input())
                for j in range(tam_pta):
                    os.system ("cls")
                    print("**** PUNTO DE ATENCION "+str(j+1)+" ****")
                    print("")
                    print("Ingrese el id de puntos de atención No. "+str(j+1)+":")
                    id_pta=input()
                    print("Ingrese el nombre de puntos de atención No. "+str(j+1)+":")
                    nom_pta=input()
                    print("Ingrese la direccion de puntos de atención No. "+str(j+1)+":")
                    dic_pta=input()
                    print("Ingrese la cantidad de escritorios de puntos de atención No. "+str(j+1)+":")
                    escri_tam=int(input())
                    for k in range(escri_tam):
                        os.system ("cls")
                        print("**** ESCRITORIO "+str(k+1)+" ****")
                        print("")
                        print("Ingrese el id del escritorio No. "+str(k+1)+":")
                        id_escri=input()
                        print("Ingrese la identificacion del escritorio No. "+str(k+1)+":")
                        iden_escri=input()
                        print("Ingrese el encargado del escritorio No. "+str(k+1)+":")
                        encar_escri=input()
                        escritoriosLista.append(Escritorio(id_escri, iden_escri,encar_escri, False))
                    puntosAtLista.append(PuntoAtencion(id_pta, nom_pta, dic_pta, escritoriosLista))

                os.system ("cls")    
                print("Ingrese la cantidad de transacciones: ")
                tam_trans=int(input())   
                for i in range(tam_trans):
                    os.system ("cls")
                    print("**** TRANSACCION "+str(i+1)+" ****")
                    print("")
                    print("Ingrese el id de la transaccion No. "+str(i+1)+":")     
                    id_trans=input()
                    print("Ingrese el nombre de la transaccion No. "+str(i+1)+":")   
                    nom_trans=input()
                    print("Ingrese el tiempo de atencion de la transaccion No. "+str(i+1)+":")   
                    tiempo_trans=int(input())
                    transaccionLista.append(Transaccion(id_trans, nom_trans, tiempo_trans))
                empresaLista.append(Empresa(id_empresa,nom_empresa,abre_empresa, puntosAtLista,transaccionLista,clientesLista))
                empresaData.agregar_al_final(Empresa(id_empresa,nom_empresa,abre_empresa, puntosAtLista,transaccionLista,clientesLista))
                os.system ("cls")
                print("Cargando informacion...")
                sleep(5)
                print("********************* PROCESO COMPLETADO ***************************")  
                sleep(5)
            if opConfig==4:
                os.system ("cls")
                print("***** 4. Cargar archivo con configuración inicial para la prueba *****")
                parser = ET.XMLParser(encoding="utf-8")
                tree = ET.parse('1.xml',parser=parser)
                root = tree.getroot()
                
                try:
                
                    for config in root:
                        idConfig = config.attrib['id']
                        idEmpresa = config.attrib['idEmpresa']
                        idPunto = config.attrib['idPunto']

                        agregar=False
                        clientesLista=[] 
                        transaccionLista=[]
                        cantLista=[]
                        escritoriosActivos=[]
                        clientesData=Lista_simple()
                        transaccionData=Lista_simple()
                    
                        for i in range(len(empresaLista)):
                            if idEmpresa==empresaLista[i].idEmpresa:  
                                for j in range(len(empresaLista[i].puntosAtencion)):
                                    if idPunto==empresaLista[i].puntosAtencion[j].idPuntoAtencion:   
                                        for escriActi in config:
                                            for listaEscri in escriActi:
                                                if listaEscri.tag == 'escritorio':
                                                    idEscri=listaEscri.attrib['idEscritorio']
                                                    for k in range(len(empresaLista[i].puntosAtencion[j].escritorios)):
                                                        escri=empresaLista[i].puntosAtencion[j].escritorios[k]
                                                        if idEscri==empresaLista[i].puntosAtencion[j].escritorios[k].idEsc:
                                                            empresaLista[i].puntosAtencion[j].escritorios[k].estado=True
                                                            escritoriosActivos.append(Escritorio(escri.idEsc,escri.identificacion,escri.encargado, escri.estado))
                                                            agregar=True
                                                        else:
                                                            pass
                                        for clientes in config:
                                            for listaClientes in clientes:
                                                if listaClientes.tag == 'cliente':
                                                    idClientes=listaClientes.attrib['dpi']   
                                                    for datos in listaClientes:
                                                        if datos.tag == 'nombre':
                                                            nomCliente=datos.text      
                                                        for trans in datos:
                                                            if trans.tag=='transaccion':
                                                                idTrans=trans.attrib['idTransaccion']
                                                                cantidadTrans=int(trans.attrib['cantidad'])
                                                                for a in range(len(empresaLista[i].transacciones)):
                                                                    dato=empresaLista[i].transacciones[a]
                                                                    if empresaLista[i].transacciones[a].idTrans==idTrans:
                                                                        transaccionLista.append(Transaccion(dato.idTrans,dato.nombre,dato.tiempo)) 
                                                                        cantLista.append(cantidadTrans)
                                                    clientesLista.append(Clientes(idClientes,nomCliente,transaccionLista,cantLista))
                                    else:
                                        pass
                                empresaLista[i].clientes=clientesLista
                            else:
                                pass
                                
                        if agregar==True:            
                            configLista.append(ConfigInicial(idConfig,idEmpresa,idPunto,escritoriosActivos,clientesLista))
                            configData.agregar_al_final(ConfigInicial(idConfig,idEmpresa,idPunto,escritoriosActivos,clientesLista))
                    print("") 
                    print("Se han obtenido un total de: "+str(len(configLista))+" Configuraciones Iniciales.")  
                    print("")  
                    print("********************* PROCESO COMPLETADO ***************************")       
                    sleep(5)
                except:
                    print("Revise su archivo xml.")  
                    print("")
                    print("********************* PROCESO NO COMPLETADO ***************************")   
            if opConfig==5:
                pass
            if opConfig>5 or opConfig==0:
                print("Opcion no valida!")
                print("Vuelva a intentarlo...")
    if op==2:
        
        
        
        while(actualSeleccionEmpresa>len(empresaLista)):
            os.system ("cls")
            print("*** Selección de empresa y punto de atención ***")
            print("")
            print("Empresas disponibles: "+str(len(empresaLista)))
            print("")
            print("_________________________________________________")
            for i in range(len(empresaLista)):
                print("")
                print("***** EMPRESA "+str(i+1)+" *****")
                print("ID: "+empresaLista[i].idEmpresa)
                print("Nombre: "+empresaLista[i].nombre)
                print("Abreviatura: "+empresaLista[i].abreviatura) 
                print("")
                
            print("_________________________________________________")
            print(" ")
            print("Digite el numero de empresa que desea trabajar: ")
            actualSeleccionEmpresa=int(input())-1
            if actualSeleccionEmpresa>len(empresaLista):
                print("Error!!! empresa no existente.")
                sleep(5)
            else:
                pass 
        os.system ("cls")        
        print(" ")
        print("***** EMPRESA "+str(actualSeleccionEmpresa+1)+" SELECCIONADA *****")
        print("ID: "+empresaLista[actualSeleccionEmpresa].idEmpresa)
        print("Nombre: "+empresaLista[actualSeleccionEmpresa].nombre)
        print("Abreviatura: "+empresaLista[actualSeleccionEmpresa].abreviatura) 
        print("Cantidad de puntos de atención: " + str(len(empresaLista[actualSeleccionEmpresa].puntosAtencion)))
        print("")
        sleep(2)
        print("***** PUNTOS DE ATENCION DE LA EMPRESA *****")
        print("_________________________________________________")
        for i in range(len(empresaLista[actualSeleccionEmpresa].puntosAtencion)): 
            print("")
            print("PUNTO DE ATENCION NO. "+str(i+1)) 
            print("ID: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[i].idPuntoAtencion)
            print("Nombre: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[i].nombre)
            print("Direccion: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[i].direccion)
            print("Cantidad de Escritorios: "+str(len(empresaLista[actualSeleccionEmpresa].puntosAtencion[i].escritorios)))        
        print("_________________________________________________")
        print("")   
        print("Digite el el punto de atencion de empresa que desea trabajar:")
        actualSeleccionPunto=int(input())-1
        os.system ("cls")
        print("")
        print("***** PUNTO DE ATENCION NO. "+str(i+1)+" SELECCIONADO *****") 
        print("ID: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].idPuntoAtencion)
        print("Nombre: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].nombre)
        print("Direccion: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].direccion)
        print("Cantidad de Escritorios: "+str(len(empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios))) 
        print("")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)        
        print("*** PROCESO TERMINADO ***")
        sleep(4)
    if op==3:
        os.system ("cls")
        print("*** Manejo de puntos de atención ***")
        print("")
        
    if op==4:
        fin=0
    if op>4 or op==0:
        print("Opcion no valida!")
        print("Vuelva a intentarlo...")
        
        

