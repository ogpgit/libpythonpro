import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Osvaldo', email='osvaldogpires@gmail.com'),
            Usuario(nome='Silvia', email='silvia1957@gmail.com')
        ],
        [
            Usuario(nome='Osvaldo', email='osvaldogpires@gmail.com')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'osvaldogpires@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Osvaldo', email='osvaldogpires@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'silvia1957@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
    assert enviador.parametros_de_envio == (
        'silvia1957@gmail.com',
        'osvaldogpires@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
