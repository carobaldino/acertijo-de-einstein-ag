import array
import random
from individuo import generarIndividuo, evaluarIndividuo, cruzar, mutarIndividuo
import numpy
from deap import base, creator, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)


toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, generarIndividuo) # Structure initializers
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluarIndividuo) #le entra por parámetro un individuo
toolbox.register("mate", tools.cxTwoPoints)
toolbox.register("mutate", mutarIndividuo, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


if __name__ == "__main__":
    pop = toolbox.population(n=3125)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    poblacionEvolucionada, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=50, stats=stats, halloffame=hof, verbose=True)

    best_individual = tools.selBest(poblacionEvolucionada,1)[0]
    

    print("======log========")
    print(log)
    print("======Población========")
    print(random.sample(pop,10))
    print("======Población Evolucionada========")
    print(random.sample(poblacionEvolucionada,10))
    print("======Mejor Individuo========")
    print(best_individual)
    print("======Evaluación========")
    print(evaluarIndividuo(best_individual))

