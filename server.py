from flask import Flask, jsonify

from Controller.GempaController import GempaController
from Controller.HomeController import HomeController
from Controller.ImageController import ImageController
from Controller.ErrorController import ErrorController

app = Flask(__name__)


# home xml
@app.route("/")
def xml_home():
  return HomeController.load_home_xml()


# home json
@app.route("/json")
def json_home():
  data = HomeController.load_home_json()
  return jsonify(data)


# GEMPA TERBARU (from json to xml)
@app.route('/new.xml')
def datagempa_xml():
  data = GempaController.datagempa()
  return GempaController.xml_root_response(data)


@app.route('/new.json')
def datagempa_json():
  data = GempaController.datagempa()
  return GempaController.json_if(data)


# 200 GEMPA LEBIH 3 MAG
@app.route('/EmgempaQL.xml')
def EmgempaQL_xml():
  data = GempaController.EmgempaQL()
  return GempaController.xml_root_response(data)


@app.route('/EmgempaQL.json')
def EmgempaQL_json():
  data = GempaController.EmgempaQL()
  return GempaController.json_if(data)


# GEMPA DARI ZAMAN DAHULU
@app.route('/katalog_gempa.xml')
def katalog_gempa_xml():
  data = GempaController.katalog_gempa()
  return GempaController.xml_root_response(data)


@app.route('/katalog_gempa.json')
def katalog_gempa_json():
  data = GempaController.katalog_gempa()
  return GempaController.json_if(data)


# GEMPA LEBIH DARI SAMADENGAN 5 MAG (from xml to xml) 30 LIST
@app.route('/m5.xml')
@app.route('/last30event.xml')
def last30event_xml():
  data = GempaController.last30event()
  return GempaController.xml_response(data)


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
  return GempaController.xml_response(data)


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
  return GempaController.xml_response(data)


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
  return GempaController.xml_response(data)


@app.route('/realtime.json')
@app.route('/live30event.json')
def live30event_json():
  data = GempaController.live30event()
  return jsonify(data)


# SENSOR SEISMIC
@app.route('/sensor_seismic.xml')
def sensor_seismic_xml():
  data = GempaController.sensor_seismic()
  return GempaController.xml_root_response(data)


@app.route('/sensor_seismic.json')
def sensor_seismic_json():
  data = GempaController.sensor_seismic()
  return GempaController.json_if(data)


# SENSOR GLOBAL
@app.route('/sensor_global.xml')
def sensor_global_xml():
  data = GempaController.sensor_global()
  return GempaController.sensor_global_build_xml(data)


@app.route('/sensor_global.json')
def sensor_global_json():
  data = GempaController.sensor_global()
  return GempaController.json_if(data)


# HISTORI
@app.route('/histori.xml')
def histori_xml():
  data = GempaController.histori()
  return GempaController.xml_root_response(data)


@app.route('/histori.json')
def histori_json():
  data = GempaController.histori()
  return GempaController.json_if(data)


# INDO FAULTS LINES
@app.route('/indo_faults_lines.xml')
def indo_faults_lines_xml():
  data = GempaController.indo_faults_lines()
  return GempaController.faults_xml(data)


@app.route('/indo_faults_lines.json')
def indo_faults_lines_json():
  data = GempaController.indo_faults_lines()
  return GempaController.json_if(data)


@app.route('/indo_faults_lines.geojson')
def indo_faults_lines_geojson():
  geojson_data = GempaController.load_geojson()
  return GempaController.faults_geojson(geojson_data)


# FAULT INDO WORLD
@app.route('/fault_indo_world.xml')
def fault_indo_world_xml():
  data = GempaController.fault_indo_world()
  return GempaController.faults_xml(data)


@app.route('/fault_indo_world.json')
def fault_indo_world_json():
  data = GempaController.fault_indo_world()
  return GempaController.json_if(data)


@app.route('/fault_indo_world.geojson')
def fault_indo_world_geojson():
  geojson_data = GempaController.load_geojson()
  return GempaController.faults_geojson(geojson_data)


# Gempabumi Terbaru
@app.route('/autogempa.xml')
def autogempa_xml():
  data = GempaController.autogempa()
  return GempaController.xml_response(data)


@app.route('/autogempa.json')
def autogempa_json():
  data = GempaController.autogempa()
  return jsonify(data)


# Daftar 15 Gempabumi M 5.0+
@app.route('/gempaterkini.xml')
def gempaterkini_xml():
  data = GempaController.gempaterkini()
  return GempaController.xml_response(data)


@app.route('/gempaterkini.json')
def gempaterkini_json():
  data = GempaController.gempaterkini()
  return jsonify(data)


# Daftar 15 Gempabumi Dirasakan
@app.route('/gempadirasakan.xml')
def gempadirasakan_xml():
  data = GempaController.gempadirasakan()
  return GempaController.xml_response(data)


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


# if requests is unavailable
# Catch-all route for unavailable routes
@app.route("/<path:path>")
def handle_unavailable_route(path):
  return ErrorController.unavailable(path)