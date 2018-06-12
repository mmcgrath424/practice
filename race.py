import os
import random

class race():
    def __init__(self,num_racers=4, num_gates=4):
        self.num_racers = num_racers
        self.num_gates = num_gates
        self.gates = [{} for x in range(0,self.num_gates+1)]
        for x in range(1,self.num_racers+1):
            self.gates[0].update({'r'+str(x):0})
        


    def gate_notify(self,racer, gate):
        self.gates[gate].update({racer:0})
        self.gates[gate-1].pop(racer)
            
    def racer_pos(self):
        positions = []
        for x in range(self.num_gates,-1,-1):
            if len(self.gates[x])>0:
                positions += [y for y in self.gates[x]]
        return positions


if __name__=='__main__':
    new_race = race()
    print (new_race.gates)
    new_race.gate_notify('r2',1)
    new_race.gate_notify('r3',1)
    new_race.gate_notify('r3',2)
    print (new_race.racer_pos())

    # while True:
    #     new_race.racers['r1'] += random.randint(1,15)
    #     new_race.racers['r2'] += random.randint(1,15)
    #     new_race.racers['r3'] += random.randint(1,15)
    #     new_race.racers['r4'] += random.randint(1,15)
    #     new_race.gate_notify()
    #     print (new_race.racer_pos())
    #     print (new_race.racers)
    #     if new_race.racers['r1']>200:
    #         break
        



                
