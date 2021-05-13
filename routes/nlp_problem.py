from flask import Blueprint,request, jsonify, render_template, session,Markup,redirect,Flask
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from keras.models import model_from_json
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras import backend as K
import numpy as np
import os
import pickle

# Creating a blueprint class
nlp_problem_blueprint = Blueprint('nlp_problem',__name__,template_folder='templates')

# Fuzzy String matching
@nlp_problem_blueprint.route('/',methods=['GET','POST'],endpoint='index')
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        question = request.form.get('question')
        user_query = request.form.get('user_query')
        choices_without_splitting = request.form.get('choices')
        choices = (request.form.get('choices')).split(',')
        result = process.extract(user_query, choices)
        print(result)
        html_table = """"""
        html_table = """<table class="table">
                                  <thead>
                                    <tr>
                                      <th scope="col">S.no</th> 
                                      <th scope="col">Choices</th> 
                                      <th scope="col">Score</th> 
                                  </thead>
                                  <tbody>"""
        for i in range(0,len(result)):
            html_table = html_table + """ <tr> <th scope="row">  """ + str(i+1) + """</th>"""
            html_table = html_table + """<td>""" + str(result[i][0]) + """</td>"""
            html_table = html_table + """<td>""" + str(result[i][1]) + """</td>"""
            html_table = html_table + """</tr>"""
        html_table = html_table + """  </tbody>
                                </table>"""
        return render_template('index.html',html_table=Markup(html_table),question=question,user_query=user_query,choices=choices_without_splitting)

# Intent Classification using keras
@nlp_problem_blueprint.route('/intent',methods=['GET','POST'],endpoint='intent_classification')
def intent_classification():
    if request.method == 'GET':
        return render_template('intent_classification.html')
    elif request.method == 'POST':
        # 1. Loading the pretrained model and the tokenizer
        # load json and create model
        json_file = open('./models/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("./models/model.h5", 'r')
        print("Loaded model from disk")

        # loading tokenizer
        with open('./models/tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        phrase = request.form.get('question')

        # 2. Predicting the text
        tokens = tokenizer.texts_to_sequences([phrase])
        tokens = pad_sequences(tokens, maxlen=5500)
        prediction = loaded_model.predict(np.array(tokens))
        prediction = prediction.tolist()
        prediction = prediction[0]
        total_possible_outcomes = ['1_BookRestaurant', '2_GetWeather', '3_PlayMusic', '4_RateBook']
        list1 = prediction
        list2 = total_possible_outcomes
        prediction, total_possible_outcomes = zip(*sorted(zip(list1, list2), reverse=True))
        print("Prediction:",prediction)
        print("Total_possible_outcome:",total_possible_outcomes)
        K.clear_session()

        html_table = """"""
        html_table = """<table class="table">
                                      <thead>
                                        <tr>
                                          <th scope="col">S.no</th> 
                                          <th scope="col">Choices</th> 
                                          <th scope="col">Score</th> 
                                      </thead>
                                      <tbody>"""
        for i in range(0, len(prediction)):
            html_table = html_table + """ <tr> <th scope="row">  """ + str(i + 1) + """</th>"""
            html_table = html_table + """<td>""" + str(total_possible_outcomes [i]) + """</td>"""
            html_table = html_table + """<td>""" + str(prediction[i]) + """</td>"""
            html_table = html_table + """</tr>"""
        html_table = html_table + """  </tbody>
                                    </table>"""




        return render_template('intent_classification.html',phrase=phrase,html_table = Markup(html_table))



