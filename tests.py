import io
import main
import pytest

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