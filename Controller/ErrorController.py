from flask import jsonify, request
from replit import db
from datetime import datetime


class ErrorController:

  @staticmethod
  def unavailable(path):
    requester_ip = request.remote_addr
    now = datetime.now()
    response = {
      "message": f"The requested route '{path}' is unavailable.",
      "ip": requester_ip,
      "datetime": now
    }
    del db["IP_address"]
    del db["path"]
    del db["datetime"]

    keys = db.keys

    for key in keys:
      print(f"""{key} : {db["key"]}""")
    return jsonify(response), 404
