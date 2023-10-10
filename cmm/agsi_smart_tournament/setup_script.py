#Package import
from agsi_teams_info import *
import requests
import json
from flask import Flask, render_template, make_response, url_for, Response, redirect, request 

 
#initialise app
app = Flask(__name__, template_folder='./templates',static_folder='./static')

#decorator for homepage 
@app.route('/' )
def index():
    return render_template('new.html')

@app.route('/', methods=['POST'])
def input_value():
    team = request.form['team_number']
    return render_template("report_card.html",
                            team_info = get_team_details(team),
                            match_details = get_match_details(team)[3],
                            calc_stats = get_calc_stats(team))
                            #add calc stats back get_calc_stats(team)

if __name__ == '__main__':
    app.run(threaded=False, debug = True, host = '0.0.0.0')