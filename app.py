# Import Necessary Libraries
from flask import Flask, render_template, request,redirect, session,url_for
from flask import Flask,jsonify,Markup, session, Response
import os
# Importing Blueprints defined in the routes -> adult_statistics.py
from routes.nlp_problem import nlp_problem_blueprint


app = Flask(__name__)


# Blueprints
app.register_blueprint(nlp_problem_blueprint)


if __name__ == "__main__":
    app_host = "0.0.0.0"
    app_port = 8003
    app.run(host=app_host, port=app_port, debug=False, threaded=True)
