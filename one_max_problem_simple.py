import array
import random
import numpy
from deap import base, creator, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def evalOneMax(individual):
    return sum(individual),

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1) # Attribute generator 
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100) # Structure initializers
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


if __name__ == "__main__":
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, stats=stats, halloffame=hof, verbose=True)

    best_individual = tools.selBest(pop,1)[0]
    
    print("======population========")
    print(pop)
    print("======log========")
    print(log)
    print("======Mejor Individuo========")
    print(best_individual)
    print("======Evaluación========")
    print(evalOneMax(best_individual))






