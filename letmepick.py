import flask
import requests
import logging
from flask import request, jsonify
from excelTest import heroRelation
from excelTest import heroOption

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/heroes/all', methods=['GET'])
def api_all():
    return jsonify(heroes)
    
@app.route('/api/v1/resources/heroes', methods=['GET'])
def api_id():
    # Valida se há algum id informado na requisição (i.e.: /api/v1/resources/heroes?pick1=1&pick2=2)
    if 'pick1' in request.args:
        pick1 = int(request.args['pick1'])
    else:
        logging.error("Error: Não foi informado um pick. Favor informar o id no formato '/api/v1/resources/heroes?pick1=1'.")
    if 'pick2' in request.args:
        pick2 = int(request.args['pick2'])
    else:
        logging.error("Error: Não foi informado um pick 2. Favor informar o id no formato '/api/v1/resources/heroes?pick2=1'.")
    
    logging.info("pick1 = "+str(pick1)+" pick2 = "+str(pick2))
    
    hero1 = heroRelation(pick1).getPick()
    hero2 = heroRelation(pick2).getPick()
    option = heroOption(hero1, hero2).getOption()
    return jsonify(option)

app.run()