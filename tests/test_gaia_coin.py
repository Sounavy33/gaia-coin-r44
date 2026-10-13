from decimal import Decimal
from datetime import date, timedelta

from gaia_coin_r44_master import NoGaIACoinMaster, SaldoInsuficienteError, NoInativoError


def test_inicializacao_distribui_compartimentos():
    nodo = NoGaIACoinMaster("usuario-001", date(2000, 1, 1), saldo_inicial=Decimal("1000.0000"))

    assert nodo.compartimentos["aposentadoria"] == Decimal("300.0000")
    assert nodo.compartimentos["patrimonio"] == Decimal("250.0000")
    assert nodo.compartimentos["saude"] == Decimal("200.0000")
    assert nodo.compartimentos["educacao"] == Decimal("150.0000")
    assert nodo.compartimentos["livre"] == Decimal("100.0000")


def test_processar_execucao_borda_recompensa_e_aloca():
    nodo = NoGaIACoinMaster("usuario-002", date(1990, 1, 1), saldo_inicial=Decimal("0.0000"))

    reward = nodo.processar_execucao_borda(2000)

    assert reward == Decimal("0.1000")
    assert nodo.compartimentos["aposentadoria"] == Decimal("0.0300")
    assert nodo.compartimentos["patrimonio"] == Decimal("0.0250")
    assert nodo.compartimentos["saude"] == Decimal("0.0200")
    assert nodo.compartimentos["educacao"] == Decimal("0.0150")
    assert nodo.compartimentos["livre"] == Decimal("0.0100")


def test_transacao_social_rejeita_categoria_perigosa():
    nodo = NoGaIACoinMaster("usuario-003", date(1992, 4, 5), saldo_inicial=Decimal("1000.0000"))

    resposta = nodo.transacao_social_destinada(Decimal("25.0000"), "livre", "APOSTAS")

    assert "RECUSADO" in resposta
    assert nodo.compartimentos["livre"] == Decimal("100.0000")


def test_solicitar_saque_cria_pendente_quarentena_e_liberacao():
    nodo = NoGaIACoinMaster("usuario-004", date(1990, 5, 10), saldo_inicial=Decimal("1000.0000"))

    pendente = nodo.solicitar_saque(Decimal("20.0000"), "livre")

    assert pendente.valor == Decimal("20.0000")
    assert pendente.data_liberacao == date.today() + timedelta(days=365)
    assert nodo.compartimentos["livre"] == Decimal("80.0000")

    liberados = nodo.processar_saques_pendentes(data_referencia=pendente.data_liberacao)
    assert len(liberados) == 1
    assert liberados[0].efetivado is True


def test_nodo_inativo_nao_processa_execucao():
    nodo = NoGaIACoinMaster("usuario-005", date(1985, 7, 7), saldo_inicial=Decimal("100.0000"))
    nodo.marcar_inativo()

    try:
        nodo.processar_execucao_borda(50)
        assert False, "Esperava NoInativoError"
    except NoInativoError:
        pass


def test_transacao_sem_saldo_lanca_erro():
    nodo = NoGaIACoinMaster("usuario-006", date(1995, 2, 3), saldo_inicial=Decimal("10.0000"))

    try:
        nodo.transacao_social_destinada(Decimal("50.0000"), "livre", "PROJETO")
        assert False, "Esperava SaldoInsuficienteError"
    except SaldoInsuficienteError:
        pass
