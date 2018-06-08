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
        positions.append(list(self.g4.keys()))
        positions.append(list(self.g3.keys()))
        positions.append(list(self.g2.keys()))
        positions.append(list(self.g1.keys()))
        positions.append(list(self.start.keys()))
        return positions

if __name__=='__main__':
    new_race = race()

    while True:
        new_race.racers['r1'] += random.randint(1,5)
        new_race.racers['r2'] += random.randint(1,5)
        new_race.racers['r3'] += random.randint(1,5)
        new_race.racers['r4'] += random.randint(1,5)
        new_race.gate_notify()
        print (new_race.racer_pos())
        if new_race.racers['r1']>200:
            break
        
    print (new_race.racers)


                
