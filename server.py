from flask import Flask, jsonify, Response
import xmltodict

from Controller.GempaController import GempaController
from Controller.HomeController import load_home_json
from Controller.ImageController import ImageController

app = Flask(__name__)


# xml_root_response
def xml_root_response(data):
  if data:
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# json_if
def json_if(data):
  if data:
    return jsonify(data)
  else:
    return jsonify({"mzessage": "Failed to fetch data."}), 500


# xml_response
def xml_response(data):
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


# faults_xml
def faults_xml(data):
  if data:
    xml_data = GempaController.convert_to_xml(data)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# faults_geojson
def faults_geojson(geojson_data):
  if geojson_data:
    return Response(geojson_data, content_type='application/json')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


def sensor_global_build_xml(data):
  if data:
    xml_data = GempaController.build_xml(data)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


#========================
# home
@app.route("/json")
def json_home():
  # Load JSON data using the function from HomeController
  data = load_home_json()
  # Convert the data to a JSON response
  return jsonify(data)


@app.route("/")
def xml_home():
  # Convert the JSON data to XML using xmltodict
  data = load_home_json()
  xml_data = xmltodict.unparse({"data": data}, pretty=True)
  # Return the XML response
  return Response(xml_data, content_type='text/xml')


# GEMPA TERBARU (from json to xml)
@app.route('/new.xml')
def datagempa_xml():
  data = GempaController.datagempa()
  return xml_root_response(data)


@app.route('/new.json')
def datagempa_json():
  data = GempaController.datagempa()
  return json_if(data)


# 200 GEMPA LEBIH 3 MAG
@app.route('/EmgempaQL.xml')
def EmgempaQL_xml():
  data = GempaController.EmgempaQL()
  return xml_root_response(data)


@app.route('/EmgempaQL.json')
def EmgempaQL_json():
  data = GempaController.EmgempaQL()
  return json_if(data)


# GEMPA DARI ZAMAN DAHULU
@app.route('/katalog_gempa.xml')
def katalog_gempa_xml():
  data = GempaController.katalog_gempa()
  return xml_root_response(data)


@app.route('/katalog_gempa.json')
def katalog_gempa_json():
  data = GempaController.katalog_gempa()
  return json_if(data)


# GEMPA LEBIH DARI SAMADENGAN 5 MAG (from xml to xml) 30 LIST
@app.route('/m5.xml')
@app.route('/last30event.xml')
def last30event_xml():
  data = GempaController.last30event()
  return xml_response(data)


@app.route('/m5.json')
@app.route('/last30event.json')
def last30event_json():
  data = GempaController.last30event()
  return jsonify(data)


# GEMPA YANG DIRASAKAN. 30 LIST
@app.route('/felt.xml')
@app.route('/last30feltevent.xml')
def last30feltevent_xml():
  data = GempaController.last30feltevent()
  return xml_response(data)


@app.route('/felt.json')
@app.route('/last30feltevent.json')
def last30feltevent_json():
  data = GempaController.last30feltevent()
  return jsonify(data)


# GEMPA YANG KEMUNGKINAN STUNAMI 30 LIST
@app.route('/tsunami.xml')
@app.route('/last30tsunamievent.xml')
def last30tsunamievent_xml():
  data = GempaController.last30tsunamievent()
  return xml_response(data)


@app.route('/tsunami.json')
@app.route('/last30tsunamievent.json')
def last30tsunamievent_json():
  data = GempaController.last30tsunamievent()
  return jsonify(data)


# GEMPA REAL-TIME 30 LIST
@app.route('/realtime.xml')
@app.route('/live30event.xml')
def live30event_xml():
  data = GempaController.live30event()
  return xml_response(data)


@app.route('/realtime.json')
@app.route('/live30event.json')
def live30event_json():
  data = GempaController.live30event()
  return jsonify(data)


# SENSOR SEISMIC
@app.route('/sensor_seismic.xml')
def sensor_seismic_xml():
  data = GempaController.sensor_seismic()
  return xml_root_response(data)


@app.route('/sensor_seismic.json')
def sensor_seismic_json():
  data = GempaController.sensor_seismic()
  return json_if(data)


# SENSOR GLOBAL
@app.route('/sensor_global.xml')
def sensor_global_xml():
  data = GempaController.sensor_global()
  return sensor_global_build_xml(data)


@app.route('/sensor_global.json')
def sensor_global_json():
  data = GempaController.sensor_global()
  return json_if(data)


# HISTORI
@app.route('/histori.xml')
def histori_xml():
  data = GempaController.histori()
  return xml_root_response(data)


@app.route('/histori.json')
def histori_json():
  data = GempaController.histori()
  return json_if(data)


# INDO FAULTS LINES
@app.route('/indo_faults_lines.xml')
def indo_faults_lines_xml():
  data = GempaController.indo_faults_lines()
  return faults_xml(data)


@app.route('/indo_faults_lines.json')
def indo_faults_lines_json():
  data = GempaController.indo_faults_lines()
  return json_if(data)


@app.route('/indo_faults_lines.geojson')
def indo_faults_lines_geojson():
  geojson_data = GempaController.load_geojson()
  return faults_geojson(geojson_data)


# FAULT INDO WORLD
@app.route('/fault_indo_world.xml')
def fault_indo_world_xml():
  data = GempaController.fault_indo_world()
  return faults_xml(data)


@app.route('/fault_indo_world.json')
def fault_indo_world_json():
  data = GempaController.fault_indo_world()
  return json_if(data)


@app.route('/fault_indo_world.geojson')
def fault_indo_world_geojson():
  geojson_data = GempaController.load_geojson()
  return faults_geojson(geojson_data)


# Gempabumi Terbaru
@app.route('/autogempa.xml')
def autogempa_xml():
  data = GempaController.autogempa()
  return xml_response(data)


@app.route('/autogempa.json')
def autogempa_json():
  data = GempaController.autogempa()
  return jsonify(data)


# Daftar 15 Gempabumi M 5.0+
@app.route('/gempaterkini.xml')
def gempaterkini_xml():
  data = GempaController.gempaterkini()
  return xml_response(data)


@app.route('/gempaterkini.json')
def gempaterkini_json():
  data = GempaController.gempaterkini()
  return jsonify(data)


# Daftar 15 Gempabumi Dirasakan
@app.route('/gempadirasakan.xml')
def gempadirasakan_xml():
  data = GempaController.gempadirasakan()
  return xml_response(data)


@app.route('/gempadirasakan.json')
def gempadirasakan_json():
  data = GempaController.gempadirasakan()
  return jsonify(data)


# IMAGE
# Define route to serve intensity logo images
@app.route('/<eventid>_rev/intensity_logo.jpg')
def serve_intensity_logo(eventid):
  return ImageController.intensity_logo_route(eventid)


# Define route to serve impact list images
@app.route('/<eventid>_rev/impact_list.jpg')
def serve_impact_list(eventid):
  return ImageController.impact_list_route(eventid)


# Define route to serve stationlist MMI images
@app.route('/<eventid>_rev/stationlist_MMI.jpg')
def serve_stationlist_mmi(eventid):
  return ImageController.stationlist_mmi_route(eventid)


# Define route to serve loc_map images (PNG)
@app.route('/<eventid>_rev/loc_map.png')
def serve_loc_map(eventid):
  return ImageController.loc_map_route(eventid)


# Define route to serve MMI images
@app.route('/<eventid>.mmi.jpg')
def mmi(eventid):
  return ImageController.mmi_route(eventid)
