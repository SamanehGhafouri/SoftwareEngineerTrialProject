import json

from flask import Flask, request
from statistics import Statistics
from flask_cors import CORS


class FlaskServer:

    def __init__(self):
        self.service = Flask(__name__)
        CORS(self.service, resources={"/*": {"origins": ["*"]}})
        self.service.add_url_rule('/', view_func=self.home)
        self.service.add_url_rule('/results', view_func=self.results, methods=['POST', 'GET'])
        self.service.run()

    def home(self):
        return "HOME"

    def results(self):
        print(request.headers)
        print(request.data)
        json_data = json.loads(request.data)
        stats = Statistics(json_data, "json")
        return stats.formatted_response()


if __name__ == '__main__':
    server = FlaskServer()
