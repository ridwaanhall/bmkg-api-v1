# ImageController.py
from flask import send_file
import requests
from io import BytesIO


def construct_urls(event_id):
  urls = {
    'intensity_logo':
    f"https://bmkg-content-inatews.storage.googleapis.com/{event_id}_rev/intensity_logo.jpg",
    'loc_map':
    f"https://bmkg-content-inatews.storage.googleapis.com/{event_id}_rev/loc_map.png",
    'impact_list':
    f"https://bmkg-content-inatews.storage.googleapis.com/{event_id}_rev/impact_list.jpg",
    'stationlist_MMI':
    f"https://bmkg-content-inatews.storage.googleapis.com/{event_id}_rev/stationlist_MMI.jpg",
    f'{event_id}': f"https://data.bmkg.go.id/DataMKG/TEWS/{event_id}.mmi.jpg"
  }

  return urls


def fetch_json_data(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None


def serve_image():
  image_url = 'https://bmkg-content-inatews.storage.googleapis.com/20230809025718_rev/intensity_logo.jpg'

  response = requests.get(image_url)
  if response.status_code == 200:
    image_data = BytesIO(
      response.content)  # Convert bytes to a file-like object
    return send_file(image_data, mimetype='image/jpeg')
  else:
    return "Image not found", 404


# get eventid to show img
def process_gempa_data():
  url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
  json_data = fetch_json_data(url)
  # get eventid
  if json_data:
    event_id = json_data['info']['eventid']
    urls = construct_urls(event_id)
    return urls
  else:
    return None