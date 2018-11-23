# -*- coding: utf-8 -*-
"""
__version__ 0.1.0

"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5



"""
a = agentframework.Agent()
print (a.y, a.x)
a.move()
print(a.y, a.x)
"""


############################################
######### Import environment ###########
########################################### 
#The pattern for dealing with looping 2D data 
        
environment = []
f = open('in.txt') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:	
    
    rowlist = []		
    for value in row:				
        rowlist.append(value)
        
    environment.append(rowlist)

f.close()
"""
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
"""

############################################

num_of_agents = 5
num_of_iterations = 3
agents = []
neighbourhood = 20


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

    
############################################
######### Call methods for each agent ######
########################################### 
for j in range(num_of_iterations):
#Check if shuffle works
    #for k in range(num_of_agents):
        #print(agents[k].x,agents[k].y)
    #print ("shuffling...")
    
    random.shuffle(agents)
#Check if shuffle works
    #for k in range(num_of_agents):
        #print(agents[k].x,agents[k].y)
    #print("----")
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat() #call eat for each agent
        agents[i].share_with_neighbours(neighbourhood)


# check store of all agents
#for i in range(num_of_agents):
#    print(agents[i].store)


############################################
######### Mapping the environment ###########
########################################### 
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(299, 0)
matplotlib.pyplot.imshow(environment)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()



###########################################################
######### Building neighbourhood method in Agent ##########
########################################################## 
"""
# Loop through the agents in self.agents .
    # Calculate the distance between self and the current other agent:
    distance = self.distance_between(agent) 
    # If distance is less than or equal to the neighbourhood
        # Sum self.store and agent.store .
        # Divide sum by two to calculate average.
        # self.store = average
            # agent.store = average
    # End if
# End loop
"""






"""
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
"""