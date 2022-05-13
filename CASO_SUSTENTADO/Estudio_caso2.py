com= str(input("Bienvenidos: Este es un programa para venta de boletas!.\nDesea realizar la compra?:"))
numeroDoc=[]
nBDo=[]
boleta=10
acu_b=0

#Validación de aceptación de proceso de compra
if com=="si" or com=="Si" or com=="SI" or com=="sI":        
    for i in range(0,5):
        TipoDoc= str(input("Cual es su tipo de documento: "))   
        nDoc=int(input("Cual es su número de cédula: "))
        #Condiciono el Tipo de documento y número de documento    
        if TipoDoc== "cc" or TipoDoc== "CC" and nDoc>0:            
            numeroDoc.append(nDoc)
            # Validación número de documento utilizando la función count()
            if numeroDoc.count(nDoc) >1:                
                print("Usuario ya adquirió boletas")
                continue            
            #Continuamos con la solicitud de la cantidad de la compra de boletas    
            nBol=int(input("Cuantas boletas va a comprar:? "))  
                # Validación y guardado de cantidad boletas
                # Definimos el parámetro que va a tomar nBol (que contiene el nro de boletas que compra el cliente que deben ser <= a 4)
            if nBol >0 and nBol<=4:        
                # Creamos una variable acu_b la cual, va a adicionar el número de boletas compradas cada vez que ingrese un cliente
                acu_b= acu_b+nBol          
                if acu_b<= boleta :
                    tb=boleta-acu_b
                    nBDo.append(nBol)
                    print(f"\n¡Venta exitosa!\n")
                    print(f"Quedan {tb} boletas disponibles\n")
                # Validamos la cantidad de boletas solicitadas por el cliente con respecto a las boletas vendidas para informar disponibilidad
                elif acu_b>boleta :                               
                    acu_b=acu_b-nBol
                    nm=boleta-acu_b
                    print(f"""Lo sentimos, en el momento NO contamos con la cantidad de boletas requeridas,
                        contamos sólo con {nm} boletas disponibles""")                        
                if tb == 0 : 
                    print(f"\n ¡Boletería agotada!\n")
                    break
            else:
                print(f"""Lo sentimos, la cantidad de boletas solicitadas por usuario son {nBol},
                    Recuerde que la cantidad máxima autorizada para su compra es de 4 boletas""")
        else:              
            print("Debe ingresar un tipo de documento válido\n")
            
        
        
