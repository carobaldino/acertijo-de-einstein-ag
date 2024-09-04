import random
import numpy
from deap import base, creator, algorithms, tools
from utils import inicializar_cromosoma, imprimir_cromosoma
from fitness import fitness_deap

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
#toolbox.register("attr_int", random.randint, a = 0, b = 4) ##esta vez los genes no son binarios son enteros, del 0 al 4
#toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_int, n=30) #pporque el cromosoma tiene largo 30
toolbox.register("individual", tools.initIterate, creator.Individual, inicializar_cromosoma)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", fitness_deap) #le entra por parámetro un individuo
toolbox.register("select", tools.selTournament, tournsize=5)
#toolbox.register("select", tools.selRoulette)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.30)


if __name__ == "__main__":
    population = toolbox.population(n=5) # tiene que ser 5, son 5 personas
    crossover_probability = 0.8
    mutation_probability = 0.3
    generations = 5000
    hall_of_fame = tools.HallOfFame(1)
    
    statistics = tools.Statistics(key = lambda individual: individual.fitness.values)
    statistics.register('max', numpy.max)
    statistics.register('min', numpy.min)
    statistics.register('med', numpy.mean) ##media
    statistics.register('std', numpy.std) ##desviacion estandard

    population, log_book = algorithms.eaSimple(population, toolbox, cxpb=crossover_probability, mutpb=mutation_probability, ngen=generations, stats=statistics, halloffame=hall_of_fame, verbose=True)

    best_solution = hall_of_fame[0]
    print(best_solution)
    print(best_solution.fitness)
    imprimir_cromosoma(best_solution)
    
