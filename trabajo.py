import random

listaNombres= ["juan","carlos","ramiro","fernando","gabriel","jose","matias","gustavo","ezequeiel","cristian",]
listaApellidos = ["carrizo","escudero","fernandez","sosa","michelo","campos","martinez","carpio","villafañes","mazzareli"]

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
        self.goles = 0
        
        
    
    def llenar_equipo(self):
        for _ in range(11):
            self.jugadores.append(jugador())
    
    def ver_jugadores(self):
        for j in self.jugadores:
            #print(vars(j))
            print(f" {j.nombre} {j.apellido} {j.numero} para {self.nombre}")




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
        
    def entretiempo(self):
        print("Finaliza primer tiempo")
        print("----------------------")
        print("----------------------")
        print("----------------------")
        print("Empieza segundo tiempo")
        
    def gol(self,equipo,minuto):
        
        #compara que equipo es
        if equipo == self.local:
            jugador=random.choice(self.local.jugadores)  #escoge el jugador
            print(f"gol de {self.local.nombre} hecho por {jugador.nombre} {jugador.apellido} en minuto {minuto}")
            self.local.goles += 1
            
        else:
            jugador=random.choice(self.visitante.jugadores)
            print(f"gol de {self.visitante.nombre} hecho por {jugador.nombre} {jugador.apellido} en minuto {minuto}")
            self.visitante.goles += 1
        pass


    def tarjeta_amarilla(self,equipo):
        
        #compara equipo
        
        if equipo == self.local:
            jugador=random.choice(self.local.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta amarilla, se suma una amarilla a {self.local.nombre} ")
            jugador.tarjetaAmarilla += 1
            
            #si tiene mas de 2 tarjetas es roja y lo saca del equipo
            
            if jugador.tarjetaAmarilla >= 2:
                self.local.jugadores.remove(jugador)
                print(f"2 amarillas de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.local.nombre} juega con uno menos ")
        else:
            #jugador visitante
            
            jugador=random.choice(self.visitante.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta amarilla, se suma una amarilla a {self.visitante.nombre} ")
            jugador.tarjetaAmarilla += 1
            
            #si tiene mas de 2 tarjetas es roja y lo saca del equipo
            
            if jugador.tarjetaAmarilla >= 2:
                self.visitante.jugadores.remove(jugador)
                self.local.jugadores.remove(jugador)
                print(f"2 amarillas de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.visitante.nombre} juega con uno menos ")

    


    def roja_directa(self,equipo):
        
        if equipo == self.local:
            
            jugador=random.choice(self.local.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.local.nombre} juega con uno menos ")
            self.local.jugadores.remove(jugador)
            
            
            
        elif equipo == self.visitante:
            
            jugador=random.choice(self.visitante.jugadores)
            print(f"falta de {jugador.nombre} {jugador.apellido} , el arbitro le saca la tarjeta roja, {self.visitante.nombre} juega con uno menos ")
            self.visitante.jugadores.remove(jugador)
    
    def posecion(self):
        posesion_equipo = random.randint(30,80)
        print("Posecion de {} {} % , posecion de {} {} %".format(self.local.nombre , posesion_equipo ,self.visitante.nombre,100-posesion_equipo ))

    def resultado(self):
        print("###################")
        print(f"Final del partido, El resultado es  {self.local.nombre} : {self.local.goles} || {self.visitante.nombre} : {self.visitante.goles}")
        









####llamando equipos






boca = equipo("Boca")
river = equipo("River")


#completa los equipos

boca.llenar_equipo()
river.llenar_equipo()
river.ver_jugadores()
print("##############################")
boca.ver_jugadores()


print("##############################")


#Instanciamos partido

partido1 = partido(boca,river)


partido1.inicio()
partido1.gol(boca,20)
partido1.tarjeta_amarilla(boca)
partido1.gol(river,30)
partido1.roja_directa(river)
partido1.entretiempo()
partido1.gol(boca,60)
partido1.gol(boca,85)
partido1.final()
partido1.posecion()
partido1.resultado()



