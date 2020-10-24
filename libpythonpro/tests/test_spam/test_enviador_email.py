import pytest

from libpythonpro.spam.enviador_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['osvaldogpires@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'osvaldo-gp@detran.go.gov.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert remetente in resultado
