# Back-End

Expose a REST API endpoint that takes random user JSON data and a file format as input, and returns a file containing the statistics.
This project was generated with Flask 2.0.1, Python 3.9.4, Werkzeug 2.0.1
Flask supports python 3.6 and newer.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask, gunicorn, flask-cors, and json2xml.

```bash
pip install Flask
```
Gunicorn is Python WSGI HTTP server for UNIX.
```bash
pip install gunicorn
```
Flask-CORS is handling cross-origin resource sharing(CORS). This package exposes a Flask extension which by default enables CORS support on all routes, for all origins and methods. It allows parameterization of all CORS headers on a per-resource level. The package also contains a decorator, for those who prefer this approach.
```bash
pip install -U flask-cors
```
Get the xml from a json string data
```bash
pip install json2xml
```
## Deployment
This project deployed on heroku at: https://statistics-sam.herokuapp.com

## How to use this API
Brief documentation can be found at: https://statistics-sam.herokuapp.com. You can try this API using POST request at Postman:
* Paste the link into Postman and use POST method.
* Specify the file type at the Endpoint.
* Available file-types: xml, json, txt
* Example: https://statistics-sam.herokuapp.com/results/xml
* Set Headers: KEY: Content-Type, VALUE: application/json
* Paste a proper json inside Body from https://randomuser.me/api/
* Hit Send
* You should be able to see the statistics based on file-type you requested.

## Testing
Provided Unittests on functionality of statistics can be found at test_statistics.py
These tests are using following json files as inputs:
* first_json_data.json
* seccond_json_data.json
* third_json_data.json
* forth_json_data.json
* last_json_data.json


