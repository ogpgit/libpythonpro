from unittest.mock import Mock

import pytest

from libpythonpro import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('ogpgit')
    assert avatar_url == url


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/67315703?v=4'
    resp_mock.json.return_value = {
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


# teste de integração realizando a chamada na rede (internet)
def test_buscar_avatar_integracao():
    # print('get originallll integracao')
    # print(github_api.requests.get)
    url = github_api.buscar_avatar('ogpgit')
    assert 'https://avatars1.githubusercontent.com/u/67315703?v=4' == url
