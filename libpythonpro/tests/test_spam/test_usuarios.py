import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture(scope='session')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessão()
    yield sessao_obj
    # Tear Down
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Osvaldo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Osvaldo'), Usuario(nome='Silvia')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar_usuarios()
