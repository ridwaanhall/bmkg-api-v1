from flask import Flask, jsonify, Response
from Controller.GempaController import GempaNews, last30event, last30feltevent, last30tsunamievent, live30event
import json, xmltodict

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "hehehe"


# Route to get earthquake data as XML
@app.route('/gempa-terkini.xml')
@app.route('/datagempa.xml')
def datagempa_xml():
  data = GempaNews()
  if data:
    # Wrap the data in a root element named "root"
    wrapped_data = {"root": data}
    xml_data = xmltodict.unparse(wrapped_data, pretty=True)
    return Response(xml_data, content_type='text/xml')
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# Route to get earthquake data as JSON
@app.route('/gempa-terkini.json')
@app.route('/datagempa.json')
def datagempa_json():
  data = GempaNews()
  if data:
    return jsonify(data)
  else:
    return jsonify({"message": "Failed to fetch data."}), 500


# gempa yang lebih dari 5 Magnitudo
@app.route('/m5')
@app.route('/last30event')
def show_last30event():
  data = last30event()
  return jsonify(data)


# gempa yang dirasakan
@app.route('/felt.xml')
@app.route('/last30feltevent.xml')
def show_last30feltevent():
  data = last30feltevent()
  response = Response(data, content_type='application/xml')
  return response


@app.route('/tsunami')
@app.route('/last30tsunamievent')
def show_last30tsunamievent():
  data = last30tsunamievent()
  # Create a Response object with the XML content and set the content-type header
  response = Response(data, content_type='application/xml')
  return response


@app.route('/realtime')
@app.route('/live30event')
def show_live30event():
  data = live30event()
  # Create a Response object with the XML content and set the content-type header
  response = Response(data, content_type='application/xml')
  return response


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
