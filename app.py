from flask import Flask, jsonify, Response
from Controller.GempaController import datagempa, last30event, last30feltevent, last30tsunamievent, live30event
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


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
