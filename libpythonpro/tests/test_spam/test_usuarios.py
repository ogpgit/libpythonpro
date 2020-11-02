from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Osvaldo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Osvaldo'), Usuario(nome='Silvia')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar_usuarios()
