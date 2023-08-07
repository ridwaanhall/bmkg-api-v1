import requests, xmltodict


def datagempa():
  url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


def last30event():
  url = "https://bmkg-content-inatews.storage.googleapis.com/last30event.xml"
  response = requests.get(url)
  xml_data = response.content
  data_dict = xmltodict.parse(xml_data)
  return data_dict


def last30feltevent():
  url = "https://bmkg-content-inatews.storage.googleapis.com/last30feltevent.xml"
  response = requests.get(url)
  xml_data = response.content
  data_dict = xmltodict.parse(xml_data)
  return data_dict


def last30tsunamievent():
  url = "https://bmkg-content-inatews.storage.googleapis.com/last30tsunamievent.xml"
  response = requests.get(url)
  xml_data = response.content
  data_dict = xmltodict.parse(xml_data)
  return data_dict


def live30event():
  url = "https://bmkg-content-inatews.storage.googleapis.com/live30event.xml"
  response = requests.get(url)
  xml_data = response.content
  data_dict = xmltodict.parse(xml_data)
  return data_dict
