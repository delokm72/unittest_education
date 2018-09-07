import unittest
import requests
import re
import responses
import json
import logging
import sys


if __name__ == '__main__':
    log = logging.getLogger()
    log.level = logging.DEBUG
    log.addHandler(logging.StreamHandler(sys.stderr))
else:
    log = logging.getLogger(__name__)
    log.info('PASS')
    log.debug('Something about %r in %s', log, __name__)
    url = 'https://jsonplaceholder.typicode.com/'
    url_post = 'https://jsonplaceholder.typicode.com/posts'
    url_delete = 'https://jsonplaceholder.typicode.com/posts/1'


class JsonPlaceholderTests(unittest.TestCase):
    def test_request_get(self):
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')

    def test_request_post(self):
        response = requests.post(url_post, data={'title': 'foo', 'body': 'bar', 'userId': '1'})
        self.assertEqual(response.status_code, 201)
        logging.info('[PASS]')

    def test_request_delete(self):
        response = requests.delete(url_delete)
        self.assertEqual(response.status_code, 200)
        logging.info('[PASS]')


if __name__ == '__main__':
    unittest.main()