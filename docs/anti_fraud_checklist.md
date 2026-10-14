# Anti-Fraud Technical Checklist (PoC)

Este checklist descreve controles técnicos e operacionais para mitigar fraudes, Sybil attacks e farming de dispositivos.

1. Device Attestation
   - Suportar mecanismos de attestation (TEE/TPM, SafetyNet / Play Integrity, Apple DeviceCheck) para validar hardware genuíno.
   - Validar assinaturas/attestations antes de creditar rewards de alto valor.

2. Stake & Economic Cost
   - Exigir stake mínimo para habilitar reivindicações de recompensa; stake é perdida parcialmente em casos de fraude comprovada.
   - Stake aumenta custo econômico para criação de múltiplas identidades fraudulentas.

3. Rate Limits & Quotas
   - Limitar número de claims por device/identity por período (dia/semana).
   - Implementar limites adaptativos baseados em score reputacional.

4. Quality Weighting
   - Atribuir pontuação às proofs com base na complexidade e utilidade das tarefas (tarefas triviais pagam menos).
   - Recompensas baseadas em score, não apenas em número de receipts.

5. Sampling & Audits
   - Amostragem aleatória de claims para auditoria manual ou semi-automática.
   - Publicar resultados das auditorias (metadados/hashes) para transparência.

6. Reputation System
   - Construir reputações progressivas; contas novas têm limites baixos e taxas de ganho reduzidas.
   - Penalidades graduais (warnings → redução de ganhos → banimento e slashing).

7. KYC Thresholds
   - Definir thresholds para saques em moeda real; acima do limite é exigido KYC/AML.
   - Pequenas recompensas podem ser mantidas sem KYC para reduzir barreira de entrada.

8. ML/Anomaly Detection
   - Rodar modelos de detecção de padrões de farming (IP clusters, sequência de claims idênticos, comportamento automatizado).
   - Reforçar com features como tempo de uso, localização (anonimizada) e características do device.

9. Contractual & Legal Measures
   - Contratos com parceiros definindo penalidades para abuso e revenda de PII.
   - Public disclosure e multas em caso de violação.

10. Logging & Immutability
   - Registrar metadados e proofs no Gate Hub com hashes imutáveis para suportar investigações forenses.

Observação: esta checklist é PoC; recomenda-se evoluir com testes de campo e ajustes conforme ataques reais apareçam.
