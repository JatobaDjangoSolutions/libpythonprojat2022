import pytest

from libpythonprojat2022.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'brjatoba92@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'bruno.jatoba@icat.ufal.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'brjatoba92']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'bruno.jatoba@icat.ufal.br',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )
