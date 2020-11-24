from unittest.mock import Mock

import pytest

from libpythonpro import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('ogpgit')
    assert avatar_url == url


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/67315703?v=4'
    resp_mock.json.return_value = {
        'avatar_url': url
    }
    get_original = github_api.requests.get
    # print('get originallll')
    # print(get_original)
    github_api.requests.get = Mock(return_value=resp_mock)
    # print('get Mockkkkkk')
    # print(github_api.requests.get)
    yield url
    github_api.requests.get = get_original


# teste de integração realizando a chamada na rede (internet)
def test_buscar_avatar_integracao():
    # print('get originallll integracao')
    # print(github_api.requests.get)
    url = github_api.buscar_avatar('ogpgit')
    assert 'https://avatars1.githubusercontent.com/u/67315703?v=4' == url


# if __name__ == '__main__':
    # test_buscar_avatar()
    # test_buscar_avatar_integracao()
