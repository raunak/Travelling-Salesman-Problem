import Genetic

print "Initialising"
genetic = Genetic.Genetic()

#Set file name
genetic.file_name = "tspadata2.txt"

#read file
genetic.read_file()

#set number of parents
genetic.no_of_parents = 1000


#Create population
genetic.create_population()

#Calcuate the crossover points
genetic.calc_crossover_point()

#calculate fitness
genetic.fitness()


cost = 0

while genetic.generation < 1000:
  genetic.cool()

  tmp =genetic.population_cost_matrix
  genetic.sort_selection(tmp)
  nCost =  tmp[0][0]

  if cost != nCost:
	print ("%d -> %f") % (genetic.generation, nCost)
	cost = nCost

for p in genetic.population_cost_matrix:
	print p