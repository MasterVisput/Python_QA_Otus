import pytest
from random import randint
from api_tests.api.dogs_api_client import DogsApiClient
from api_tests.api.brewery_api_client import BreweryApiClient



@pytest.fixture(scope='session')
def client_dogs():
    client_dogs = DogsApiClient(host='https://dog.ceo/api',
                                num=randint(1, 50)
                                )
    return client_dogs


@pytest.fixture(params=['affenpinscher', 'african', 'dalmatian', 'groenendael'])
def client_with_params(request):
    client_with_params = DogsApiClient(host='https://dog.ceo/api',
                                       breed=request.param
                                       )
    return client_with_params


@pytest.fixture(params=['australian', 'buhund', 'bulldog', 'bullterrier', 'cattledog', 'collie', 'corgi', 'hound'])
def client_with_params_sub_breeds(request):
    client_with_params_sub_breeds = DogsApiClient(host='https://dog.ceo/api',
                                                  sub_breed=request.param
                                                  )
    return client_with_params_sub_breeds


@pytest.fixture(scope='session')
def client_brewery():
    client_brewery = BreweryApiClient(host='https://api.openbrewerydb.org')
    return client_brewery



