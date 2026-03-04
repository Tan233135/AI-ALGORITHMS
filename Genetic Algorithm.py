import random
import numpy as np

class GeneticMutation:
    def __init__(self, population_size, num_generations, mutation_rate):
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.population = []

    def generate_initial_population(self):
        for _ in range(self.population_size):
            individual = [random.randint(0, 1) for _ in range(10)]  # 10-bit binary string
            self.population.append(individual)

    def fitness(self, individual):
        # Simple fitness function: sum of the bits
        return sum(individual)

    def selection(self):
        fitnesses = [self.fitness(individual) for individual in self.population]
        selected_individuals = []
        for _ in range(self.population_size):
            r = random.random()
            cumulative_sum = 0
            for i, individual in enumerate(self.population):
                cumulative_sum += fitnesses[i]
                if r <= cumulative_sum / sum(fitnesses):
                    selected_individuals.append(individual)
                    break
        return selected_individuals

    def crossover(self, parents):
        child = []
        for i in range(len(parents[0])):
            if random.random() > 0.5:
                child.append(parents[0][i])
            else:
                child.append(parents[1][i])
        return child

    def mutation(self, individual):
        if random.random() < self.mutation_rate:
            for i in range(len(individual)):
                if random.random() < 0.5:
                    individual[i] = 1 - individual[i]
        return individual

    def evolve(self):
        selected_individuals = self.selection()
        new_population = []
        for _ in range(self.population_size):
            parents = random.sample(selected_individuals, 2)
            child = self.crossover(parents)
            child = self.mutation(child)
            new_population.append(child)
        self.population = new_population

    def run(self):
        self.generate_initial_population()
        for _ in range(self.num_generations):
            self.evolve()
        return self.population

# Example usage
algorithm = GeneticMutation(population_size=100, num_generations=100, mutation_rate=0.01)
population = algorithm.run()
print(population)