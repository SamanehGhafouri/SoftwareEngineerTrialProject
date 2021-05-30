from flask import Flask, request, render_template
from statistics import Statistics
from flask_cors import CORS

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


# class FlaskServer:
#
#     def __init__(self):
#         self.service = Flask(__name__)
#         # CORS(self.service, resources={"/*": {"origins": ["*"]}})
#         self.service.add_url_rule('/', view_func=self.home, methods=['GET'])
#         self.service.add_url_rule('/results', view_func=self.results, methods=['POST'])
#         self.service.add_url_rule('/results/<string:file_type>', view_func=self.results, methods=['POST'])
#         self.service.run(threaded=True, port=5000)
#
#     def home(self):
#         return render_template('home.html')
#
#     def results(self, file_type: str = None):
#
#         response = {}
#
#         if request.content_type is None or request.content_type.lower() != 'application/json':
#             response['ERROR'] = 'ERROR', f'Expecting "application/json" value for Content-Type header'
#             return response, 400
#
#         file_types = ['txt', 'json', 'xml']
#         if file_type is not None and file_type.lower() not in file_types:
#             response['ERROR'] = f"Unrecognized file type. Only accepting {', '.join(file_types)}"
#             return response, 400
#         else:
#             if file_type is None:
#                 # assign default file type of json.
#                 file_type = "json"
#             try:
#                 stats = Statistics(request.json, file_type)
#                 return stats.formatted_response()
#             except KeyError as e:
#                 response['ERROR'] = f"JSON Key ERROR Detected {e.args}"
#                 return response, 400


if __name__ == '__main__':
    # server = FlaskServer()
    app.run(threaded=True, port=5000)

