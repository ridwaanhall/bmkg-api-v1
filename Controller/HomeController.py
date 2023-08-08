import json


def load_home_json():
  with open('datahome/home.json', 'r') as json_file:
    data = json.load(json_file)
  return data
