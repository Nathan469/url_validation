import io
import main
import pytest

def test_read_input_ok(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a\nb\nc\nd\n'))
    assert main.read_input() == ['a', 'b', 'c', 'd']