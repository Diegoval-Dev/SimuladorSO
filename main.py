import random
import simpy
import numpy

# Referencias de https://simpy.readthedocs.io/en/latest/api_reference/simpy.resources.html


print(" ")
print(" ")
print("--------------------Simulación en curso--------------------")
print(" ")
print(" ")

arr = []
#init = 100 
capacity = 200 #ram memory capacity (100 y 200)
time_ini = 0
rango = 10 #Intervalos (1, 5, 10)
inst = 3 #instrucciones del ciclo (3, 6)
operacion = 1 #operaciones por ciclo
procesos_cant = 50  #number of processes (25,50,100,150 y 200)
cant_procesadores = 1



def proceso(env, cantRam, cantInstrucciones, id_proceso, inst, operacion, memoria_disponible, acceso_procesador, tiempo_inicio):
     
    
    # El código muestra información del proceso nuevo en cola con la cantidad de RAM requerida y disponible
    global time_ini #variable global
    
    
    yield env.timeout(tiempo_inicio)
    tiempo_inicio_Individual = env.now
    # Utilizando f-strings
    print(f" {id_proceso}, en cola [NEW]. Tiempo: {env.now:.1f}. Cantidad de RAM requerida: {cantRam}. Cantidad de RAM disponible: {memoria_disponible.level}") # Representa la memoria RAM disponible para ser utilizada por los procesos en la simulación
    yield memoria_disponible.get(cantRam)
    print(f" {id_proceso}, en cola [READY] en tiempo {env.now:.1f}. Cantidad de instrucciones pendientes: {cantInstrucciones}")

    
    #Se ejecuta mientras la cantidad de instrucciones pendientes sea mayor a cero
    while cantInstrucciones > 0:
        #procesamiento de instrucciones en un procesador
        with acceso_procesador.request() as solicitud:
            yield solicitud
            cantInstrucciones  -= inst
            yield env.timeout(operacion) # tiempo en cada operación
            print(f" {id_proceso}, proceso en cola [READY] en tiempo {env.now:.1f}. Cantidad de instrucciones pendientes {cantInstrucciones}") # Utilizando f-strings

        #representación lógica para mover los procesos a la cola de espera si quedan instrucciones pendientes
        if cantInstrucciones  > 0 and random.randint(1, 2) == 1: 
            # si quedan instrucciones pendientes, mover a la cola de espera
            print(f" {id_proceso}, ha ingresado a la cola [WAITING]") # Utilizando f-strings
            yield env.timeout(random.randint(1, 5)) #espera un tiempo aleatorio (entre 1 y 5 unidades de tiempo)
  
    
    # Encargado de llevar un registro del tiempo en que un proceso es eliminado y devuelve la cantidad de memoria que se liberó
    yield memoria_disponible.put(cantRam)
    arr.append(tiempo_inicio_Individual)
    print(f" {id_proceso}, proceso [TERMINATED] en tiempo {env.now:.1f}. Cantidad de RAM devuelta: {cantRam}. Cantidad de memoria disponible: {memoria_disponible.level}")
    
# nuevo objeto de la clase Environment  
env = simpy.Environment() #entorno de simulación
#cantidad de memoria disponible en la simulación
memoria_disponible = simpy.Container(env, capacity, capacity)
acceso_procesador = simpy.Resource(env, cant_procesadores )


#Cada proceso se genera con una cantidad random de instrucciones y RAM requerida
for c in range(procesos_cant): #(25,50,100,150 y 200)
    
    #representa el tiempo de llegada del siguiente proceso a la simulación.
    #https://www.geeksforgeeks.org/random-expovariate-function-in-python/
    tiempo_inicio = random.expovariate(1.0/rango)  # valor random que representa el tiempo de inicio random de un proceso
    cantInstrucciones = random.randint(1, 10)  # genera una cantidad random de instrucciones 
    cantRam = random.randint(1, 10)  # genera una cantidad random de RAM 
    env.process(proceso(env=env, tiempo_inicio=tiempo_inicio, id_proceso=f"Proceso {c}", cantRam=cantRam, cantInstrucciones=cantInstrucciones, inst=inst, operacion=operacion , memoria_disponible=memoria_disponible, acceso_procesador=acceso_procesador)) #crea un nuevo proceso en la simulación y se agrega a env


# Ejecutar la simulación
#Calcula y muestra el tiempo promedio
env.run()
promed = numpy.mean(arr)
desviacion = numpy.std(arr)
print(f"El tiempo promedio de finalización de los procesos es de {promed} segundos con una desviacion estandar de {desviacion}")