import os
import datetime
import json
import logging

import requests
import exceptions

from config import __endpoint_map__


log = logging.getLogger(__name__)

class Api(object):

    def __init__(self, options=None, **kwargs):

        # get mode default to sandbox
        self.mode = kwargs.get("mode", "sandbox")
        
        if self.mode != "live" and self.mode != "sandbox":
            # TODO handle errors
            return

        self.merchant_id = kwargs['merchant_id']
        self.api_key = kwargs['merchant_api_key']
        
        
        
    def default_endpoint(self):
        return __endpoint_map__.get(self.mode)


    def http_call(self, method, url, **kwargs):
        if self.mode.lower() != 'live':
            request_headers = kwargs.get("headers", {})
            request_body = kwargs.get("data", {})
            log.debug("Level: " + self.mode)
            log.debug('Request: \nHeaders: %s\nBody: %s' % (
                str(request_headers), str(request_body)))

        else:
            log.info(
                'Not logging full request/response headers and body in live mode for compliance')

        kwargs['data']['merchant-id'] = self.merchant_id
        kwargs['data']['api-key'] = self.api_key

        start_time = datetime.datetime.now()
        response = requests.request(method, url, **kwargs)
        duration = datetime.datetime.now() - start_time

        log.info('Response[%d]: %s, Duration: %s.%ss.' % (
            response.status_code, response.reason, duration.seconds, duration.microseconds))

        return self.handle_response(response, response.content.decode('utf-8'))


    def post(self, uri='/', **kwargs):
        '''Make POST request
            Usage::
                 >>> api.post("/submit.php", data={}, headers={})
        '''
        return self.http_call('POST', self.default_endpoint() + uri, **kwargs)

    def handle_response(self, response, content):
        ''' Expresspay shit status system handle here. And return a json response '''
        # status = content['status']
        if response.status_code == 404:
            raise exceptions.ConnectionError(response, content) 
        return json.loads(content) if content else {}


def set_config(options=None, **config):
    __api__ = Api(options or {}, **config)

    return __api__


def default():
    ''' create a default api client '''
    try:
        merchant_id = os.environ['EXPRESSPAY_MERCHANT_ID']
        merchant_api_key =os.environ['EXPRESSPAY_MERCHANT_API_KEY']

    except KeyError:
        raise Exception("Required EXPRESSPAY_MERCHANT_ID and EXPRESSPAY_MERCHANT_API_KEY.")

    __api__ = Api(mode=os.environ.get(
            "EXPRESSPAY_MODE", "sandbox"), merchant_id=merchant_id, merchant_api_key=merchant_api_key)

    
    return __api__

configure = set_config
