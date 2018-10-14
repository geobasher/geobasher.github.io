# -*- coding: utf-8 -*-
"""
Created on Tus Oct 02 09:58:17 2018

The purpose of this code is to model the agents behaviour within the environment

@author: Jack Gatrell
"""


import random

#Creates the random location of each agent.
class Agent:
    def __init__(self, environment, agents):
        self._x = random.randint(0,99) 
        self._y = random.randint(0,99) 
        self.environment = environment
        self.agents = agents
        self.store = 0     
     
              
    @property
    def getx(self):
        return self._x
    
    
    @property
    def gety(self):
        return self._y
    
    
    @getx.setter
    def setx(self, value):
        self.x = random.randint(0,99)
    
    
    @gety.setter
    def sety(self, value):
        self.y = random.randint(0,99)
    
    #Moves each agent around the environment randomly.
    def move(self):
        if random.random() <0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

        if random.random() <0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
    
    #Agent eats 10 from the environment.
    def eat(self):
            if self.environment[self._y][self._x] > 0:
                self.environment[self._y][self._x] -= 10
                self.store += 10
     
    #Calculates the distance between each agent.       
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    #Shares store with closest agent.
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                
   