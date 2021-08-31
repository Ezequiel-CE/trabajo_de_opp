import random

nombres= ["juan","carlos","ramiro","fernando","gabriel"]
apellidos = ["carrizo","escudero","fernandez","sosa","michelo"]


class jugador:
    def __init__(self):
        self.nombre = random.choice(nombres)
        self.apellido = random.choice(apellidos)
        self.numero = random.randint(1,30)
        self.edad = random.randint(18,35)
        self.altura = round(random.uniform(1.30,2.00),2)
        self.tarjetaAmarilla= 0
        self.tarjetaRoja= False
        
        
    





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
            
    

#print(vars(jugador1))

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
        if equipo == self.local:
            jugador=self.local.jugadores[random.randint(0,10)]
            print(f"gol de {self.local.nombre} hecho por {jugador.nombre} {jugador.apellido} en minuto {minuto}")
        else:
            jugador=self.visitante.jugadores[random.randint(0,10)]
            print(f"gol de {self.visitante.nombre} hecho por {jugador.nombre} {jugador.apellido} en minuto {minuto}")
            
        pass
    
    def tarjeta_amarilla(self,equipo):
        
        if equipo == self.local:
            jugador=self.local.jugadores[random.randint(0,10)]
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta amarilla, se suma una amarilla a {self.local.nombre} ")
            jugador.tarjetaAmarilla += 1
            
            if jugador.tarjetaAmarilla >= 2:
                self.tarjeta_roja(None,jugador)
        else:
            jugador=self.visitante.jugadores[random.randint(0,10)]
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta amarilla, se suma una amarilla a {self.visitante.nombre} ")
            jugador.tarjetaAmarilla += 1
           
            if jugador.tarjetaAmarilla >= 2:
                self.tarjeta_roja(None,jugador)
        
        
            
    def tarjeta_roja(self,equipo=None,jugador=None):
        
        if equipo == self.local:
            
            jugador=self.local.jugadores[random.randint(0,10)]
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.local.nombre} juega con uno menos ")
            jugador.tarjetaRoja = True
            
            
        elif equipo == self.visitante:
            
            jugador=self.visitante.jugadores[random.randint(0,10)]
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.visitante.nombre} juega con uno menos ")
            jugador.tarjetaRoja = True
            
        
        elif equipo == None: 
            print(f"2 amarilla para {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.local.nombre} juega con uno menos")
            jugador.tarjetaRoja = True
            








####llamando equipos






boca = equipo("Boca")
river = equipo("River")
boca.llenar_equipo()
river.llenar_equipo()






partido1 = partido(boca,river)
partido1.inicio()
partido1.gol(river,45)

partido1.tarjeta_amarilla(boca)
partido1.tarjeta_amarilla(boca)
partido1.tarjeta_amarilla(boca)

partido1.tarjeta_amarilla(boca)

partido1.tarjeta_amarilla(boca)

partido1.tarjeta_amarilla(boca)

partido1.tarjeta_amarilla(boca)

partido1.tarjeta_amarilla(boca)

partido1.tarjeta_amarilla(boca)



partido1.tarjeta_amarilla(river)

partido1.tarjeta_roja(river)


