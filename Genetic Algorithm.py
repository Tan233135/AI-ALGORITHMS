import random

# Parameters
target = "1010101010"
pop_size = 10
mut_rate = 0.1
gens = 50

# Fitness function: number of matching bits
def fitness(ind):
    return sum(a==b for a,b in zip(ind,target))

# Random individual
def rand_ind():
    return ''.join(random.choice('01') for _ in target)

# Crossover
def crossover(p1,p2):
    i = random.randint(1,len(p1)-1)
    return p1[:i]+p2[i:]

# Mutation
def mutate(ind):
    return ''.join(b if random.random()>mut_rate else random.choice('01') for b in ind)

# Initial population
pop = [rand_ind() for _ in range(pop_size)]

for g in range(gens):
    pop = sorted(pop,key=fitness,reverse=True)
    if fitness(pop[0])==len(target):
        break
    pop = [mutate(crossover(random.choice(pop[:5]),random.choice(pop[:5]))) for _ in range(pop_size)]

print("Best:",pop[0],"Fitness:",fitness(pop[0]))