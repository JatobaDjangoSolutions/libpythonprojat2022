from unittest.mock import Mock

from libpythonprojat2022 import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'brjatoba92', 'id': 69490377,
                                   'avatar_url': 'https://avatars.githubusercontent.com/u/69490377?v=4',
                                   }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('brjatoba92')
    assert 'https://avatars.githubusercontent.com/u/69490377?v=4' == url
