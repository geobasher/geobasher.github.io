# -*- coding: utf-8 -*-
"""
Created on Tus Oct 02 09:44:13 2018

The purpose of this code is to model 25 agents within an environment and move 
them randomly around based on the variable number. Once at a location the agent 
will take 10 from the value of the environment.

To run this program execute the code and it will display the agents and what they
have ate.

@author: Jack Gatrell
"""

#Importing relevent modules.
import agentframework
import csv
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


#Ensure the agents are able to interact with the environment.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


#Shuffle agents
random.shuffle(agents)


#Agents move and eat the environment avoiding each other.    
for j in range(num_of_iterations):#How many time the agents will move.
    for i in range(num_of_agents):#How many angents are prents in environment.
        agents[i].move()#Moves the agent.
        agents[i].eat()#Agent eats from environment.
        agents[i].share_with_neighbours(neighbourhood)#Shares stores with other agents.

       
#Animation settions
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#Used to animate agents#
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

       
#Plot points on a graph.
plt.xlim(0, 99)
plt.ylim(0, 99)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i]._x, agents[i]._y)
    print(agents[i]._x, agents[i]._y)
#ani = animation.FuncAnimation(fig, update, interval=1000, repeat=False, frames=num_of_iterations)#Could not get this to work.
plt.show()



        
