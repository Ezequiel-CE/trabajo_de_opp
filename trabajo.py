import random

listaNombres= ["juan","carlos","ramiro","fernando","gabriel"]
listaApellidos = ["carrizo","escudero","fernandez","sosa","michelo"]

## clase jugador


class jugador:
    def __init__(self):
        self.nombre = random.choice(listaNombres)
        self.apellido = random.choice(listaApellidos)
        self.numero = random.randint(1,30)
        self.edad = random.randint(18,35)
        self.altura = round(random.uniform(1.30,2.00),2)
        self.tarjetaAmarilla= 0






###################### clase equipo





#print(jugadores)

class equipo:
    
    
    
    def __init__(self,nombre):
        
        self.nombre = (nombre)
        self.jugadores=[]
        
        
    
    def llenar_equipo(self):
        for _ in range(11):
            self.jugadores.append(jugador())
    
    def ver_jugadores(self):
        for j in self.jugadores:
            print(vars(j))




###################### clase partido


class partido:
    
    def __init__(self,local,visitante) :
        self.duracion = 90
        self.local = local
        self.visitante = visitante
        pass
    
    def inicio(self):
        print("comienza el partido")
    
    def final(self):
        print("finaliza el partido")
        
    def gol(self,equipo,minuto):
        
        #compara que equipo es
        if equipo == self.local:
            jugador=random.choice(self.local.jugadores)  #escoge el jugador
            print(f"gol de {self.local.nombre} hecho por {jugador.nombre} {jugador.apellido} en minuto {minuto}")
            
        else:
            jugador=random.choice(self.visitante.jugadores)
            print(f"gol de {self.visitante.nombre} hecho por {jugador.nombre} {jugador.apellido} en minuto {minuto}")
            
        pass


    def tarjeta_amarilla(self,equipo):
        
        #compara equipo
        
        if equipo == self.local:
            jugador=random.choice(self.local.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta amarilla, se suma una amarilla a {self.local.nombre} ")
            jugador.tarjetaAmarilla += 1
            
            #si tiene mas de 2 tarjetas es roja
            
            if jugador.tarjetaAmarilla >= 2:
                self.tarjeta_roja(self.local,jugador)
        else:
            jugador=random.choice(self.visitante.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta amarilla, se suma una amarilla a {self.visitante.nombre} ")
            jugador.tarjetaAmarilla += 1
           
            if jugador.tarjetaAmarilla >= 2:
                self.tarjeta_roja(self.visitante,jugador)



    def tarjeta_roja(self,equipo=None,jugadorArgumen=None):
        
        #corregir el tema de cuando un jugador tiene mas de 2 amarillas
        
        if jugadorArgumen != None :
            print(f"2 amarillas de {jugadorArgumen.nombre} {jugadorArgumen.apellido} , el arbitro le saca la tarjeta roja, {equipo.nombre} juega con uno menos ")
            equipo.jugadores.remove(jugadorArgumen)
        
        
        if equipo == self.local and jugadorArgumen== None:
            
            jugador=random.choice(self.local.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.local.nombre} juega con uno menos ")
            self.local.jugadores.remove(jugador)
            
            
            
        elif equipo == self.visitante and jugadorArgumen== None:
            
            jugador=random.choice(self.visitante.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.visitante.nombre} juega con uno menos ")
            self.visitante.jugadores.remove(jugador)
    
    def posecion(self):
        posesion_equipo = random.randint(0,100)
        print("Posecion de {} {} % , posecion de {} {} %".format(self.local.nombre , posesion_equipo ,self.visitante.nombre,100-posesion_equipo ))

    









####llamando equipos






boca = equipo("Boca")
river = equipo("River")




boca.llenar_equipo()
river.llenar_equipo()
river.ver_jugadores()






partido1 = partido(boca,river)
partido1.inicio()
partido1.gol(boca,50)

partido1.posecion()



