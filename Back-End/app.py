from flask import Flask, request, render_template
from statistics import Statistics
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": ["*"]}})


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
@app.route('/results/<string:file_type>', methods=['POST'])
def results(file_type: str = None):
    response = {}

    if request.content_type is None or request.content_type.lower() != 'application/json':
        response['ERROR'] = 'ERROR', f'Expecting "application/json" value for Content-Type header'
        return response, 400

    file_types = ['txt', 'json', 'xml']
    if file_type is not None and file_type.lower() not in file_types:
        response['ERROR'] = f"Unrecognized file type. Only accepting {', '.join(file_types)}"
        return response, 400
    else:
        if file_type is None:
            # assign default file type of json.
            file_type = "json"
        try:
            stats = Statistics(request.json, file_type)
            return stats.formatted_response()
        except KeyError as e:
            response['ERROR'] = f"JSON Key ERROR Detected {e.args}"
            return response, 400


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
