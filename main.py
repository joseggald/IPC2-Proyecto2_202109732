
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from time import sleep

import jinja2
from ListaSimple import Lista_simple
from claseCI import ConfigInicial
from claseClientes import Clientes
from claseEmpresa import Empresa
from claseEscritorios import Escritorio
from clasePuntoAtencion import PuntoAtencion
from claseTransaccion import Transaccion
from escritoriosAtendiendo import EscritorioAt


simulador=0
opConfig=0
fin=100
empresaData=Lista_simple()
empresaLista=[]
configData=Lista_simple()
configLista=[]
atencionCliente=[]
actualSeleccionEmpresa=1000
actualSeleccionPunto=1000
colaCliente=[]
tiempoColaTotal=0
tiempoColaProm=0   
contAt=0
ca=0
escritorioAt=[]
clinteAt=[]
cola=[]
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
                actualSeleccionEmpresa=1000
                actualSeleccionPunto=1000
                simulador=0
                tiempoColaTotal=0
                tiempoColaProm=0   
                contAt=0
                ca=0
                clinteAt.clear()
                cola.clear()
                escritorioAt.clear()
                atencionCliente.clear()
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
                print("")
                print("Escriba el nombre del archivo que se encuentra en la carpeta: ")
                carga=input()
                parser = ET.XMLParser(encoding="utf-8")
                tree = ET.parse(carga,parser=parser)
                root = tree.getroot()
                for empresa in root:
                    idEmpresa = empresa.attrib['id']
                    
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
                                escritoriosData=Lista_simple()
                                escritoriosLista=[]  
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
                                puntosAtData.agregar_al_final(PuntoAtencion(idPA, nombrePA,direccionPA,escritoriosData,clientesData))   
                                puntosAtLista.append(PuntoAtencion(idPA, nombrePA,direccionPA,escritoriosLista, clientesLista))                                                                       
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
                    empresaData.agregar_al_final(Empresa(idEmpresa,NombreEmpresa,AbreviaturaEmpresa,puntosAtData,transaccionData))
                    empresaLista.append(Empresa(idEmpresa,NombreEmpresa,AbreviaturaEmpresa,puntosAtLista,transaccionLista))
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
                print("Escriba el nombre del archivo que se encuentra en la carpeta: ")
                carga=input()
                parser = ET.XMLParser(encoding="utf-8")
                tree = ET.parse(carga,parser=parser)
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
                                        empresaLista[i].puntosAtencion[j].clientes=clientesLista
                                    else:
                                        pass 
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
        actualSeleccionEmpresa=1000
        actualSeleccionPunto=1000
        while(actualSeleccionEmpresa>len(empresaLista)):
            tiempoColaTotal=0
            tiempoColaProm=0 
            ca=0
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
            print("Cantidad de Clientes: "+ str(len(empresaLista[actualSeleccionEmpresa].puntosAtencion[i].clientes)))      
        print("_________________________________________________")
        print("")   
        print("Digite el el punto de atencion de empresa que desea trabajar:")
        actualSeleccionPunto=int(input())-1
        os.system ("cls")
        print("")
        print("***** PUNTO DE ATENCION NO. "+str(actualSeleccionPunto+1)+" SELECCIONADO *****") 
        print("ID: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].idPuntoAtencion)
        print("Nombre: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].nombre)
        print("Direccion: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].direccion)
        print("Cantidad de Escritorios: "+str(len(empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios))) 
        print("Cantidad de Clientes: "+ str(len(empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].clientes)))
        print("")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)   
        print("...")     
        sleep(1) 
        print("")
        print("*** PROCESO TERMINADO ***")
        colaCliente=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].clientes
        parteTiempos=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].clientes
        contCola=0
        for a in range(len(parteTiempos)):
            for b in range(len(parteTiempos[a].transacciones)):
                tiempoColaTotal=int(parteTiempos[a].transacciones[b].tiempo)+tiempoColaTotal
                contCola=1+contCola
        tiempoColaProm=tiempoColaTotal/contCola 
        if contAt==0:
                    
                    escritorio=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios
                    clienteLen=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].clientes
                    for i in range(len(escritorio)):
                        if escritorio[i].estado==True:
                            ides=escritorio[i].idEsc
                            encar=escritorio[i].encargado
                            escritorioAt.append(EscritorioAt(ides,"vacio","vacio"))   
                    
                    for j in range(len(clienteLen)):
                        nomCl=clienteLen[j].nombre
                        cola.append(nomCl)
        
    if op==3:
        if actualSeleccionEmpresa==1000 and actualSeleccionPunto==1000:
            print("*** ERROR ***")
            print("NO SE HA SELECCIONADO NINGUNA EMPRESA")
            sleep(5)
        else:
            opManejo=0
            stop=False
            while(stop!=True):
                os.system ("cls")
                print("*** Manejo de puntos de atención ***")
                print("")
                print(" 1. Ver estado del punto de atención ")
                print(" 2. Activar escritorio de servicio ")
                print(" 3. Desactivar escritorio ")
                print(" 4. Atender cliente ")
                print(" 5. Solicitud de atención ")
                print(" 6. Simular actividad del punto de atención ")
                print(" 7. Regresar Menu Principal")
                opManejo=int(input())
                if opManejo>7 or opManejo<=0:
                    print("Opcion no valida!")
                    print("Vuelva a intentarlo...")
                else:
                    stop=True
            if opManejo==1:
                os.system ("cls")
                print("****** Ver estado del punto de atención ******")
                print("__________________________________________________________")
                print(" ")
                print("********************************************************")
                print(" ")
                print(" EMPRESA "+str(actualSeleccionEmpresa+1)+" ")
                print("ID: "+empresaLista[actualSeleccionEmpresa].idEmpresa)
                print("Nombre: "+empresaLista[actualSeleccionEmpresa].nombre)
                print(" ")
                print(" PUNTO DE ATENCION NO. "+str(actualSeleccionPunto+1)+" ") 
                print("ID: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].idPuntoAtencion)
                print("Nombre: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].nombre)
                print("Cantidad en la cola de Clientes: "+ str(len(colaCliente)))
                print("Tiempo total de espera: "+str(tiempoColaTotal))
                print("Tiempo promedio por persona de espera: "+str(tiempoColaProm))
                print(" ")
                print("********************************************************")
                print("__________________________________________________________")
                print(" ")
                print("***** ESCRITORIOS ACTIVOS *****")
                escritorio=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios
                for i in range(len(empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios)):
                    if escritorio[i].estado==True:
                        print(" ")
                        print("Id:"+escritorio[i].idEsc)
                        print("Identificacion:"+escritorio[i].identificacion)
                        print("Encargado:"+escritorio[i].encargado)
                        print(" ")
                print("__________________________________________________________")
                print("__________________________________________________________")
                print(" ")
                print("***** ESCRITORIOS INACTIVOS *****")
                escritorio=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios
                for i in range(len(empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios)):
                    if escritorio[i].estado==False:
                        print(" ")
                        print("Id:"+escritorio[i].idEsc)
                        print("Identificacion:"+escritorio[i].identificacion)
                        print("Encargado:"+escritorio[i].encargado)
                        print(" ")
                print("__________________________________________________________")
                sleep(20)
                
            if opManejo==2:
                inactivos=[]
                stop=False
                os.system ("cls")
                print("****** Activar escritorio de servicio ******")
                print("__________________________________________________________")
                print(" ")
                print("***** ESCRITORIOS INACTIVOS *****")
                escritorio=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios
                for i in range(len(escritorio)):
                    if escritorio[i].estado==False:
                        print(" ")
                        print("Id:"+escritorio[i].idEsc)
                        print("Identificacion:"+escritorio[i].identificacion)
                        print("Encargado:"+escritorio[i].encargado)
                        inactivos.append(i)
                        print(" ")
                print("__________________________________________________________")
                print(" ")
                while(stop!=True):
                    print("Seleccione el numero de escritorio que desea activar: ")
                    actiEscri=int(input())-1
                    
                    for i in range(len(inactivos)):
                        if inactivos[i]==actiEscri:
                            print("Se ha activado el escritorio No. "+ str(actiEscri+1))
                            print("Id:"+escritorio[actiEscri].idEsc)
                            print("Identificacion:"+escritorio[actiEscri].identificacion)
                            print("Encargado:"+escritorio[actiEscri].encargado)
                            escritorio[actiEscri].estado=True
                            escritorioAt.append(EscritorioAt(escritorio[actiEscri].idEsc,"vacio","vacio"))
                            stop=True
                            break
                        else:
                            pass
                    if stop==False:
                        print(" ")
                        print("ERROR, el escritorio que selecciono no se encuentra en activos o existe, recuerde que si esta en servicio no es posible desactivar.")
                        print(" ")
                sleep(10)
            if opManejo==3:
                activos=[]
                stop=False
                os.system ("cls")
                print("****** Desactivar escritorio ******") 
                print("__________________________________________________________")
                print(" ")
                print("***** ESCRITORIOS ACTIVOS *****")
                escritorio=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios
                for i in range(len(escritorio)):
                        if escritorio[i].estado==True:
                            print(" ")
                            print("Id: "+escritorio[i].idEsc)
                            print("Identificacion: "+escritorio[i].identificacion)
                            print("Encargado:"+escritorio[i].encargado)
                            activos.append(i)
                            print(" ")
                print("__________________________________________________________")
                print(" ")
                while(stop!=True):
                    print("Seleccione el numero de escritorio que desea desactivar: ")
                    actiEscri=int(input())-1
                    
                    for i in range(len(activos)):
                        for j in range(len(escritorioAt)):
                            if activos[i]==actiEscri:
                                if escritorioAt[j].idEsc==escritorio[actiEscri].idEsc:
                                    if escritorioAt[j].nomCliente=="vacio":  
                                        print("Se ha desactivado el escritorio No. "+ str(actiEscri+1))
                                        print("Id: "+escritorio[actiEscri].idEsc)
                                        print("Identificacion: "+escritorio[actiEscri].identificacion)
                                        print("Encargado:"+escritorio[actiEscri].encargado)
                                        escritorio[actiEscri].estado=False
                                        escritorioAt.pop(j)
                                        stop=True
                                        break
                            else:
                                pass
                    if stop==False:
                        print("ERROR, el escritorio que selecciono no se encuentra en inactivos o existe.")
                sleep(10)
            
            if opManejo==4:
                if contAt==1:
                    os.system ("cls")
                    print("****** Atender Cliente ******") 
                    escritorio=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios
                    clienteLen=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].clientes
                    for i in range(len(escritorioAt)):
                        if escritorioAt[i].nomCliente=="vacio":
                            escritorioAt[i].nomCliente=cola[0]
                            cola.pop(0)
                    ca=0
                if contAt>1:  
                    os.system ("cls")
                    print("****** Atender Cliente ******") 
                    escritorio=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].escritorios
                    clienteLen=empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].clientes 
                    
                    if ca == len(escritorioAt):
                        ca=0
                    for i in range(len(escritorioAt)):
                        if escritorioAt[i].nomCliente=="vacio" and len(cola)>0:
                            escritorioAt[i].nomCliente=cola[0]
                            cola.pop(0)
                    if escritorioAt[ca].nomCliente!="vacio":
                        escritorioAt[ca].nomCliente="vacio"
                    if ca < len(escritorioAt): 
                        ca=ca+1
                contAt=contAt+1    
                print(" ")
                print(" ")
                print("-|-|-|-|-| ESCRITORIOS ATENDIENDO |-|-|-|-|-")
                for b in range(len(escritorioAt)):
                    print(" ")
                    print(escritorioAt[b].idEsc)
                    print("Nombre Cliente: "+escritorioAt[b].nomCliente)
                print(" ")
                print(" ")
                print("-|-|-|-|-| COLA |-|-|-|-|-")
                for d in range(len(cola)):
                    print(cola[d])
                sleep(15)
                if len(cola)<1:
                    print(" ")
                    print("-|-|-|-|-| COLA TERMINADA |-|-|-|-|-")
           

            if opManejo==5:
                uno=0
                trans=[]
                cant=[]
                stop=False
                os.system ("cls")
                print("****** Solicitud de atención ******") 
                print("__________________________________________________________")
                print(" ")
                print("********************************************************")
                print(" ")
                print(" EMPRESA "+str(actualSeleccionEmpresa+1)+" ")
                print("ID: "+empresaLista[actualSeleccionEmpresa].idEmpresa)
                print("Nombre: "+empresaLista[actualSeleccionEmpresa].nombre)
                print(" ")
                print(" PUNTO DE ATENCION NO. "+str(actualSeleccionPunto+1)+" ") 
                print("ID: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].idPuntoAtencion)
                print("Nombre: "+empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].nombre)
                print("Cantidad en la cola de Clientes: "+ str(len(colaCliente)))
                print(" ")
                print("********************************************************")
                print("__________________________________________________________")
                print(" ") 
                print("-|-|-|-|-| Formulario de Datos de Nuevo Cliente |-|-|-|-|-") 
                print("DPI: ") 
                dpiCli=input()
                print("Nombre: ") 
                nomCli=input()
                
                while stop!=True:
                    os.system ("cls")
                    print("-|-|-|-|-| Seleccion de Transacciones |-|-|-|-|-") 
                    print("__________________________________________________________")
                    print("**** TRANSACCIONES DISPONIBLES ****") 
                    print(" ")
                    for i in range (len(empresaLista[actualSeleccionEmpresa].transacciones)):
                        print(" Transaccion No. "+str(i+1))
                        print("Id: "+empresaLista[actualSeleccionEmpresa].transacciones[i].idTrans)
                        print("Nombre: "+empresaLista[actualSeleccionEmpresa].transacciones[i].nombre)
                        print("Tiempo estipulado: "+ str(empresaLista[actualSeleccionEmpresa].transacciones[i].tiempo))
                        print(" ")
                    print(" ")
                    print("Digite el numero de transacción que hara:")
                    opTrans=int(input())-1
                    if opTrans>len(empresaLista[actualSeleccionEmpresa].transacciones):
                        print("Transaccion no existente!")
                        print("Vuelva a intentarlo...")
                    else:
                        tr=empresaLista[actualSeleccionEmpresa].transacciones[opTrans]
                        print("Digite la cantidad de dinero que utilizara:")
                        cantTxt=int(input())
                        trans.append(Transaccion(tr.idTrans,tr.nombre,tr.tiempo))
                        cant.append(cantTxt)
                        print(" ")
                        print("Desea hacer otra transaccion? Si=1 o No=0")
                        opf=int(input())
                        if opf==1:
                            pass
                        if opf==0: 
                            stop=True 
                    
                empresaLista[actualSeleccionEmpresa].puntosAtencion[actualSeleccionPunto].clientes.append(Clientes(dpiCli,nomCli,trans,cant))
      
                os.system ("cls")

                
                print("Cliente en cola!")
                sleep(6)
                    


            if opManejo==6:
                os.system ("cls")
                print("**** IMPRESION COMPLETA ****")
                sleep(4)
                simulador=1+simulador
                os.system ("cls")
                print("****** Simular actividad del punto de atención ******")
                archi1=open("GraficaNo"+str(simulador)+".dot","w") 
                archi1.write("digraph L{\n")  
                archi1.write('  node[shape=box fillcolor="#4D92C5" style=filled] \n')  
                archi1.write('  subgraph cluster_p{ \n')
                archi1.write('      label="ATENCION AL CLIENTE"\n')
                for b in range(len(escritorioAt)):
                    archi1.write('      Escritorio'+str(b)+'[label= "Escritorio: '+str(escritorioAt[b].idEsc)+'" fillcolor="#4D92C5"]\n')
                    archi1.write('      edge[dir="both"]\n')
                    archi1.write('      cliente'+str(b)+'[label= "Nombre: '+str(escritorioAt[b].nomCliente)+' ", group=1]\n')
                    archi1.write('      Escritorio'+str(b)+'->cliente'+str(b)+'\n')
                archi1.write('      Cola[label= "Cola Actual"]\n')
                archi1.write('      edge[dir="both"]\n')
                for d in range(len(cola)):
                    if d==0:
                        archi1.write('      clienteCola'+str(d)+'[label= "Nombre: ", group=1\n')
                        archi1.write('      Cola->clienteCola'+str(d)+'\n')
                    else:
                        archi1.write('      clienteCola'+str(d)+'[label= "Nombre: ", group=1\n')
                        archi1.write('      clienteCola'+str(d-1)+'->clienteCola'+str(d)+'\n')
                archi1.write('  }\n')
                archi1.write('}\n')
                archi1.close()
                os.system('dot -Tpng GraficaNo'+str(simulador)+'.dot -o GraficaNo'+str(simulador)+'.png')
                os.system('cd ./GraficaNo'+str(simulador)+'.png')
                os.startfile('GraficaNo'+str(simulador)+'.png')
            if opManejo==7:
                pass

    if op==4:
        fin=0
    if op>4 or op==0:
        print("Opcion no valida!")
        print("Vuelva a intentarlo...")
        
        

