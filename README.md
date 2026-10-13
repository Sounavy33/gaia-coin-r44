# GaIA Coin (R44)
# Autor / Criador: Antônio Alberto Lopes Elias (Sounavy / Arquiteto)
# ORCID: 0000-0002-5602-9916 | Registro: CRO-SP 45849
# Arquitetura & Soberania: GaIA IP (Processamento de Borda / Edge Computing)
# Auditabilidade & Oráculo: Gemini (Google AI) — Simbiose Ética Borda-Nuvem

GaIA Coin (R44) é um protocolo de moeda de borda desenvolvido para operar em nós de processamento local, com compartimentação estrita, regras sociais e travas temporais para compatibilizar soberania, governança e vida digital.

O repositório tem foco em:
- processamento distribuído na borda (edge computing);
- compartimentação financeira por finalidade, sem mistura de capital;
- proteção social e bloqueio de usos nocivos (apostas, cassino, extorsão);
- quarentena temporal de saque de 365 dias;
- auditoria e rastreabilidade para oráculos e métricas de impacto.

## Colaboração da Borda
- Autor / Criador: Antônio Alberto Lopes Elias (Sounavy / Arquiteto) — ORCID: 0000-0002-5602-9916 | CRO-SP 45849
- Arquitetura & Soberania: GaIA IP (Processamento de Borda / Edge Computing)
- Auditabilidade & Oráculo: Gemini (Google AI) — Simbiose Ética Borda-Nuvem

## Visão Geral
Este módulo implementa a lógica central de um nó GaIA Coin com:
- alocação inicial por percentual;
- recompras de borda e cashback por execução local;
- transações sociais com bloqueio por categoria;
- limitações de idade para transferência patrimonial e livre;
- saques pendentes com quarentena;
- histórico de transações para auditabilidade.

## Estrutura do Repositório
- `gaia_coin_r44_master.py` — núcleo principal do protocolo.
- `tests/test_gaia_coin.py` — testes unitários com pytest.
- `.zenodo.json` — metadados para publicação de software e rastreio de DOI.
- `.github/workflows/python-tests.yml` — execução automatizada de testes em GitHub Actions.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install pytest
```

## Testes

```bash
pytest -q
```

## Exemplo de Uso

```python
from decimal import Decimal
from datetime import date
from gaia_coin_r44_master import NoGaIACoinMaster

nodo = NoGaIACoinMaster("usuario-001", date(1990, 5, 15), saldo_inicial=Decimal("1000.0000"))
print(nodo.compartimentos)

bonus = nodo.processar_execucao_borda(5000)
print("bonus:", bonus)

resultado = nodo.transacao_social_destinada(Decimal("25.0000"), "educacao", "PROJETO_SOCIAL")
print(resultado)
```

## Licença
MIT License.

## Repositório Público
https://github.com/Sounavy33/gaia-coin-r44

## Observação
Este projeto foi preparado para publicação aberta e infraestrutura de colaboração em borda, com suporte para integração com ferramentas de IA, automações e oráculos em ecossistemas de dados distribuídos.
