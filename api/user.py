from http.server import BaseHTTPRequestHandler
from os.path import join
from pymongo import MongoClient

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print('TEST 1234567')
        return
