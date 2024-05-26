
from flask import Blueprint,request,render_template,jsonify
from src.db import QuearyExe
from flask_socketio import emit

query = QuearyExe()
home_bp = Blueprint("home",__name__)

from ..flask_app import socket

@home_bp.route("/", methods=['GET'])
def home():
    query = QuearyExe()
    res = query.getTiltleSponser()
    print("re",res)
    stadiums = query.Stduim_details()
    print("st",stadiums)
    return render_template("index.html",stadiums=stadiums ,title_sponsors=res)

@home_bp.route('/titleSponser', methods=['GET'])
def titleSponser():
    query = QuearyExe()
    res = query.getTiltleSponser()
    return res
    # return render_template("index.html",res)

@home_bp.route('/player', methods=['GET'])
def players():
    query = QuearyExe()
    team_name = request.args.get('team')
    res = query.Player_details_by_name(team_name)
    print("pop",res)
    return render_template("player info.html",data = res)



@socket.on("search_player_by_name")
def player_by_name():
    pass