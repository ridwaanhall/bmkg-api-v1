import requests, xmltodict, json
import xml.etree.ElementTree as ET
from flask import jsonify, Response


class GempaController:

  @staticmethod
  def build_xml(data):
    # Manually build the XML structure for each station
    xml_data = '<?xml version="1.0" encoding="UTF-8"?><stations>'
    for station in data:
      xml_data += f'<station><id>{station["id"]}</id><type>{station["type"]}</type><geometry><type>{station["geometry"]["type"]}</type><coordinates>{",".join(str(coord) for coord in station["geometry"]["coordinates"])}</coordinates></geometry><properties><description>{station["properties"]["description"]}</description><net>{station["properties"]["net"]}</net><sta>{station["properties"]["sta"]}</sta></properties></station>'
    xml_data += '</stations>'
    return xml_data

  @staticmethod
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

  @staticmethod
  def load_geojson():
    data = GempaController.indo_faults_lines()
    if data:
      return json.dumps(data)
    else:
      return jsonify({"message": "Failed to fetch data."}), 500

  @staticmethod  # fetch json data
  def fetch_json_data(url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    else:
      return None

  # ====================== new =====

  # xml_root_response
  @staticmethod
  def xml_root_response(data):
    if data:
      wrapped_data = {"root": data}
      xml_data = xmltodict.unparse(wrapped_data, pretty=True)
      return Response(xml_data, content_type='text/xml')
    else:
      return jsonify({"message": "Failed to fetch data."}), 500

  # json_if
  @staticmethod
  def json_if(data):
    if data:
      return jsonify(data)
    else:
      return jsonify({"mzessage": "Failed to fetch data."}), 500

  # xml_response
  @staticmethod
  def xml_response(data):
    response = Response(xmltodict.unparse(data, pretty=True),
                        content_type='application/xml')
    return response

  # faults_xml
  @staticmethod
  def faults_xml(data):
    if data:
      xml_data = GempaController.convert_to_xml(data)
      return Response(xml_data, content_type='text/xml')
    else:
      return jsonify({"message": "Failed to fetch data."}), 500

  # faults_geojson
  @staticmethod
  def faults_geojson(geojson_data):
    if geojson_data:
      return Response(geojson_data, content_type='application/json')
    else:
      return jsonify({"message": "Failed to fetch data."}), 500

  # sgb_build_xml
  @staticmethod
  def sensor_global_build_xml(data):
    if data:
      xml_data = GempaController.build_xml(data)
      return Response(xml_data, content_type='text/xml')
    else:
      return jsonify({"message": "Failed to fetch data."}), 500

  #========================= url ====================
  @staticmethod  # DATA GEMPA
  def datagempa():
    url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
    json_data = GempaController.fetch_json_data(url)
    return json_data

  @staticmethod
  def EmgempaQL():
    url = "https://bmkg-content-inatews.storage.googleapis.com/3mgempaQL.json"
    json_data = GempaController.fetch_json_data(url)
    return json_data

  @staticmethod
  def katalog_gempa():
    url = "https://bmkg-content-inatews.storage.googleapis.com/katalog_gempa.json"
    json_data = GempaController.fetch_json_data(url)
    return json_data

  @staticmethod
  def last30event():
    url = "https://bmkg-content-inatews.storage.googleapis.com/last30event.xml"
    response = requests.get(url)
    xml_data = response.content
    data_dict = xmltodict.parse(xml_data)
    return data_dict

  @staticmethod
  def last30feltevent():
    url = "https://bmkg-content-inatews.storage.googleapis.com/last30feltevent.xml"
    response = requests.get(url)
    xml_data = response.content
    data_dict = xmltodict.parse(xml_data)
    return data_dict

  @staticmethod
  def last30tsunamievent():
    url = "https://bmkg-content-inatews.storage.googleapis.com/last30tsunamievent.xml"
    response = requests.get(url)
    xml_data = response.content
    data_dict = xmltodict.parse(xml_data)
    return data_dict

  @staticmethod
  def live30event():
    '''
    this api using UTC Time.
    '''
    url = "https://bmkg-content-inatews.storage.googleapis.com/live30event.xml"
    response = requests.get(url)
    xml_data = response.content
    data_dict = xmltodict.parse(xml_data)
    return data_dict

  @staticmethod
  def sensor_seismic():
    url = "https://bmkg-content-inatews.storage.googleapis.com/sensor_seismic.json"
    json_data = GempaController.fetch_json_data(url)
    return json_data

  @staticmethod
  def sensor_global():
    url = "https://bmkg-content-inatews.storage.googleapis.com/sensor_global.json"
    json_data = GempaController.fetch_json_data(url)
    return json_data

  @staticmethod
  def histori():
    url = "https://bmkg-content-inatews.storage.googleapis.com/histori.json"
    json_data = GempaController.fetch_json_data(url)
    return json_data

  #https://bmkg-content-inatews.storage.googleapis.com/indo_faults_lines
  @staticmethod
  def indo_faults_lines():
    url = "https://bmkg-content-inatews.storage.googleapis.com/indo_faults_lines.geojson"
    json_data = GempaController.fetch_json_data(url)
    return json_data

  #fault_indo_world.geojson
  @staticmethod
  def fault_indo_world():
    url = "https://bmkg-content-inatews.storage.googleapis.com/fault_indo_world.geojson"
    json_data = (url)
    return json_data

  @staticmethod
  def autogempa():
        url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml"
        try:
          response = requests.get(url)
          response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

          xml_data = response.content
          root = ET.fromstring(xml_data)

          # Extract relevant information from XML
          tanggal = root.findtext("gempa/Tanggal")
          jam = root.findtext("gempa/Jam")
          coordinates = root.findtext("gempa/point/coordinates")
          lintang = root.findtext("gempa/Lintang")
          bujur = root.findtext("gempa/Bujur")
          magnitude = root.findtext("gempa/Magnitude")
          kedalaman = root.findtext("gempa/Kedalaman")
          wilayah = root.findtext("gempa/Wilayah")
          potensi = root.findtext("gempa/Potensi")
          dirasakan = root.findtext("gempa/Dirasakan")
          shakemap = root.findtext("gempa/Shakemap")

          # Create a dictionary with the extracted information
          data_dict = {
              "Tanggal": tanggal,
              "Jam": jam,
              "Coordinates": coordinates,
              "Lintang": lintang,
              "Bujur": bujur,
              "Magnitude": magnitude,
              "Kedalaman": kedalaman,
              "Wilayah": wilayah,
              "Potensi": potensi,
              "Dirasakan": dirasakan,
              "Shakemap": shakemap
          }

          return data_dict

        except requests.exceptions.RequestException as e:
          # Handle HTTP request errors
          return {'error': f'Failed to fetch data. Error: {e}'}
        except ET.ParseError as e:
          # Handle XML parsing errors
          return {'error': f'Failed to parse XML. Error: {e}'}

  @staticmethod
  def gempaterkini():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.xml"
    response = requests.get(url)
    xml_data = response.content
    data_dict = xmltodict.parse(xml_data)
    return data_dict

  @staticmethod
  def gempadirasakan():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.xml"
    response = requests.get(url)
    xml_data = response.content
    data_dict = xmltodict.parse(xml_data)
    return data_dict

  # ASEAN EARTHQUAKE INFORMATION CENTER
  @staticmethod
  def aeicgempaQL():
    url = "https://bmkg-content-inatews.storage.googleapis.com/aeicgempaQL.json"
    json_data = GempaController.fetch_json_data(url)
    return json_data