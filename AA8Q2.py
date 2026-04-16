import random

# ----------------- Distance Matrix -----------------
cities = ['A','B','C','D','E','F','G','H']
dist = [
 [0,10,15,20,25,30,35,40],
 [12,0,35,15,20,25,30,45],
 [25,30,0,10,40,20,15,35],
 [18,25,12,0,15,30,20,10],
 [22,18,28,20,0,15,25,30],
 [35,22,18,28,12,0,40,20],
 [30,35,22,18,28,32,0,15],
 [40,28,35,22,18,25,12,0]
]

# ----------------- Cost Function -----------------
def cost(path):
    c = 0
    for i in range(len(path)-1):
        c += dist[path[i]][path[i+1]]
    c += dist[path[-1]][path[0]]
    return c

# ----------------- Crossover -----------------
def crossover(p1, p2, two_point=False):
    n = len(p1)
    child = [-1]*n

    if two_point:
        a,b = sorted(random.sample(range(n),2))
    else:
        a,b = 0, random.randint(1,n-1)

    child[a:b] = p1[a:b]

    k = 0
    for i in range(n):
        if child[i] == -1:
            while p2[k] in child:
                k += 1
            child[i] = p2[k]
    return child

# ----------------- Mutation -----------------
def mutate(path):
    i,j = random.sample(range(len(path)),2)
    path[i],path[j] = path[j],path[i]

# ----------------- Genetic Algorithm -----------------
def genetic(crossover_type):
    pop = [random.sample(range(8),8) for _ in range(10)]

    for _ in range(200):
        pop.sort(key=cost)
        new_pop = pop[:2]   # elitism

        while len(new_pop) < 10:
            p1,p2 = random.sample(pop[:5],2)
            child = crossover(p1,p2,crossover_type)
            if random.random() < 0.2:
                mutate(child)
            new_pop.append(child)

        pop = new_pop

    best = min(pop,key=cost)
    return best, cost(best)

# ----------------- Run -----------------
best1, c1 = genetic(False)
best2, c2 = genetic(True)

print("1-Point Crossover:", [cities[i] for i in best1], "Cost:", c1)
print("2-Point Crossover:", [cities[i] for i in best2], "Cost:", c2)