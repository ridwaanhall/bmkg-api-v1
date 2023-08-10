from flask import jsonify, request
#from replit import db
from datetime import datetime


class ErrorController:

  @staticmethod
  def unavailable(path):
    requester_ip = request.remote_addr
    now = datetime.now()
    response = {
      "message": f"The requested route '{path}' is unavailable.",
      "ip": requester_ip,
      "datetimeUTC": now.strftime('%Y-%m-%d %H:%M:%S')
    }

    #db["IP_address"] = requester_ip
    #db["path"]       = path
    #db["datetime"]   = now.strftime('%Y-%m-%d %H:%M:%S')

    #stored_data = {}
    #for key in db.keys():
    #   stored_data[key] = db[key]

    #print("Stored Data:", stored_data)

    return jsonify(response), 404
