import requests, xmltodict


def build_xml(data):
  # Manually build the XML structure for each station
  xml_data = '<?xml version="1.0" encoding="UTF-8"?><stations>'
  for station in data:
    xml_data += f'<station><id>{station["id"]}</id><type>{station["type"]}</type><geometry><type>{station["geometry"]["type"]}</type><coordinates>{",".join(str(coord) for coord in station["geometry"]["coordinates"])}</coordinates></geometry><properties><description>{station["properties"]["description"]}</description><net>{station["properties"]["net"]}</net><sta>{station["properties"]["sta"]}</sta></properties></station>'
  xml_data += '</stations>'
  return xml_data


def datagempa():
  url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


def EmgempaQL():
  url = "https://bmkg-content-inatews.storage.googleapis.com/3mgempaQL.json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


def katalog_gempa():
  url = "https://bmkg-content-inatews.storage.googleapis.com/katalog_gempa.json"
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
  '''
  this api using UTC Time.
  '''
  url = "https://bmkg-content-inatews.storage.googleapis.com/live30event.xml"
  response = requests.get(url)
  xml_data = response.content
  data_dict = xmltodict.parse(xml_data)
  return data_dict


def sensor_seismic():
  url = "https://bmkg-content-inatews.storage.googleapis.com/sensor_seismic.json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


def sensor_global():
  url = "https://bmkg-content-inatews.storage.googleapis.com/sensor_global.json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None
