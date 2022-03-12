import pytest

from libpythonprojat2022.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'brjatoba92@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'bruno.jatoba@icat.ufal.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert destinatario in resultado
