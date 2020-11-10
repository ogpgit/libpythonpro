import requests


def buscar_avatar(usuario):
    """
    Buscar o avatar de um usuário no Github

    :param usuario: str com o nome do usuário no github
    :return: str com o link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'

    resp = requests.get(url)
    # print(resp)
    # print(resp.cookies)
    # print(resp.json())
    # r = resp.json()
    # print(r)
    # print(r['avatar_url'])
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('ogpgit'))
