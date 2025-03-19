import requests
import argparse
from random import randint as rnd

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Host URL')
parser.add_argument('--count', help='count runs', default=1)

args = parser.parse_args()

host = args.host


def send_requests():
    print('start sending')
    # command injection
    requests.get(f'{host}/ping?host=1.1.1.1')
    # # csrf
    requests.get(f'{host}/transfer_form')
    # # file inclusion
    requests.get(f'{host}/page/%3Chtml%3E123%3C%2Fhtml%3E')
    # file upload
    files = [('file', ('file', open('file_for_test', 'rb'), 'application/octet-stream'))]
    requests.post(f'{host}/upload_file', files=files)
    # sql injection
    requests.post(f'{host}/items', json={"name": f"test_{rnd(1, 9999999):07d}", "description": "description"})
    # # xss
    requests.get(f'{host}/search?query=1')
    # open redirect
    requests.get(f'{host}/open_redirect?redirect_to=https://wallarm.com')
    print('sent')


for _ in range(int(args.count)):
    send_requests()
