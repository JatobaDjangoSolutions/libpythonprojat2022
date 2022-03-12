from libpythonprojat2022.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'brjatoba92@gmail.com',
        'bruno.jatoba@icat.ufal.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert 'brjatoba92@gmail.com' in resultado
