import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

jokes = []
joke_list = [
    "Myles Henderson Sr. #23",
    "Benny Herrick Sr. #11",
    "Troy Cresto Sr. #3",
    "Austin Del Castillo Sr. #24",
    "Bradley Bartelt Sr. #18",
    "Owen Ross Sr. #8",
    "Subaeg Gill Sr. #15",
    "Dylan McGee Jr. #5",
    "Gavin Kirby Jr. #12",
    "Shane O’Neal Jr. #9",
    "Kyson Cockrell Jr. #19",
    "Andrew McKinnon So. #13",
    "Cameron Dale So. #2",
    "Jayden Chen Fr. #17",
]

joke_list2 = [
    "Nematt Lalehzarian",
    "Declan Cockrell",
    "Brandon So",
    "Will Bartelt",
    "Chris Albertson",
    "Ninaad Kiran",
    "Grant Dennison",
    "Paul Tassos",
    "David Lee",
    "Alex Traina",
    "Riley Namin",
    "Gabriel Pearl",
    "Dylan Quan",
]

joke_list3 = [
    "Rayhan Shamly",
    "Ali Almahdawi",
    "Noah Kim",
    "Sean Choi",
    "Beijan Moniza",
    "Samarth Kalankr",
    "Eric Kownacki",
    "Rabi Mohammad",
    "Joshua Thinh",
    "Levi Stratton",
    "Ryan Liao",
    "Lucas Moore",
    "Walid Alsaialy",
    "Michael Chappius",
]

def _find_next_id():
    return max(jokes["id"] for joke in jokes) + 1


def _init_jokes():
    id = 1
    for joke in joke_list:
        jokes.append({"id": id, "joke": joke, "haha": 0, "boohoo": 0})
        id += 1


