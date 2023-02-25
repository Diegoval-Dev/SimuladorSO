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
    yield env.timeout(tiempo_inicio)
    
    # Utilizando f-strings
    print(f"Proceso {id_proceso} en cola [NEW]. Tiempo: {env.now}. Cantidad de RAM requerida: {cantRam}. Cantidad de RAM disponible: {memoria_disponible.level}") # Representa la memoria RAM disponible para ser utilizada por los procesos en la simulación
    yield memoria_disponible .get(cantRam)
    print(f"Proceso {id_proceso} en cola [READY] en tiempo {env.now}. Cantidad de instrucciones pendientes: {cantInstrucciones}")
    
    
    # Encargado de llevar un registro del tiempo en que un proceso es eliminado y devuelve la cantidad de memoria que se liberó
    inicial_proced = env.now 
    yield memoria_disponible .put(cantRam)
    global tiempo_total
    tiempo_total += env.now - inicial_proced
    print(f"{id_proceso} proceso [TERMINATED] en tiempo {env.now}. Cantidad de RAM devuelta: {cantRam}. Cantidad de memoria disponible: {memoria_disponible.level}")
    
    
    
    
    
    
    




    
    
    
"""   
env = simpy.Environment()
RAM = simpy.Container(env, init=100, capacity=100)
"""   