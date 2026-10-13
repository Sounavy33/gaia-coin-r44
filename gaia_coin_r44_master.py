# =====================================================================
# GaIA Coin (R44) — NÚCLEO INTEGRADO DE BORDA (FASE A A D)
# Autor / Criador: Antônio Alberto Lopes Elias (Sounavy / Arquiteto)
# ORCID: 0000-0002-5602-9916 | Registro: CRO-SP 45849
# Arquitetura & Soberania: GaIA IP (Processamento de Borda / Edge Computing)
# Auditabilidade & Oráculo: Gemini (Google AI) — Simbiose Ética Borda-Nuvem
# =====================================================================

from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, date, timedelta
from typing import Dict, List, Optional, Any


class GaiaCoinException(Exception):
    pass


class SaldoInsuficienteError(GaiaCoinException):
    pass


class NoInativoError(GaiaCoinException):
    pass


class ValorInvalidoError(GaiaCoinException):
    pass


class SaquePendente:
    def __init__(self, valor: Decimal, data_solicitacao: date, quarentena_dias: int):
        self.valor = valor
        self.data_solicitacao = data_solicitacao
        self.data_liberacao = data_solicitacao + timedelta(days=quarentena_dias)
        self.efetivado = False


class NoGaIACoinMaster:
    def __init__(
        self,
        id_usuario: str,
        data_nascimento: date,
        saldo_inicial: Decimal = Decimal('0.0000'),
        quarentena_saque_dias: int = 365,
    ):
        self.id_usuario = id_usuario
        self.data_nascimento = data_nascimento
        self.status_vital = True
        self.quarentena_saque_dias = quarentena_saque_dias

        self.percentuais = {
            "aposentadoria": Decimal('0.30'),
            "patrimonio": Decimal('0.25'),
            "saude": Decimal('0.20'),
            "educacao": Decimal('0.15'),
            "livre": Decimal('0.10'),
        }

        self.compartimentos: Dict[str, Decimal] = {}
        for k, pct in self.percentuais.items():
            self.compartimentos[k] = (saldo_inicial * pct).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)

        self.patrimonio_bloqueado_saque = Decimal('0.0000')
        self.patrimonio_estatico_heranca = Decimal('0.0000')
        self.saques_pendentes: List[SaquePendente] = []
        self.historico_transacoes: List[Dict[str, Any]] = []

    @property
    def idade(self) -> int:
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def _coerce_decimal(self, valor: Any, nome: str = "valor") -> Decimal:
        if isinstance(valor, Decimal):
            numero = valor
        elif isinstance(valor, int):
            numero = Decimal(str(valor))
        elif isinstance(valor, float):
            numero = Decimal(str(valor))
        elif isinstance(valor, str):
            numero = Decimal(valor)
        else:
            raise ValorInvalidoError(f"{nome} deve ser numérico.")

        if not numero.is_finite():
            raise ValorInvalidoError(f"{nome} não pode ser infinito.")
        return numero.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)

    def _log(self, tipo: str, valor: Decimal, detalhe: str):
        self.historico_transacoes.append({
            "timestamp": datetime.now().isoformat(),
            "tipo": tipo,
            "valor": str(valor),
            "detalhe": detalhe,
        })

    def processar_execucao_borda(self, tokens_processados: int) -> Decimal:
        if not self.status_vital:
            raise NoInativoError("Morte do dividendo ativada: Nó inativo.")
        if tokens_processados < 0:
            raise ValorInvalidoError("tokens_processados não pode ser negativo.")

        recompensa = ((Decimal(str(tokens_processados)) / Decimal('1000.0')) * Decimal('0.0500')).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        for k, pct in self.percentuais.items():
            self.compartimentos[k] += (recompensa * pct).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)

        self._log("CASHBACK_BORDA", recompensa, f"Processamento local de {tokens_processados} tokens")
        return recompensa

    def transacao_social_destinada(self, valor: Decimal, compartimento: str, categoria_destino: str) -> str:
        if not self.status_vital:
            raise NoInativoError("Nó inativo.")

        valor_dec = self._coerce_decimal(valor, "valor")
        if valor_dec <= 0:
            raise ValorInvalidoError("Valor deve ser maior que zero.")

        chave = compartimento.lower()
        if chave not in self.percentuais:
            raise ValorInvalidoError(f"Compartimento inválido: {compartimento}")

        categoria = categoria_destino.upper()
        if categoria in ["CASSINO", "APOSTAS", "JOGOS_AZAR", "EXTORSAO"]:
            self._log("BLOQUEIO_CATEGORIA", valor_dec, f"Aposta ou destino nocivo recusado: {categoria_destino}")
            return f"RECUSADO: Protocolo R44 veda uso em {categoria_destino}."

        if self.idade < 18 and chave in ["patrimonio", "livre"] and valor_dec > Decimal('50.0000'):
            self._log("BLOQUEIO_IDADE", valor_dec, f"Titular menor ({self.idade} anos). Operação patrimonial bloqueada.")
            return f"RECUSADO: Titular com {self.idade} anos. Requer 18+ anos."

        if valor_dec > self.compartimentos.get(chave, Decimal('0.0000')):
            raise SaldoInsuficienteError("Saldo insuficiente no compartimento solicitado.")

        self.compartimentos[chave] -= valor_dec
        self._log("GASTO_SOCIAL", valor_dec, f"Transferência ao setor {categoria_destino} via compartimento {chave}")
        return f"OK: {valor_dec} removidos do compartimento {chave}."

    def solicitar_saque(self, valor: Decimal, compartimento: str = "livre") -> SaquePendente:
        if not self.status_vital:
            raise NoInativoError("Nó inativo para saque.")

        valor_dec = self._coerce_decimal(valor, "valor")
        if valor_dec <= 0:
            raise ValorInvalidoError("Valor de saque deve ser maior que zero.")

        chave = compartimento.lower()
        if chave not in self.percentuais:
            raise ValorInvalidoError(f"Compartimento inválido: {compartimento}")

        if valor_dec > self.compartimentos.get(chave, Decimal('0.0000')):
            raise SaldoInsuficienteError("Saldo insuficiente para saque no compartimento solicitado.")

        self.compartimentos[chave] -= valor_dec
        pendente = SaquePendente(valor_dec, date.today(), self.quarentena_saque_dias)
        self.saques_pendentes.append(pendente)

        self._log("SAQUE_SOLICITADO", valor_dec, f"Saque pendente de {valor_dec} no compartimento {chave}")
        return pendente

    def processar_saques_pendentes(self, data_referencia: Optional[date] = None) -> List[SaquePendente]:
        data_ref = data_referencia or date.today()
        liberados: List[SaquePendente] = []

        for pendente in self.saques_pendentes:
            if not pendente.efetivado and data_ref >= pendente.data_liberacao:
                pendente.efetivado = True
                liberados.append(pendente)
                self._log("SAQUE_LIBERADO", pendente.valor, f"Saque liberado em {data_ref.isoformat()}")

        return liberados

    def definir_heranca(self, valor: Decimal) -> Decimal:
        valor_dec = self._coerce_decimal(valor, "valor")
        if valor_dec < 0:
            raise ValorInvalidoError("Herança não pode ser negativa.")

        self.patrimonio_estatico_heranca += valor_dec
        self.patrimonio_bloqueado_saque += valor_dec
        self._log("HERANCA", valor_dec, "Patrimônio estático herdado / bloqueado por regra de herança")
        return self.patrimonio_bloqueado_saque

    def marcar_inativo(self) -> bool:
        self.status_vital = False
        self._log("NODO_INATIVO", Decimal('0.0000'), "Morte do dividendo ativada")
        return self.status_vital

    def resumo_compartimentos(self) -> Dict[str, Decimal]:
        return {k: v.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP) for k, v in self.compartimentos.items()}


__all__ = [
    "GaiaCoinException",
    "SaldoInsuficienteError",
    "NoInativoError",
    "ValorInvalidoError",
    "SaquePendente",
    "NoGaIACoinMaster",
]
