import random

# Define parameters
POPULATION_SIZE = 100
GENE_LENGTH = 6
MUTATION_RATE = 0.01
TARGET = "HELLO"

# Generate initial population
def generate_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(GENE_LENGTH))
        population.append(individual)
    return population

# Fitness function
def fitness(individual):
    score = 0
    for i in range(len(TARGET)):
        if individual[i] == TARGET[i]:
            score += 1
    return score

# Selection
def selection(population):
    scores = [fitness(individual) for individual in population]
    total_score = sum(scores)
    probabilities = [score / total_score for score in scores]
    selected_indices = random.choices(range(len(population)), weights=probabilities, k=2)
    return [population[i] for i in selected_indices]

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENE_LENGTH - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation
def mutation(individual):
    mutated_individual = ""
    for gene in individual:
        if random.random() < MUTATION_RATE:
            mutated_individual += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            mutated_individual += gene
    return mutated_individual

# Main genetic algorithm function
def genetic_algorithm():
    population = generate_population()
    generation = 0
    while True:
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == len(TARGET):
            print("Solution found in generation:", generation)
            print("Solution:", population[0])
            break
        selected_parents = [selection(population) for _ in range(int(POPULATION_SIZE / 2))]
        children = [crossover(parent1, parent2) for parent1, parent2 in selected_parents]
        population = [mutation(child) for sublist in children for child in sublist]
        generation += 1

# Run the genetic algorithm
genetic_algorithm()