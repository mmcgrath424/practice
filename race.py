import os
import random

class race():
    def __init__(self):
        self.racers = {'r1':0,'r2':0,'r3':0,'r4':0}
        self.start = {'r1':0,'r2':0,'r3':0,'r4':0}
        self.g1 = {}
        self.g2 = {}
        self.g3 = {}
        self.g4 = {}
        self.g1_dist = 50
        self.g2_dist = 100
        self.g3_dist = 150
        self.g4_dist = 200

    def gate_notify(self):
        for key,value in self.racers.items():
            if (self.g1_dist <= value <= self.g2_dist) and (key not in self.g1) :
                self.g1.update({key:value})
                self.start.pop(key)
                print ("Runner "+key+" has passed gate 1")
            elif (self.g2_dist <= value <= self.g3_dist) and (key not in self.g2):
                self.g2.update({key:value})
                self.g1.pop(key)
                print ("Runner "+key+" has passed gate 2")
            elif (self.g3_dist <= value <= self.g4_dist) and (key not in self.g3):
                self.g3.update({key:value})
                self.g2.pop(key)
                print ("Runner "+key+" has passed gate 3")
            elif (self.g4_dist <= value) and (key not in self.g4):
                self.g4.update({key:value})
                self.g3.pop(key)
                print ("Runner "+key+" has passed gate 4")
            
    def racer_pos(self):
        positions = []
        if len(self.g4) >0:
            positions = [x for x in self.g4.keys()]
        if len(self.g3) >0:
            positions += [x for x in self.g3.keys()]
        if len(self.g2) >0:
            positions += [x for x in self.g2.keys()]
        if len(self.g1) >0:
            positions += [x for x in self.g1.keys()]
        if len(self.start) >0:
            positions += [x for x in self.start.keys()]
        return positions

if __name__=='__main__':
    new_race = race()

    while True:
        new_race.racers['r1'] += random.randint(1,15)
        new_race.racers['r2'] += random.randint(1,15)
        new_race.racers['r3'] += random.randint(1,15)
        new_race.racers['r4'] += random.randint(1,15)
        new_race.gate_notify()
        print (new_race.racer_pos())
        print (new_race.racers)
        if new_race.racers['r1']>200:
            break
        
    print (new_race.racers)


                
