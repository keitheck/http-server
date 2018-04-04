import requests
import json

"""test do_GET()"""


def test_server_sends_200_response():
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200


def test_server_sends_get():
    response = requests.get('http://127.0.0.1:3000/cow')
    assert response.status_code == 400


def test_server_sends_get2():
    response = requests.get('http://127.0.0.1:3000/cow?msg=hello')
    assert response.status_code == 200


def test_404():
    response = requests.get('http://127.0.0.1:3000/cat')
    assert response.status_code == 404


def test_post_1():
    """test do_POST()"""
    response = requests.post('http://127.0.0.1:3000/cow', data=json.dumps({'msg':'sdfghjkjhgfdf'}))
    assert response.status_code == 200
    assert response.text == '{"content": " _______________ \n< sdfghjkjhgfdf >\n --------------- \n  o\n   o   \\_\\_    _/_/\n    o      \\__/\n           (oo)\\_______\n           (__)\\       )\\/\\\n               ||----w |\n               ||     ||"}'

