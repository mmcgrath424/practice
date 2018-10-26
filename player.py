import os

class Player():
    def __init__(self,ids,name,sport,pos,team,cost,fppg,val):
        self._ids = ids
        self._name = name
        self._sport = sport
        self._position = pos
        self._team = team
        self._cost = cost
        self._avgPts = fppg
        self._value = val

    @property
    def ids(self):
        return self.ids
    @ids.setter
    def ids(self,value):
        self._ids = value
    @property
    def name(self):
        return self._name
    @property
    def sport(self):
        return self._sport
    @property
    def position(self):
        return self._position
    @property
    def team(self):
        return self._team
    @property
    def cost(self):
        return self._cost
    @property
    def avgPts(self):
        return self._avgPts
    @property
    def value(self):
        return self._value

    @name.setter
    def name(self,value):
        self._name = value
    @sport.setter
    def sport(self,value):
        self._sport = value
    @position.setter
    def position(self,value):
        self._position = value
    @team.setter
    def team(self,value):
        self._team = value
    @cost.setter
    def cost(self,value):
        self._cost = value
    @avgPts.setter
    def avgPts(self,avgPts):
        self.avgPts = avgPts
    @value.setter
    def value(self):
        if self.cost != None and self.avgPts != None:
            self.value = self.cost/self.avgPts
        else:
            print("Cost and average points not set yet")



class FDNFLLineup():
    
    def __init__(self):
        self.qb = None
        self.rb1 = None
        self.rb2 = None
        self.wr1 = None
        self.wr2 = None
        self.wr3 = None
        self.te = None
        self.flex = None
        self.defense = None

    @property
    def qb(self):
        return self.qb
    @qb.setter
    def qb(self,qb):
        self.qb = qb
    @property
    def rb1(self,rb1):
        return self.rb1
    @rb1.setter
    def rb1(self,rb1):
        self.rb1 = rb1
    @property
    def rb2(self):
        return self.rb2
    @rb2.setter
    def rb2(self,rb2):
        self.rb2 = rb2
    @property
    def wr1(self):
        return self.wr1
    @wr1.setter
    def wr1(self,wr1):
        self.wr1 = wr1
    @property
    def wr2(self):
        return self.wr2
    @wr2.setter
    def wr2(self,wr2):
        self.wr2 = wr2
    @property
    def wr3(self):
        return self.wr3
    @wr3.setter
    def wr3(self,wr3):
        self.wr3 = wr3
    @property
    def te(self):
        return self.te
    @te.setter
    def te(self,te):
        self.te = te
    @property
    def flex(self):
        return self.flex
    @flex.setter
    def flex(self,flex):
        self.flex = flex
    @property
    def defense(self):
        return self.defense
    @defense.setter
    def defense(self,defense):
        self.defense = defense

class FDNBALineup():
    
    def __init__(self):
        self.pg1 = None
        self.pg2 = None
        self.sg1 = None
        self.sg2 = None
        self.sf1 = None
        self.sf2 = None
        self.pf1 = None
        self.pf2 = None
        self.cen = None
        self.salary_cap = 60000
        self.salary_rem = 60000

    @property
    def pg1(self):
        return self.pg1
    @pg1.setter
    def pg1(self,pg):
        self.pg1 = pg
    @property
    def pg2(self):
        return self.pg2
    @pg2.setter
    def pg2(self,pg):
        self.pg2 = pg
    @property
    def sg1(self):
        return self.sg1
    @sg1.setter
    def sg1(self,sg):
        self.sg1 = sg
    @property
    def sg2(self):
        return self.sg2
    @sg2.setter
    def sg2(self,sg):
        self.sg2 = sg
    @property
    def sf1(self):
        return self.sf1
    @sf1.setter
    def sf1(self,sf):
        self.sf1 = sf
    @property
    def sf2(self):
        return self.sf2
    @sf2.setter
    def sf2(self,sf):
        self.sf2 = sf
    @property
    def pf1(self):
        return self.pf1
    @pf1.setter
    def pf1(self,pf):
        self.pf1 = pf
    @property
    def pf2(self):
        return self.pf2
    @pf2.setter
    def pf2(self,pf):
        self.pf2 = pf
    @property
    def cen(self):
        return self.cen
    @cen.setter
    def cen(self,cen):
        self.cen = cen
    
    def print_lineup(self):
        print(self.pg1)
        print(self.pg2)
        print(self.sg1)
        print(self.sg2)
        print(self.sf1)
        print(self.sf2)
        print(self.pf1)
        print(self.pf2)
        print(self.cen)
        print(self.salary_rem)

class CreateDataSetNBA():
    def __init__(self):
        self._pg_pool = set()
        self._sg_pool = set()
        self._sf_pool = set()
        self._pf_pool = set()
        self._cen_pool = set()
        self.csv_file = None

    @property
    def pg_pool(self):
        return self._pg_pool
    @pg_pool.setter
    def pg_pool(self,value):
        self._pg_pool = value
    @property
    def sg_pool(self):
        return self._sg_pool
    @sg_pool.setter
    def sg_pool(self,value):
        self._sg_pool = value
    @property
    def sf_pool(self):
        return self.sf_pool
    @sf_pool.setter
    def sf_pool(self,value):
        self._sf_pool = value
    @property
    def pf_pool(self):
        return self._pf_pool
    @pf_pool.setter
    def pf_pool(self,value):
        self._pf_pool = value
    @property
    def cen_pool(self):
        return self._cen_pool
    @cen_pool.setter
    def cen_pool(self,value):
        self._cen_pool = value

# open csv
    def file_open(self,filename):
        self.csv_file = open(filename)

    def add_check (self, pos, data):
        if pos in data[1]:
            return 1
        else: 
            return 0
        
    
    def parse_file(self):
        ids = 0
        pos = 1
        fname = 2
        nname = 3
        lname = 4
        fppg = 5
        played = 6
        sal = 7
        game = 8
        team = 9
        opp = 10
        inj_ind = 11
        inj_det = 12
        tier = 13
        empty1 = 14
        empty2 = 15
        
        line = self.csv_file.readline()
        line = self.csv_file.readline()
        while line != "":
            spl = line.split(",")
            if self.add_check("PG",spl) and float(spl[fppg][1:-1])>0:
                self._pg_pool.add(Player(spl[0][1:-1],spl[nname][1:-1],"BBall",spl[pos][1:-1],spl[team][1:-1],int(spl[sal][1:-1]),float(spl[fppg][1:-1]),float(spl[sal][1:-1])/float(spl[fppg][1:-1])))
                print ("pg added")
            line = self.csv_file.readline()

    def print_pg(self):
        for x in self.pg_pool:

            print (x.name + " " + str(x.value))    


if __name__=='__main__':
    test = CreateDataSetNBA()
    test.file_open("FDNBAPlayers.csv")
    test.parse_file()
    test.print_pg()

        

    