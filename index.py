#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')

# Endpoint for the API '/api/callhome', receives a POST request with a JSON body and save it to the database
# @app.route('/api/callhome', methods=['POST'])
# def callhome():
#     if request.method == 'POST':
#         print(request.json)
#         return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
