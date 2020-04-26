import pytest
from random import randint

@pytest.fixture()
def random_num():
    num = randint(1, 100)
    return num


@pytest.fixture()
def return_list():
    lst = [int(randint(1,100)) for i in range(10)]
    return lst


@pytest.fixture()
def return_set():
    data_set = set('hello')
    return data_set


@pytest.fixture()
def return_dict():
    data_dict = {'банан': 1, 'яблоко': 2, 'апельсин': 3, 'груша': 4}
    return data_dict


@pytest.fixture()
def return_string():
    data_string = 'mississippi'
    return data_string


@pytest.fixture(params=[14,28,34,51])
def fixture_witch_params_num(request):
    return request.param


@pytest.fixture(params=['банан', 'яблоко', 'апельсин', 'груша'])
def fixture_witch_params_word(request):
    return request.param