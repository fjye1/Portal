import requests
from flask import Blueprint, Response

proxy_bp = Blueprint("proxy", __name__)

@proxy_bp.route("/event-builder/<path:path>")
def event_builder_proxy(path):
    url = f"http://event-builder:5001/{path}"
    resp = requests.get(url)
    return Response(resp.content, resp.status_code)