import json

import requests
from flask import Response
from flask_restful import abort
from requests.exceptions import ConnectionError

from rubix_http.method import HttpMethod

PORT: int = 1616


def gw_request(api: str, body: json = None, http_method: HttpMethod = HttpMethod.GET):
    actual_url: str = f'http://0.0.0.0:{PORT}/{api.strip("/")}'
    return __gw_http_request(actual_url, body, http_method)


def gw_mqtt_slave_request(slave_global_uuid: str, api: str, body: json = None,
                          http_method: HttpMethod = HttpMethod.GET):
    actual_url: str = f'http://0.0.0.0:{PORT}/slave/{slave_global_uuid}/{api.strip("/")}'
    return __gw_http_request(actual_url, body, http_method)


def gw_mqtt_slaves_multicast_request(api: str, body: json = None, http_method: HttpMethod = HttpMethod.GET):
    actual_url: str = f'http://0.0.0.0:{PORT}/slaves/multicast/{api.strip("/")}'
    return __gw_http_request(actual_url, body, http_method)


def gw_mqtt_slaves_broadcast_request(api: str, body: json = None, http_method: HttpMethod = HttpMethod.GET):
    actual_url: str = f'http://0.0.0.0:{PORT}/slaves/broadcast/{api.strip("/")}'
    return __gw_http_request(actual_url, body, http_method)


def gw_mqtt_master_request(api: str, body: json = None, http_method: HttpMethod = HttpMethod.GET):
    actual_url: str = f'http://0.0.0.0:{PORT}/master/{api.strip("/")}'
    return __gw_http_request(actual_url, body, http_method)


def __gw_http_request(url: str, body: json, http_method: HttpMethod):
    try:
        resp = requests.request(http_method.value, url, json=body)
        response = Response(resp.content, resp.status_code, resp.raw.headers.items())
        return response
    except ConnectionError:
        abort(404)
