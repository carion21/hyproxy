# main.py
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import time
import os

load_dotenv()

app = Flask(__name__)


@app.route('/hello')
def index():
    return 'Hello, World!'


# @app.route('/proxy', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def proxy():
#     path = request.args.get('path')
#     url = f'{os.getenv("HOST")}{path}'

#     print(f'path: {path}')
#     print(f'url: {url}')

#     start = time.time()

#     response = requests.request(
#         method=request.method,
#         url=url,
#         headers={key: value for key,
#                  value in request.headers if key != 'Host'},
#         data=request.get_data(),
#         cookies=request.cookies,
#         allow_redirects=False)

#     end = time.time()

#     print(f'{url} - {response.status_code} - {end-start} seconds')

#     return (response.content, response.status_code, response.headers.items())

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def catch_all(path):
    print('='*50)
    query_string = request.query_string.decode('utf-8')
    complete_path = f'{path}?{query_string}' if query_string else path
    url = f'{os.getenv("HOST")}/{complete_path}'

    print(f'complete_path: {complete_path}')
    print('-'*50)
    # print(f'n===url: {url}')

    start = time.time()

    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for key,
                 value in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    end = time.time()

    print(f'{url} - {response.status_code} - {end-start} seconds')

    return (response.content, response.status_code, response.headers.items())


if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    app.run(host='0.0.0.0', port=port, debug=True)
