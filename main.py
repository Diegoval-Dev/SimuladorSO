import random
import simpy



print("Simulación en curso")
"""
def car(env):
     while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)
        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

env = simpy.Environment()
env.process(car(env))
env.run(until=50)
"""


## init = 100 
capacity = 100 #ram memory capacity (100 y 200)
time_ini = 0
rango = 10 #Intervalos (1 y 5)
inst = 3 #instrucciones del ciclo (6)
operacion = 1 #operaciones por ciclo
procesos_cant = 25  #number of processes (25,50,100,150 y 200)


def proceso(env, cantRam, cantInstrucciones, id_proceso, inst, operacion, memoria_disponible, acceso_procesador, tiempo_inicio):
        
    # Utilizando f-strings
    # El código muestra información del proceso nuevo en cola con la cantidad de RAM requerida y disponible
    global time_ini #variable global
    yield env.timeout(tiempo_inicio)
    
    print(f"Proceso {id_proceso} en cola [NEW]. Tiempo: {env.now}. Cantidad de RAM requerida: {cantRam}. Cantidad de RAM disponible: {memoria_disponible.level}") # Representa la memoria RAM disponible para ser utilizada por los procesos en la simulación
    yield memoria_disponible .get(cantRam)
    print(f"Proceso {id_proceso} en cola [READY] en tiempo {env.now}. Cantidad de instrucciones pendientes: {cantInstrucciones}")
    
    #Se ejecuta mientras la cantidad de instrucciones pendientes sea mayor a cero
    while cantInstrucciones > 0:
        #procesamiento de instrucciones en un procesador
        with acceso_procesador.request() as req:
            yield req
            cantInstrucciones  -= inst
            yield env.timeout(operacion) # tiempo en cada operación
            print(f"{id_proceso} proces en cola [READY] en tiempo {env.now}. Cantidad de instrucciones pendientes {cantInstrucciones}") # Utilizando f-strings

        #representación lógica para mover los procesos a la cola de espera si quedan instrucciones pendientes
        if cantInstrucciones  > 0 and random.randint(1, 2) == 1: 
            # si quedan instrucciones pendientes, mover a la cola de espera
            print(f"{id_proceso} ha ingresado a la cola [WAITING]") # Utilizando f-strings
            yield env.timeout(random.randint(1, 5)) #espera un tiempo aleatorio (entre 1 y 5 unidades de tiempo)
  
    
    # Encargado de llevar un registro del tiempo en que un proceso es eliminado y devuelve la cantidad de memoria que se liberó
    yield memoria_disponible .put(cantRam)
    inicial_proced = env.now 
    time_ini += env.now - inicial_proced #calculando el tiempo transcurrido desde que inició el proceso
    print(f"{id_proceso} proceso [TERMINATED] en tiempo {env.now}. Cantidad de RAM devuelta: {cantRam}. Cantidad de memoria disponible: {memoria_disponible.level}")
    
  
env = simpy.Environment() #entorno de simulación
#cantidad de memoria disponible en la simulación
memoria_disponible = simpy.Container(env, capacity, capacity) #capacidad inicial y máxima igual a capacity.
acceso_procesador = simpy.Resource(env, capacity=1 )

#Cada proceso se genera con una cantidad random de instrucciones y RAM requerida
for i in range(procesos_cant): #(25,50,100,150 y 200)
    tiempo_inicio = random.expovariate(1/10)  # valor random que representa el tiempo de inicio de un proceso
    cantInstrucciones = random.randint(1, 10)  # genera una cantidad random de instrucciones 
   


