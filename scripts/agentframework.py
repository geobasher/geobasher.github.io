# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:11:19 2018

@author: Jack Gatrell

The purpose of this module is to define agent location, movementment and attributes.
"""

import random


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
    
    def move(self):
        if random.random() <0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

        if random.random() <0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
    
    def eat(self):# can you make it eat what is left?
        if self.environment[self._y][self._x] > 0:
            self.environment[self._y][self._x] -= 10
            self.store += 10
    
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
   