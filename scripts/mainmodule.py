# -*- coding: utf-8 -*-
"""
Created on Tuesday Oct 09 09:20:25 2018

@author: Jack Gatrell

The purpose of this module is to create a Agent Based Model to interacts with an
environment.
"""


import agentframework
import csv
import operator
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('classic')


#Variable values.
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#Making the tables
agents = []
environment = []
rowlist = []

#Inputing the data in to the environment table.
with open("in.txt") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for rowlist in reader:
        environment.append(rowlist)
        
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


#Shuffle agents
random.shuffle(agents)


fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

def update(frame_number):
    
    fig.clear()
    
    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0] = (agents[i][0] + 1) % 99 
            else:
                agents[i][0] = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1] = (agents[i][1] + 1) % 99 
            else:
                agents[i][1] = (agents[i][1] - 1) % 99   
 

#Agents move and eat the environment avoiding each other.    
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
       

       
#Plot points on a graph.
plt.xlim(0, 99)
plt.ylim(0, 99)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i]._x, agents[i]._y)
    print(agents[i]._x, agents[i]._y)
ani = animation.FuncAnimation(fig, update, interval=1000, repeat=False, frames=num_of_iterations)
plt.show()



        
