import pandas as pd
import requests
import json
import logging
from decimal import *

with open('heroes.json') as json_file:
    heroes = json.load(json_file)
            
class heroRelation:
    def __init__(self, hero):
        self.hero = hero
#        logging.info("heroRelation Class > recived values pick1: " +str(hero))
    def getPick(self):
        r = requests.get('https://api.opendota.com/api/heroes/'+str(self.hero)+'/matchups').text
        a = json.loads(r)
        getcontext().prec = 2
        score = 0.55
        matchup = []
        for hero in a:
            if (Decimal(hero["wins"])/Decimal(hero["games_played"])) > score:
                matchup.append(hero["hero_id"])
        return(matchup)
    
class heroOption:
    def __init__(self, options1, options2):
        self.options1 = options1
        self.options2 = options2
        logging.info("heroOption Class > reviced both heroes options")
    def getOption(self):
        opcao = []
        
        if len(self.options1) >= len(self.options2):
            z = len(self.options2)
        else:
            z = len(self.options1)
        
        print("op1 len: "+str(len(self.options1)) + " | op2 len: " +str(len(self.options2)))
        print("Z: "+str(z))
        self.options1.sort()
        self.options2.sort()
        print(self.options1)
        print(self.options2)
        
        escolha = []
        x = 0
        while x < z:
            i = 0
            while i < z:
                if self.options1[x] is self.options2[i]:
                    p = self.options1[x]
                    escolha.append(p)
                i = i + 1
            x = x + 1
        t = 0
        while t < len(escolha):
            for hero in heroes:
                if hero["id"] is escolha[t]:
                    opcao.append(hero)
            t = t + 1
            
        return(opcao)