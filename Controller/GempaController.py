import requests, xmltodict, json
import xml.etree.ElementTree as ET
from flask import jsonify

def build_xml(data):
  # Manually build the XML structure for each station
  xml_data = '<?xml version="1.0" encoding="UTF-8"?><stations>'
  for station in data:
    xml_data += f'<station><id>{station["id"]}</id><type>{station["type"]}</type><geometry><type>{station["geometry"]["type"]}</type><coordinates>{",".join(str(coord) for coord in station["geometry"]["coordinates"])}</coordinates></geometry><properties><description>{station["properties"]["description"]}</description><net>{station["properties"]["net"]}</net><sta>{station["properties"]["sta"]}</sta></properties></station>'
  xml_data += '</stations>'
  return xml_data


def convert_to_xml(geojson_data):
  root = ET.Element("FeatureCollection")

  for i, feature in enumerate(geojson_data["features"], 1):
    feature_element = ET.SubElement(root, "Feature", ID=str(i))
    for key, value in feature.items():
      if key == "geometry":
        geometry_element = ET.SubElement(feature_element,
                                         "geometry",
                                         type=value["type"])
        coordinates_element = ET.SubElement(geometry_element, "coordinates")
        for coordinate in value["coordinates"]:
          ET.SubElement(coordinates_element, "coordinate").text = ", ".join(
            str(c) for c in coordinate)
      else:
        ET.SubElement(feature_element, key).text = str(value)

  xml_data = ET.tostring(root, encoding="unicode", method="xml")
  return xml_data


def load_geojson():
  data = indo_faults_lines()
  if data:
    return json.dumps(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


#=========================
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


def histori():
  url = "https://bmkg-content-inatews.storage.googleapis.com/histori.json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


#https://bmkg-content-inatews.storage.googleapis.com/indo_faults_lines.geojson
def indo_faults_lines():
  url = "https://bmkg-content-inatews.storage.googleapis.com/indo_faults_lines.geojson"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


#fault_indo_world.geojson
def fault_indo_world():
  url = "https://bmkg-content-inatews.storage.googleapis.com/fault_indo_world.geojson"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None