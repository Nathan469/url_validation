import io
import json
import main
import pytest
import requests

def test_read_input_ok(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a\nb\nc\nd\n'))
    assert main.read_input() == ['a', 'b', 'c', 'd']

def test_is_valid_url_happycase_returns_true():
    assert main.is_valid_url("https://www.google.com/")

def test_is_valid_url_invalid_returns_false():
    assert not main.is_valid_url("httpxs://www.google.com/")   

def test_is_valid_url_parameters_returns_true():
    assert main.is_valid_url("https://www.example.com/?bedroom=birthday&bit=airplane")    

def test_is_valid_url_anchors_returns_true():
    assert main.is_valid_url("http://www.example.com/basket/birthday#border")  

def test_main_happycase_ok(monkeypatch, capsys):

    def mock_requests(url, timeout):
        if url == 'https://golang.org/':
            response = requests.models.Response()
            response.status_code = 200
            response.headers = {
                    'Date': 'Fri, 12 Feb 2021 18:11:35 GMT',
                    'Content-Type': 'text/html; charset=utf-8',
                    'Vary': 'Accept-Encoding',
                    "Content-Length": "61",
                    'Transfer-Encoding': 'chunked'}
            return response
        
    monkeypatch.setattr('sys.stdin', io.StringIO('https://golang.org/\n'))
    monkeypatch.setattr('requests.get', mock_requests)
    main.main()
    captured = capsys.readouterr()
    assert json.loads(captured.out) == json.loads(
"""{
    "Status_code": 200,
    "Url": "https://golang.org/",
    "Content_length": "61",
    "Date": "Fri, 12 Feb 2021 18:11:35 GMT"}""")


def test_main_invalid_address_outputs_to_stderr(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO('bad://address/\n'))
    main.main()
    captured = capsys.readouterr()
    assert json.loads(captured.err) == json.loads(
"""{
    "Url": "bad://address/",
    "Error": "invalid url"}""")


def test_main_timeout_prints_to_stderr(monkeypatch, capsys):

    def mock_requests(url, timeout):
        if url == 'https://golang.org/':
            raise requests.exceptions.Timeout()
        
    monkeypatch.setattr('sys.stdin', io.StringIO('https://golang.org/\n'))
    monkeypatch.setattr('requests.get', mock_requests)
    main.main()
    captured = capsys.readouterr()
    assert json.loads(captured.err) == json.loads(
"""{
    "Url": "https://golang.org/",
    "Error": "RequestException"}""")