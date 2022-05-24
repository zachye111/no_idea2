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

joke_list4 = [
    "February 17th @ Carlsbad: JV – 4:30 PM; Varsity – 5:30 PM",
    "March 1st vs. Torrey Pines: JV- 4:30 PM; Varsity – 5:30 PM",
    "March 4th – Best of the West Varsity Tournament: vs. Mira Costa – 3 PM; San Clemente – 5 PM; Campolindo – 7 PM",
    "March 5th – Best of the West Tournament Day 2: vs. Buchanan;",
    "March 11th – La Jolla HS Mini Tournament @ LJHS: Times TBD",
    "March 22nd @ Sage Creek: JV – 4:30 PM; Varsity – 5:30 PM",
    "March 23rd vs. Poway: JV – 4:30 PM; Varsity – 5:30 PM",
    "March 26th – Sage Creek JV Tournament: Times TBD",
    "March 29th @ Poway: JV – 4:00 PM; Varsity – 5:00 PM",
    "March 30th @ Otay Ranch: JV – 4:30 PM; Varsity – 5:30 PM",
    "March 31st @ Mt. Carmel: JV – 4:30 PM; Varsity – 5:30 PM",
    "April 1st vs. Cathedral: JV – 4:30 PM; Varsity- 5:30 PM",
    "April 5th vs. Rancho Bernardo: JV – 4:30 PM; Varsity – 5:30 PM",
    "April 7th vs. TBD?: JV – 4:30 PM Varsity – 5:30 PM",
    "April 19th vs. Mt. Carmel: JV – 4:30 PM; Varsity – 5:30 PM",
    "April 25th @ Rancho Bernardo: JV – 4:00 PM; Varsity – 5:30 PM",
    "April 22nd @ Westview: JV – 4:30 PM; Varsity – 5:30 PM",
    "April 28th vs. Westview: JV – 4:30 PM; Varsity – 5:30 PM (SENIOR NIGHT!!)",
    "May 3rd @ San Marcos – 7:00 PM (Open Playoffs 1st Round)",
    "May 5th vs. Sage Creek – 7:00 PM (Open Playoffs 2nd Round)",
    "May 7th @ Westview (Open Playoffs 3rd Round)",
    "May 14th: CIF Open Division Finals",
    "May 17th & 18th: State Playoffs – TBD,",
]

def _find_next_id():
    return max(jokes["id"] for joke in jokes) + 1


def _init_jokes():
    id = 1
    for joke in joke_list:
        jokes.append({"id": id, "joke": joke, "haha": 0, "boohoo": 0})
        id += 1


