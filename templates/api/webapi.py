import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

jokes = []
joke_list = [
    "Myles Henderson, Sr. #23",
    "Benny Herrick, Sr. #11",
    "Troy Cresto, Sr. #3",
    "Austin Del Castillo, Sr. #24",
    "Bradley Bartelt, Sr. #18",
    "Owen Ross, Sr. #8",
    "Subaeg Gill, Sr. #15",
    "Dylan McGee, Jr. #5",
    "Gavin Kirby, Jr. #12",
    "Shane O’Neal, Jr. #9",
    "Kyson Cockrell, Jr. #19",
    "Andrew McKinnon, So. #13",
    "Cameron Dale, So. #2",
    "Jayden Chen, Fr. #17",
]


def _find_next_id():
    return max(jokes["id"] for joke in jokes) + 1


def _init_jokes():
    id = 1
    for joke in joke_list:
        jokes.append({"id": id, "joke": joke, "haha": 0, "boohoo": 0})
        id += 1


@app_starter.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("starter/joke.html", joke=response.json())


@app_starter.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("starter/jokes.html", jokes=response.json())


@app_starter.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("starter/covid19.html", stats=response.json())

if __name__ == "__main__":
    print(random.choice(joke_list))