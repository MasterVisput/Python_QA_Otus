import pytest
import requests

def test_status_code_that_url(url,status_code):
    res = requests.get(url)
    assert res.status_code == int(status_code), f'Сервис вернул код {res.status_code}'
    print(res.status_code)
