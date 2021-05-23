from flask import Flask
from statistics import Statistics


class FlaskServer:

    def __init__(self):
        self.service = Flask(__name__)
        self.service.add_url_rule('/', view_func=self.home)
        self.service.add_url_rule('/results', view_func=self.results)
        self.service.run()

    def home(self):
        return "HOME"

    def results(self):
        data = {"name": "Samaneh"}
        stats = Statistics(data, "json")
        return stats.formatted_response()


if __name__ == '__main__':
    server = FlaskServer()

