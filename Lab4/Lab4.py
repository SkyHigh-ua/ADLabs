import random

class Knapsack:
    def __init__(self, P, items, population, gen_limit):
        self.P = P
        self.items = items
        self.parents = []
        for i in range(population):
            parent = [1 if j == i else 0 for j in range(len(items))]
            self.parents.append((parent, self.fitness(parent)[0]))
        self.max_value = 0
        self.max_weight = 0
        self.gen_limit = gen_limit

    def fitness(self, chrom):
        weight_sum = 0
        value_sum = 0
        for i, gen in enumerate(chrom):
            if gen:
                weight_sum += self.items[i][0]
                value_sum += self.items[i][1]
        if weight_sum > self.P:
            return -1, None
        else: 
            return value_sum, weight_sum

    def mutation(self, chrom):
        index = random.randint(0, len(chrom)-1)
        if chrom[index]:
            chrom[index] = 0
        else: 
            chrom[index] = 1
        return chrom

    def crossover(self, chrom1, chrom2):
        l1 = int(len(chrom1)/4)
        l2 = int(len(chrom1)/2)
        l3 = l2+l1
        return chrom1[:l1]+chrom2[l1:l2]+chrom1[l2:l3]+chrom2[l3:]

    def local_improvement(self, chrom):
        items = self.items[:]
        index = items.index(max(items, key = lambda x: x[1]))
        items.pop(index)
        while chrom[index] and items:
            index = items.index(max(items, key = lambda x: x[1]))
            items.pop(index)
        chrom[index] = 1
        return chrom

    def compare(self, oldch, new_chrom, value_sum=None, weight_sum=None):
        new_value_sum, new_weight_sum = self.fitness(new_chrom)
        if new_value_sum and new_weight_sum:
            return new_chrom, new_value_sum, new_weight_sum
        else:
            if not value_sum and not weight_sum:
                value_sum, weight_sum = self.fitness(oldch)
            return oldch, value_sum, weight_sum 

    def choose_parent(self):
        parent1 = self.parents.index(max(self.parents, key = lambda x: x[1]))
        parent2 = random.randint(0, len(self.parents)-1)
        while parent1 == parent2:
            parent2 = random.randint(0, len(self.parents)-1)
        return self.parents[parent1][0], self.parents[parent2][0]

    def genetic_algorith(self):
        generation = 0
        for item in self.parents:
            if item[1] > self.max_value:
                self.max_value = item[1]
                self.max_weight = self.fitness(item[0])[1]
        while (self.max_weight < self.P and generation < self.gen_limit):
            parent_chroms = self.choose_parent()
            new_chrom = self.crossover(parent_chroms[0], parent_chroms[1])
            value_sum, weight_sum = None, None
            if random.uniform(0, 1) <= 0.05:
                new_chrom, value_sum, weight_sum = self.compare(new_chrom, self.mutation(new_chrom))
            new_chrom, value_sum, weight_sum = self.compare(new_chrom, self.local_improvement(new_chrom), value_sum, weight_sum)
            if value_sum > self.max_value:
                self.max_value = value_sum
                self.max_weight = weight_sum
            self.parents[self.parents.index(min(self.parents, key = lambda x: x[1]))] = (new_chrom, value_sum)
            generation += 1
        return self.parents[self.parents.index(max(self.parents, key = lambda x: x[1]))], self.max_weight, generation

def generate_items(n):
    return [(random.randint(1, 25), random.randint(2, 30)) for _ in range(n)]

def saveitems(items):
    with open("./Lab4/Knapsackitems.txt", "w") as f:
        print("\n".join([f"Item #{i+1};Weight - {item[0]};Value - {item[1]}" for i, item in enumerate(items)]), file=f)

if __name__ == "__main__":
    P = 250
    n = 100
    population = 100
    gen_limit = 1000
    items = generate_items(n)
    obj = Knapsack(P, items, population, gen_limit)
    result = obj.genetic_algorith()
    saveitems(items)
    if result[2] == gen_limit:
        print("Max generation limit reached")
    else:
        print(f"Result found in generation №{result[2]}")
    print(f"Сhromosome - {', '.join([str(i) for i in result[0][0]])}\nValue - {result[0][1]}\nWeight - {result[1]}")