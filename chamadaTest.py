import requests
import json
from decimal import *
from excelTest import heroRelation
from excelTest import heroOption
from flask import jsonify

def main():
    hero1 = heroRelation(1).getPick()
    hero2 = heroRelation(12).getPick()
    
    option = heroOption(hero1, hero2).getOption()
    print (option)
    
if __name__ == "__main__":
    main()
