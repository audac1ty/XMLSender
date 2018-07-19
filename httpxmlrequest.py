import sys
import http
import requests

def main():
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <a>6</a>"""
    headers = {'Content-Type':'application/xml', 'X-Request-ID':'1YQ4XR08WV'}
    requests.post('http://172.17.20.46:1026/?sdcApplicationId=1YQ4XR08WV', data=xml, headers=headers).text
if __name__ == '__main__':
    main()