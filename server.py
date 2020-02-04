import http.server
import socketserver
import requests
import json
from flask import Flask
from flask import render_template

# start the environment
#. venv/bin/activate
#use these before running project & after starting the venv
# export FLASK_APP=server.py
# export FLASK_ENV=development
# flask run

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

app = Flask(__name__)
base_url = "https://api.clashroyale.com/v1/"
player_tag = "%232JQQYUU"
# endpoint = "clans?minMembers=20"
endpoint = "players/"+player_tag
chest_endpoint = "players/"+player_tag+"/upcomingchests"
cards_endpoint = base_url + "cards"
#   my_key = f.read().rstrip("\n")
# with open("my_api_key.txt") as f:
with open("home_api.txt") as f:
  my_key = f.read().rstrip("\n")

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/cards')
def cards():
  response = requests.get(cards_endpoint,  {"Authorization": "Bearer %s" %my_key })
  data = json.loads(response.content)
  return data

@app.route('/test')
def test():
  return render_template('index.html')


response = requests.get(base_url + endpoint,  {"Authorization": "Bearer %s" %my_key })
chest_response = requests.get(base_url + chest_endpoint,  {"Authorization": "Bearer %s" %my_key })

data = json.loads(response.content)
chest_data = json.loads(chest_response.content)
print('Name: {0} Trophies: {1}'.format(data["name"], data["trophies"]))
print(chest_data)
# for item in data["items"]:
#   # print('{0} [{1}]'.format(item["name"], item["maxLevel"]))
#   print('Clan:{0} \n Members[{1}] \nScore:{2}\n Tag:{3}\n\n'.format(item["name"], item["members"], item["clanScore"], item["tag"] ))

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
