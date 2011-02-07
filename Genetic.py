import random, math

class Genetic:

  def __init__(self):
    self.file_name = ""
    self.generation = 0
    self.no_of_parents = 0

    self.population = []
    self.cost_matrix = []
    self.population_cost_matrix = []

    self.crossover_point = ()

    self.mutate_probability = 0.05
    self.crossover_probablitiy = 0.70
    
  
  def read_file(self):
    file = open(self.file_name, 'r')
    allLines = file.readlines()
    file.close()
    for eachLine in allLines:
      self.cost_matrix.append(eachLine.split())  
  
  def create_population(self):
    for parent in range(0,self.no_of_parents):
      one = range(0, len(self.cost_matrix))
      random.shuffle(one)
      self.population.append(one)

  def calc_crossover_point(self):
    length = float(len(self.cost_matrix))
    point1 = int(math.floor((length/3)))
    point2 = int(length) - point1
    self.crossover_point = (point1, point2)

  def crossover(self, parent1, parent2):
    child1 = self.create_child(parent1, parent2)
    child2 = self.create_child(parent2, parent1)
    return (child1, child2)

  def create_child(self, parent1, parent2):
    #Get middle of parent
    child = parent1[self.crossover_point[0]:self.crossover_point[1]]
  
    tmp = parent2[self.crossover_point[1]:]
    tmp.extend(parent2[:self.crossover_point[1]])
    
    #remove duplicate nodes from parent2
    new_nodes = filter(lambda x: x not in child, tmp)

    #add elements to end of parent
    child.extend(new_nodes[:self.crossover_point[0]-1])
    
  
    #add elements to front of parent
    elements = new_nodes[self.crossover_point[0]-1:len(new_nodes)]
    elements.extend(child)

    return elements

  def mutate(self, individual):
    swap_position = random.sample(range(0,len(individual)), 2)
    individual[swap_position[0]], individual[swap_position[1]] = individual[swap_position[1]], individual[swap_position[0]]
    # return individual

  def sort_selection(self, individuals):
    individuals.sort(lambda x, y: cmp(x[0],y[0]))
    
  def evaluate_path(self, val):
    sum = 0
    start = 0
    while start < len(val) - 1:
      sum += float(self.cost_matrix[val[start]][val[start+1]])
      start +=1
    sum += float(self.cost_matrix[val[len(val)-1]][val[0]])
    return sum


  # Create new population, and replace existing one. 
  def cool(self):
    self.generation += 1
    new_population = []
    
    while len(new_population) < len(self.population):
      
      #Tournament selection
      individuals = random.sample(self.population_cost_matrix, 10)

      self.sort_selection(individuals)
      lucky_individual1 , lucky_individual2 = individuals[0], individuals[1]

      pC = random.random()
      if pC <= self.crossover_probablitiy:
        children = self.crossover(lucky_individual1[1], lucky_individual2[1])

        for child in children:
          pM = random.random()

          if pM <= self.mutate_probability:
            self.mutate(child)
           
          new_population.append(child)
      else:
        new_population.append(lucky_individual1[1])
        new_population.append(lucky_individual2[1])
      
    self.population = new_population
    self.fitness()

  def fitness(self):
    self.population_cost_matrix = []
    for individual in self.population:
      fitness = 0
      index = 0
      while index < len(individual) - 1:
        fitness += float(self.cost_matrix[individual[index]][individual[index+1]])
        index +=1
      fitness += float(self.cost_matrix[individual[len(individual)-1]][individual[0]])
      self.population_cost_matrix.append((fitness, individual))