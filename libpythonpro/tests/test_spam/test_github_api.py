from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'avatar_url': 'https://avatars1.githubusercontent.com/u/67315703?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('ogpgit')
    assert 'https://avatars1.githubusercontent.com/u/67315703?v=4' == url
