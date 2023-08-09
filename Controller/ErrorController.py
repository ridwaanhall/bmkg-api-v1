from flask import jsonify, request


class ErrorController:

  @staticmethod
  def unavailable(path):
    requester_ip = request.remote_addr
    response = {
      "message": f"The requested route '{path}' is unavailable.",
      "ip": requester_ip
    }
    return jsonify(response), 404