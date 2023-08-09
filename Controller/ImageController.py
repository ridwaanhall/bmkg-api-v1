import requests
from flask import Response


class ImageController:

  @staticmethod
  def get_eventid(json_data):
    return json_data.get("info", {}).get("eventid")

  @staticmethod
  def intensity_logo_route(eventid):
    json_url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
    response = requests.get(json_url)

    if response.status_code == 200:
      json_data = response.json()
      event_id = ImageController.get_eventid(json_data)

      if event_id == eventid:
        image_data = ImageController.intensity_logo(eventid)
        if image_data:
          return Response(image_data, content_type='image/jpeg')
        else:
          return "Image not found", 404
      else:
        return "Event ID mismatch", 400
    else:
      return "Failed to fetch JSON data", 500

  @staticmethod
  def impact_list_route(eventid):
    json_url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
    response = requests.get(json_url)

    if response.status_code == 200:
      json_data = response.json()
      event_id = ImageController.get_eventid(json_data)

      if event_id == eventid:
        image_data = ImageController.impact_list(eventid)
        if image_data:
          return Response(image_data, content_type='image/jpeg')
        else:
          return "Image not found", 404
      else:
        return "Event ID mismatch", 400
    else:
      return "Failed to fetch JSON data", 500

  @staticmethod
  def stationlist_mmi_route(eventid):
    json_url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
    response = requests.get(json_url)

    if response.status_code == 200:
      json_data = response.json()
      event_id = ImageController.get_eventid(json_data)

      if event_id == eventid:
        image_data = ImageController.stationlist_mmi(eventid)
        if image_data:
          return Response(image_data, content_type='image/jpeg')
        else:
          return "Image not found", 404
      else:
        return "Event ID mismatch", 400
    else:
      return "Failed to fetch JSON data", 500

  @staticmethod
  def mmi_route(eventid):
    json_url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
    response = requests.get(json_url)

    if response.status_code == 200:
      json_data = response.json()
      event_id = ImageController.get_eventid(json_data)

      if event_id == eventid:
        image_data = ImageController.mmi(eventid)
        if image_data:
          return Response(image_data, content_type='image/jpeg')
        else:
          return "Image not found", 404
      else:
        return "Event ID mismatch", 400
    else:
      return "Failed to fetch JSON data", 500

  @staticmethod
  def loc_map_route(eventid):
    json_url = "https://bmkg-content-inatews.storage.googleapis.com/datagempa.json"
    response = requests.get(json_url)

    if response.status_code == 200:
      json_data = response.json()
      event_id = ImageController.get_eventid(json_data)

      if event_id == eventid:
        image_data = ImageController.loc_map(eventid)
        if image_data:
          return Response(image_data, content_type='image/png')
        else:
          return "Image not found", 404
      else:
        return "Event ID mismatch", 400
    else:
      return "Failed to fetch JSON data", 500

  @staticmethod
  def intensity_logo(eventid):
    url = f"https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/intensity_logo.jpg"
    response = requests.get(url)
    if response.status_code == 200:
      return response.content
    else:
      return None

  @staticmethod
  def impact_list(eventid):
    url = f"https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/impact_list.jpg"
    response = requests.get(url)
    if response.status_code == 200:
      return response.content
    else:
      return None

  @staticmethod
  def stationlist_mmi(eventid):
    url = f"https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/stationlist_MMI.jpg"
    response = requests.get(url)
    if response.status_code == 200:
      return response.content
    else:
      return None

  @staticmethod
  def loc_map(eventid):
    url = f"https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/loc_map.png"
    response = requests.get(url)
    if response.status_code == 200:
      return response.content
    else:
      return None

  @staticmethod
  def mmi(eventid):
    url = f"https://data.bmkg.go.id/DataMKG/TEWS/{eventid}.mmi.jpg"
    response = requests.get(url)
    if response.status_code == 200:
      return response.content
    else:
      return None