import Genetic, euclidean

print "Initialising"
genetic = Genetic.Genetic()

#Set file name
genetic.file_name = "tspadata2.txt"

#read file
genetic.read_file()

#set number of parents
genetic.population_size = 1000


#Create population
genetic.create_population()

#Calcuate the crossover points
genetic.calc_crossover_point()

#calculate fitness
genetic.fitness()

while genetic.generation < 1000:
  genetic.evaluate()
  genetic.tmp_function()
  print ("%d -> %d - > %s") % (genetic.generation, genetic.fittest[0], genetic.fittest[1])

