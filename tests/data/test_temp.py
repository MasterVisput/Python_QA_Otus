import pytest
def pytest_generate_tests(metafunc):
    if 'fixture1' in metafunc.fixturenames:
        metafunc.parametrize('fixture1', [1,2,3,4,5])
    if 'fixture2' in metafunc.fixturenames:
        metafunc.parametrize('fixture2', [6,7,8,9,0])


def test_parm(fixture1, fixture2):
    assert fixture1 + fixture2 > 0