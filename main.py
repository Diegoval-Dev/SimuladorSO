import simpy
import random



print("Hello, world")
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

def proceso(env, cantRam, cantInstrucciones):
    global tiempo




env = simpy.Environment()
RAM = simpy.Container(env, init=100, capacity=100)