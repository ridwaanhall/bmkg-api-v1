import requests, xmltodict


def GempaNews():
  url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


def last30event():
  url = "https://bmkg-content-inatews.storage.googleapis.com/last30event.xml"
  response = requests.get(url)
  data_dict = xmltodict.parse(response.content)
  return data_dict


def last30feltevent():
  url = "https://bmkg-content-inatews.storage.googleapis.com/last30feltevent.xml"
  response = requests.get(url)
  return response.content


def last30tsunamievent():
  url = "https://bmkg-content-inatews.storage.googleapis.com/last30tsunamievent.xml"
  response = requests.get(url)
  return response.content


def live30event():
  url = "https://bmkg-content-inatews.storage.googleapis.com/live30event.xml"
  response = requests.get(url)
  return response.content
