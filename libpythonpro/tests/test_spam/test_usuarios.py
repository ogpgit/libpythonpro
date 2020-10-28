def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessão()
    usuario = Usuario(nome = 'Osvaldo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_liatar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessão()
    usuarios = [Usuario(nome = 'Osvaldo'), Usuario(nome = 'Silvia')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()