from flask import Flask, jsonify, Response
from Controller.GempaController import datagempa, last30event, last30feltevent, last30tsunamievent, live30event, EmgempaQL, katalog_gempa, sensor_seismic, sensor_global, build_xml, histori, indo_faults_lines, convert_to_xml, fault_indo_world, load_geojson, process_gempa_data, autogempa, gempaterkini, gempadirasakan
import xmltodict
from xml.etree import ElementTree as ET

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "hehehe"


# GEMPA TERBARU (from json to xml)
@app.route('/new.xml')
def datagempa_xml():
  data = datagempa()
  if data:
    # Wrap the data in a root element named "root"
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


@app.route('/new.json')
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


# GEMPA DARI ZAMAN DAHULU
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


# GEMPA LEBIH DARI SAMADENGAN 5 MAG (from xml to xml) 30 LIST
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


# GEMPA YANG DIRASAKAN. 30 LIST
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


# GEMPA YANG KEMUNGKINAN STUNAMI 30 LIST
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


# GEMPA REAL-TIME 30 LIST
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


# IMAGE OF GEMPA_NEWS
@app.route('/img_news.json', methods=['GET'])
def img_news_json():
  urls = process_gempa_data()
  if urls:
    return jsonify(urls)
  else:
    return "Failed to fetch data."


@app.route('/img_news.xml', methods=['GET'])
def img_news_xml():
  urls = process_gempa_data()
  if urls:
    xml_root = ET.Element('urls')
    for key, url in urls.items():
      url_elem = ET.SubElement(xml_root, 'url')
      key_elem = ET.SubElement(url_elem, 'key')
      key_elem.text = key
      url_elem.text = url

    xml_string = ET.tostring(xml_root, encoding='utf-8', method='xml')
    response = Response(xml_string, content_type='application/xml')
    return response
  else:
    return "Failed to fetch data."


# Gempabumi Terbaru
@app.route('/autogempa.xml')
def autogempa_xml():
  data = autogempa()
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


@app.route('/autogempa.json')
def autogempa_json():
  data = autogempa()
  return jsonify(data)


# Daftar 15 Gempabumi M 5.0+
@app.route('/gempaterkini.xml')
def gempaterkini_xml():
  data = gempaterkini()
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


@app.route('/gempaterkini.json')
def gempaterkini_json():
  data = gempaterkini()
  return jsonify(data)


# Daftar 15 Gempabumi Dirasakan
@app.route('/gempadirasakan.xml')
def gempadirasakan_xml():
  data = gempadirasakan()
  response = Response(xmltodict.unparse(data, pretty=True),
                      content_type='application/xml')
  return response


@app.route('/gempadirasakan.json')
def gempadirasakan_json():
  data = gempadirasakan()
  return jsonify(data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
