from flask import Flask, jsonify, Response
from Controller.GempaController import datagempa, last30event, last30feltevent, last30tsunamievent, live30event, EmgempaQL, katalog_gempa, sensor_seismic, sensor_global, build_xml, histori, indo_faults_lines, convert_to_xml, fault_indo_world, load_geojson
import xmltodict

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "hehehe"


# GEMPA TERBARU (from json to xml)
@app.route('/gempa-terkini.xml')
@app.route('/datagempa.xml')
def datagempa_xml():
  data = datagempa()
  if data:
    # Wrap the data in a root element named "root"
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/gempa-terkini.json')
@app.route('/datagempa.json')
def datagempa_json():
  data = datagempa()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# 200 GEMPA LEBIH 3 MAG
@app.route('/EmgempaQL.xml')
def EmgempaQL_xml():
  data = EmgempaQL()
  if data:
    # Wrap the data in a root element named "root"
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/EmgempaQL.json')
def EmgempaQL_json():
  data = EmgempaQL()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# 200 GEMPA LEBIH 5 MAG
@app.route('/katalog_gempa.xml')
def katalog_gempa_xml():
  data = katalog_gempa()
  if data:
    # Wrap the data in a root element named "root"
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/katalog_gempa.json')
def katalog_gempa_json():
  data = katalog_gempa()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# GEMPA LEBIH DARI SAMADENGAN 5 MAG (from xml to xml)
@app.route('/m5.xml')
@app.route('/last30event.xml')
def last30event_xml():
  data = last30event()
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


@app.route('/m5.json')
@app.route('/last30event.json')
def last30event_json():
  data = last30event()
  return jsonify(data)


# GEMPA YANG DIRASAKAN
@app.route('/felt.xml')
@app.route('/last30feltevent.xml')
def last30feltevent_xml():
  data = last30feltevent()
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


@app.route('/felt.json')
@app.route('/last30feltevent.json')
def last30feltevent_json():
  data = last30feltevent()
  return jsonify(data)


# GEMPA YANG KEMUNGKINAN STUNAMI
@app.route('/tsunami.xml')
@app.route('/last30tsunamievent.xml')
def last30tsunamievent_xml():
  data = last30tsunamievent()
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


@app.route('/tsunami.json')
@app.route('/last30tsunamievent.json')
def last30tsunamievent_json():
  data = last30tsunamievent()
  return jsonify(data)


# GEMPA REAL-TIME
@app.route('/realtime.xml')
@app.route('/live30event.xml')
def live30event_xml():
  data = live30event()
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


@app.route('/realtime.json')
@app.route('/live30event.json')
def live30event_json():
  data = live30event()
  return jsonify(data)


# SENSOR SEISMIC
@app.route('/sensor_seismic.xml')
def sensor_seismic_xml():
  data = sensor_seismic()
  if data:
    # Wrap the data in a root element named "root"
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/sensor_seismic.json')
def sensor_seismic_json():
  data = sensor_seismic()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# SENSOR GLOBAL
@app.route('/sensor_global.xml')
def sensor_global_xml():
  data = sensor_global()
  if data:
    xml_data = build_xml(data)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/sensor_global.json')
def sensor_global_json():
  data = sensor_global()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# HISTORI
@app.route('/histori.xml')
def histori_xml():
  data = histori()
  if data:
    # Wrap the data in a root element named "root"
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/histori.json')
def histori_json():
  data = histori()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# INDO FAULTS LINES
@app.route('/indo_faults_lines.xml')
def indo_faults_lines_xml():
  data = indo_faults_lines()
  if data:
    xml_data = convert_to_xml(data)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/indo_faults_lines.json')
def indo_faults_lines_json():
  data = indo_faults_lines()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/indo_faults_lines.geojson')
def indo_faults_lines_geojson():
  geojson_data = load_geojson()
  if geojson_data:
    return Response(geojson_data, content_type='application/json')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# FAULT INDO WORLD
@app.route('/fault_indo_world.xml')
def fault_indo_world_xml():
  data = fault_indo_world()
  if data:
    xml_data = convert_to_xml(data)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/fault_indo_world.json')
def fault_indo_world_json():
  data = fault_indo_world()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/fault_indo_world.geojson')
def fault_indo_world_geojson():
  geojson_data = load_geojson()
  if geojson_data:
    return Response(geojson_data, content_type='application/json')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
