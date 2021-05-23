from flask import url_for
from flask_testing import TestCase
from requests.api import request
from app import app
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG=True)
        return app

class TestHome(TestBase):
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get(
                "http://palette-generator:5001/palette", 
                json={"palette":[[255,0,0],[0,255,0],[0,0,255]]}
            )
            m.get(
                "http://name-generator:5002/name",
                json={"name":["Testing,","Testing,","123"]}
            )
            response = self.client.post(url_for("get_palette"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Testing, Testing, 123', response.data)
            self.assertIn(b'background:rgb(255, 0, 0)', response.data)
            self.assertIn(b'background:rgb(0, 255, 0)', response.data)
            self.assertIn(b'background:rgb(0, 0, 255)', response.data)

